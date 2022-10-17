import subprocess
from tqdm import tqdm
from warnings import warn

from nibv.generator.utils import parse_node, hide_text


def parse_signature(string):
    # Remove "signature = Signature(" ... ")"
    string = string[string.find('(')+1:-1]
    # Replace text by identifiers
    hstring, text_elements = hide_text(string)
    # Remove spaces
    hstring = hstring.replace(" ", "")
    # Extract structure
    items = parse_node(hstring, text_elements)

    traits = {}
    for i in range(0, len(items), 2):
        params = {}
        values = []
        for val in items[i+1][1]:
            if isinstance(val, tuple) and val[0] in ['requiredAttributes', 'exactType']:
                params[val[0]] = val[1]
            else:
                values.append(val)
        traits[items[i]] = {'type': items[i+1][0],
                            'values': values, 'params': params}
    return traits


def parse_signature_of(fname):
    # Read the process script
    script = subprocess.check_output(
        ['bv', 'cat', fname]).decode('utf-8').split('\n')

    # Read and concatenate the signature lines
    p = 0
    signature = None
    while p < len(script):
        line = script[p]
        if line.startswith("signature = "):
            signature = line
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
        warn("No axon signature in {}".format(fname))
        return None, None

    # Parse the signature
    traits = parse_signature(signature)

    if len(traits) < 1:
        warn("Empty signature in {}".format(fname))
        return None, None

    return traits, signature


def list_toolboxes():
    description = subprocess.check_output(
        ['bv', 'axon-runprocess', '--list']).decode('utf-8').split('\n')

    toolboxes = set()
    for line in description:
        if line.startswith("    toolbox: "):
            toolboxes.add(line[13:])
    return toolboxes


def list_process_files(toolbox):
    description = subprocess.check_output(
        ['bv', 'axon-runprocess', '--list']).decode('utf-8').split('\n')

    current_process = {}
    processes = []
    for line in tqdm(description, desc="Parsing the axon processes", unit="lines"):
        if line.startswith("Process ID: "):
            current_process['id'] = line[12:]
        elif line.startswith("    name: "):
            current_process['name'] = line[10:]
        elif line.startswith("    toolbox: "):
            current_process['toolbox'] = line[13:]
        elif line.startswith("    fileName: "):
            current_process['filename'] = line[14:]
            if current_process['toolbox'] == toolbox:
                signature, raw = parse_signature_of(
                    current_process['filename'])
                current_process['signature'] = signature
                current_process['raw'] = raw
                if current_process:
                    processes.append(current_process)
            current_process = {}
    return processes
