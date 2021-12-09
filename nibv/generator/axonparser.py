"""
 https://nipype.readthedocs.io/en/latest/devel/interface_specs.html#traited-attributes
"""
import subprocess
from tqdm import tqdm

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
