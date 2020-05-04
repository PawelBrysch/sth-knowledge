import sys
import os
import argparse


def parse_arguments(input_):
    input_ = input_[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_path', type=str)
    parser.add_argument('output_dir', type=str)
    return parser.parse_args(input_)


def do_your_stuff(input_file_path, output_dir):
    lines_to_prepend = [
        "# Since now, this file is :\n",
        "# COMPILED !!!\n"
    ]

    with open(input_file_path, "r") as infile:
        lines = infile.readlines()
        lines = lines_to_prepend + lines

    output_file_path = os.path.join(
        output_dir,
        os.path.basename(input_file_path)
    )

    with open(output_file_path, "w") as outfile:
        outfile.writelines(lines)


def main(input):
    parsed_args = parse_arguments(input)
    do_your_stuff(**vars(parsed_args))
    return 0


if __name__ == '__main__':
    # sys.argv = [
    #     "nothing",
    #     rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\les_Jenkins\workspace_mock\src\some_module.py",
    #     rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\les_Jenkins\workspace_mock\target"
    # ]
    sys.exit(main(sys.argv))

