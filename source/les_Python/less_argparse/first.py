#!/usr/bin/env python
# TODO zbadac te linijke powyzej

import sys
import argparse


def parse_arguments(input_):
    """first element is just a script's path"""
    input_ = input_[1:]
    parser = argparse.ArgumentParser()
    parser.add_argument('name_of_arg1', type=str)
    parser.add_argument('name_of_arg2', type=str)
    return parser.parse_args(input_)


def do_your_stuff(name_of_arg1, name_of_arg2):
    pass


def main(input):
    parsed_args = parse_arguments(input)
    do_your_stuff(**vars(parsed_args))
    return 0


if __name__ == '__main__':
    """you can mock if you want"""
    # sys.argv = [
    #     "nothing",
    #     rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\les_Jenkins\workspace_mock\src\some_module.py",
    #     rf"C:\Users\Lenovo\Desktop\PROJECTS\django_top2\sth-knowledge\source\les_Jenkins\workspace_mock\target"
    # ]
    sys.exit(main(sys.argv))