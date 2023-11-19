#!/usr/bin/env python3
from gendiff.cli import parsing_arguments
from gendiff.modules.generate import generate_diff
from gendiff.parser import parser


def main():
    first_file, second_file, formats = parsing_arguments()
    data1 = parser(first_file)
    data2 = parser(second_file)
    diff = generate_diff(data1, data2)
    print(diff)


if __name__ == '__main__':
    main()
