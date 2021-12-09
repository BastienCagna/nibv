import os.path as op
import json
import sys
from tqdm import tqdm

import nibv.generator.wrapper as gw


def main():
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
        gw.generate_nipype_wrap(toolbox, sign)

    i_dir = op.realpath(
        op.join(op.split(__file__)[0], "..", "nibv", "interfaces"))
    gw.create_init_file(i_dir)

    tb_dir = op.join(i_dir, toolbox)
    gw.create_tb_init_file(tb_dir, toolbox)

    # Create __init__.py files
    # if not op.isfile(toolbox):
    #     makedirs(tb_dir)

    #     with open(op.join(tb_dir, '__init__.py'), 'w') as f:
    #         f.write("")

    # Run the wraps to procude outputs

    # Read outputs and modify output spec


if __name__ == "__main__":
    main()
