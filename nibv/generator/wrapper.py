import os.path as op
from os import makedirs, listdir
import importlib
import inspect

import nibv.generator.traits as gt
from nibv.generator.utils import remove_characters


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
        argname = remove_characters(argname.lower(), '"').strip()

        if params:
            desc = remove_characters(", ".join(params), "'", '"', "[", "]")
        else:
            desc = ""
        if argtype == "ReadDiskItem":
            tscript = gt.generate_file_trait(
                argname, position, desc, input=True)
        elif argtype == "WriteDiskItem":
            tscript = gt.generate_file_trait(
                argname, position, desc, input=False)
            out_files.append((argname, desc))
        elif argtype == "Float":
            tscript = gt.generate_float_trait(argname, position, desc)
        elif argtype == "Integer":
            tscript = gt.generate_int_trait(argname, position, desc)
        elif argtype == "String":
            tscript = gt.generate_str_trait(argname, position, desc)
        elif argtype == "Choice":
            tscript = gt.generate_enum_trait(argname, position, params, desc)
        elif argtype == "Boolean":
            tscript = gt.generate_bool_trait(argname,
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
            script += gt.generate_out_file_trait(f, desc)
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
