"""
 https://nipype.readthedocs.io/en/latest/devel/interface_specs.html#traited-attributes
"""
import os.path as op
import json
import sys
import subprocess
from tqdm import tqdm
from os import makedirs, listdir
import importlib
import inspect

"""

Signature('Commissure_coordinates', ReadDiskItem('Commissure coordinates', 'Commissure coordinates'), 'T1mri',
          ReadDiskItem("T1 MRI", 'aims readable Volume Formats'), 'validation', Choice("Visualise", "Lock", "Unlock"),)

Inout string
'element1', [nodenameA]('elementA1', [nodenameB]('elementB1', 'elementB2'), 'elementA3'), [
                        nodename]('elementB1', [nodenameB]('elementB1', 'elementB2'), 'elementA3'),
Output dict:
{
    "element1": []
    "nodenameA": [
        "elementA1": None
        "nodenameB": ['elementB1', 'elementB2'],
        "elementA3": None
}
"""


def remove(string, *args):
    for s in args:
        string = string.replace(s, "")
    return string


def find_element_limit(node):
    i = 0
    depth = 0
    while i < len(node):
        if node[i] == '(':
            depth += 1
        elif node[i] == ')':
            depth -= 1
            if depth == 0:
                return i
        i += 1
    return -1


def parse_node(node):
    elements = []
    while len(node):
        par = node[1:].find('(')
        vir = node.find(',')
        par = par + 1 if par > -1 else 1000000
        vir = vir if vir > -1 else 1000000
        if par == 1000000 and vir == 1000000:
            nodename = node
            subelements = None
            node = ''
        elif vir < par:
            # Next node is just a string
            nodename = node[:vir].strip()
            subelements = None
            node = node[vir+1:]
        else:
            # Next node is a Class
            nodename = node[0:par].strip()
            end = find_element_limit(node) + 1
            subelements = parse_node(node[par:end])
            node = node[end+2:]
        nodename = nodename.replace("'", "").replace("(", "").replace(")", "")
        elements.append((nodename, subelements))
    return elements


def parse_process(fname):
    script = subprocess.check_output(
        ['bv', 'cat', fname]).decode('utf-8').split('\n')

    p = 0
    signature = None
    while p < len(script):
        line = script[p]
        if line.startswith("signature = "):
            signature = line[12:]
            p += 1
            while len(script[p].strip()):
                lstr = script[p].strip()
                idx = lstr.find('#')
                if idx > -1:
                    signature += lstr[:idx]
                else:
                    signature += lstr
                p += 1
            break
        p += 1

    if signature is None:
        print("No signature in", fname)
        return None

    sign_dict = parse_node(signature)[0][1]
    inputs = {}
    for i in range(0, len(sign_dict), 2):
        inputs[sign_dict[i][0]] = sign_dict[i+1]
    return inputs


def list_process_files(toolbox):
    description = subprocess.check_output(
        ['bv', 'axon-runprocess', '--list']).decode('utf-8').split('\n')
    print("{} lines".format(len(description)))

    current_process = {}
    processes = []
    for line in tqdm(description):
        if line.startswith("Process ID: "):
            current_process['id'] = line[12:]
        elif line.startswith("    name: "):
            current_process['name'] = line[10:]
        elif line.startswith("    name: "):
            current_process['name'] = line[10:]
        elif line.startswith("    toolbox: "):
            current_process['toolbox'] = line[13:]
        elif line.startswith("    fileName: "):
            current_process['filename'] = line[14:]
            if current_process['toolbox'] == toolbox:
                try:
                    current_process['arguments'] = parse_process(
                        current_process['filename'])
                    if current_process:
                        processes.append(current_process)
                except IndexError:
                    pass
            current_process = {}
    return processes


def generate_file_trait(argname, position, description="", input=True, mandatory=False):
    """
        t1_file = traits.File(
            exists=True,
            desc='Whole-head T1w image',
            mandatory=True, position=0, argstr="%s")
    """
    return "    {} = traits.File(\n        exists={},\n        desc='{}',\n        position={}, mandatory={}, argstr='%s')\n".format(
        argname, "True" if input else "False", description, position, "True" if mandatory else "False")


def generate_out_file_trait(argname, description):
    """
        t2_coreg_file = File(
            desc="coreg T2 from T1")
    """
    return "    {} = traits.File(\n        desc='{}')\n".format(argname, description)


def generate_float_trait(argname, position, description="", default=None, mandatory=False):
    """
        f = traits.Float(
            0.5, usedefault=True,
            desc='-f options of BET: fractional intensity threshold (0->1); \
                default=0.5; smaller values give larger brain outline estimates',
            argstr="-f %f", mandatory=False)
    """
    description = remove(description, '"', "'")
    return "    {} = traits.Float(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%f', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_int_trait(argname, position, description="", default=None, mandatory=False):
    description = remove(description, '"', "'")
    return "    {} = traits.Int(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%d', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_str_trait(argname, position, description="", default=None, mandatory=False):
    description = remove(description, '"', "'")
    return "    {} = traits.String(\n        {},\n        usedefault={},\n        desc='{}',\n        position={}, argstr='%s', mandatory={})\n".format(
        argname, default, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_bool_trait(argname, position, description="", default=None, mandatory=False):
    """
        k = traits.Bool(
            False, usedefault=True, argstr="-k",
            desc="Will keep temporary files",
            mandatory=False)
    """
    description = remove(description, '"', "'")
    return "    {} = traits.Bool(\n        {}, usedefault={},\n        argstr='%s',\n        desc='{}',\n        position={}, mandatory={})\n".format(
        argname, "True" if default else "False", "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_enum_trait(argname, position, values, description="", default=None, mandatory=False):
    """
        jobtype = traits.Enum('estwrite', 'estimate', 'write',
                          desc='one of: estimate, write, estwrite',
                          usedefault=True)
    """
    if len(values) > 0 and len(values[0]) > 0:
        values = list(('' if len(v) == 0 else '"{}"'.format(
            remove(v, "'", '"').strip())) for v in values)
        vals = []
        for v in values:
            if len(v) > 0:
                vals.append(v)
        values_str = (", ".join(vals) + ",\n        ")
    else:
        print("/!\ empty enum", argname, ":", values)
        return ""

    description = remove(description, '"', "'")
    return "    {} = traits.Enum(\n        {}usedefault={},\n        desc='{}',\n        position={}, mandatory={})\n".format(
        argname, values_str, "True" if default is not None else "False",
        description, position, "True" if mandatory else "False")


def generate_inputspec(process, process_node_name):
    if process['arguments'] is None:
        print("{} do not have any arguments".format(process['id']))
        return None, None
    script = "\nclass {}InputSpec(CommandLineInputSpec):\n".format(
        process_node_name)
    out_files = []
    position = 0
    traits_script = ""
    for position, (argname, (argtype, params)) in enumerate(process['arguments'].items()):
        if params is not None:
            params = list(item[0] for item in params)
        else:
            params = []
        argname = remove(argname.lower(), '"').strip()

        if params:
            desc = remove(", ".join(params), "'", '"', "[", "]")
        else:
            desc = ""
        if argtype == "ReadDiskItem":
            tscript = generate_file_trait(argname, position, desc, input=True)
        elif argtype == "WriteDiskItem":
            tscript = generate_file_trait(
                argname, position, desc, input=False)
            out_files.append((argname, desc))
        elif argtype == "Float":
            tscript = generate_float_trait(argname, position, desc)
        elif argtype == "Integer":
            tscript = generate_int_trait(argname, position, desc)
        elif argtype == "String":
            tscript = generate_str_trait(argname, position, desc)
        elif argtype == "Choice":
            tscript = generate_enum_trait(argname, position, params, desc)
        elif argtype == "Boolean":
            tscript = generate_bool_trait(argname,
                                          position, desc,  default=False)
        else:
            # print(process['id'], "Unimplemented argtype:", argtype)
            # print(process['filename'])
            continue
        if len(tscript) == 0:
            print("Empty trait script in ", process['id'])
            continue
        traits_script += tscript
        position += 1

    if len(traits_script) == 0:
        script += "    pass\n"
    else:
        script += traits_script

    return script, out_files


def generate_outputspec(proc_name, out_files):
    script = "class {}OutputSpec(TraitedSpec):\n".format(proc_name)
    if len(out_files) == 0:
        script += "    pass\n"
    else:
        for f, desc in out_files:
            script += generate_out_file_trait(f, desc)
    return script


def generate_nipype_wrap(toolbox, process):
    name = "_" + process['id']
    name = name.replace("-", "_")

    idx = name.find("_")
    while idx > -1:
        name = name[:idx] + name[idx+1].upper() + name[idx+2:]
        idx = name.find("_")

    inspec, out_files = generate_inputspec(process, name)
    if inspec is None:
        return
    outspec = generate_outputspec(name, out_files)
    script = "from nipype.interfaces.base import (CommandLineInputSpec, TraitedSpec)\n" \
             "from nipype.interfaces.base import traits\n" \
             "from nibv.base import BVCommand\n" \
             "\n{}" \
             "\n" \
             "\n{}" \
             "\n" \
             "\n" \
             "class {}(BVCommand):\n" \
             "    input_spec = {}InputSpec\n" \
             "    output_spec = {}OutputSpec\n" \
             "    _cmd = '{}'\n\n" \
        .format(
            inspec,
            outspec,
            name,
            name,
            name,
            name,
            name
        )

    tb_dir = op.realpath(
        op.join(op.split(__file__)[0], "..", "nibv", "interfaces", toolbox))
    script_f = op.join(tb_dir, name.lower() + ".py")

    makedirs(tb_dir, exist_ok=True)

    with open(script_f, 'w') as f:
        f.write(script)


def list_classnames(toolbox, module):
    module_path = 'nibv.interfaces.{}.{}'.format(toolbox, module)
    cnames = []
    for name, cls in inspect.getmembers(importlib.import_module(module_path), inspect.isclass):
        cnames.append(name)
    return cnames


def create_init_file(tb_dir):
    script = ""

    with open(op.join(tb_dir, '__init__.py'), 'w') as f:
        f.write(script)


def create_tb_init_file(tb_dir, toolbox):
    script = ""
    for item in sorted(listdir(tb_dir)):
        if item.endswith('.py') and not item.startswith("__"):
            cnames = list_classnames(toolbox, item[:-3])
            if len(cnames) == 0:
                continue
            filt_cnames = []
            for name in cnames:
                if not name.endswith("Spec") and name != "BVCommand":
                    filt_cnames.append(name)

            script += "from .{} import {}\n".format(
                item[:-3], ", ".join(filt_cnames))

    with open(op.join(tb_dir, '__init__.py'), 'w') as f:
        f.write(script)


if __name__ == "__main__":
    toolbox = sys.argv[1]

    # List processes and read input specs
    # signatures = list_process_files(sys.argv[1])
    # print(len(signatures), "processes")
    # if len(sys.argv) > 2:
    #     with open(sys.argv[2], 'w') as f:
    #         json.dump(signatures, f)

    # Create wraps without outputs
    signatures = json.load(open(sys.argv[2], 'r'))
    for sign in tqdm(signatures):
        generate_nipype_wrap(toolbox, sign)

    i_dir = op.realpath(
        op.join(op.split(__file__)[0], "..", "nibv", "interfaces"))
    create_init_file(i_dir)

    tb_dir = op.join(i_dir, toolbox)
    create_tb_init_file(tb_dir, toolbox)

    # Create __init__.py files
    # if not op.isfile(toolbox):
    #     makedirs(tb_dir)

    #     with open(op.join(tb_dir, '__init__.py'), 'w') as f:
    #         f.write("")

    # Run the wraps to procude outputs

    # Read outputs and modify output spec
