#!/usr/bin/env python3
import argparse
from gendiff.modules.generate import generate_diff
import json


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', help='set format of output')
args = parser.parse_args()

def main():
    with open(args.first_file) as f1:
        data1 = json.load(f1)
    with open(args.second_file) as f2:
        data2 = json.load(f2)
    diff = generate_diff(data1, data2)
    print(diff)



if __name__ == '__main__':
    main()