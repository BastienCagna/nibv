import os.path as op
import json
import sys
import argparse
from tqdm import tqdm

import nibv.generator.wrapper as gw
from nibv.generator.axonparser import list_toolboxes, list_process_files


def main():
    # Command line parser
    parser = argparse.ArgumentParser(
        description="Wrap axon processes")
    parser.add_argument('toolboxes', nargs='*',
                        help="specify needed toolbox if you don't want to generate wraps for all")
    args = parser.parse_args()

    # List toolboxes
    avail_toolboxes = list_toolboxes()
    print("Available toolboxes:", avail_toolboxes)
    toolboxes = set()
    if len(args.toolboxes) > 0:
        for t in args.toolboxes:
            if t in avail_toolboxes:
                toolboxes.add(t)
    else:
        toolboxes = avail_toolboxes

    # Process each ones
    for toolbox in toolboxes:
        print("-- Parsing toolbox:", toolbox)

        # List processes and read input specs
        signatures = list_process_files(toolbox)
        print(len(signatures), "processes in", toolbox)
        # if len(sys.argv) > 2:
        #     with open(sys.argv[2], 'w') as f:
        #         json.dump(signatures, f)

        # Create wraps without outputs
        # signatures = json.load(open(sys.argv[2], 'r'))
        for sign in tqdm(signatures):
            gw.create_nipype_wrap(toolbox, sign)

        i_dir = op.realpath(
            op.join(op.split(__file__)[0], "..", "nibv", "interfaces"))
        gw.create_init_file(i_dir)

        tb_dir = op.join(i_dir, toolbox)
        gw.create_tb_init_file(tb_dir, toolbox)


if __name__ == "__main__":
    main()
