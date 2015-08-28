#!/usr/bin/env python

import argparse
import sys

def define_parser():
    parser = argparse.ArgumentParser(description="Compute sums")
    parser.add_argument('-n', action="store_const", const=True, default=False, help="set the first integer as the total number")
    return parser

if __name__ == '__main__':
    parser = define_parser()
    args = parser.parse_args()

    if args.n:
        n = input()
        s = 0
        for i in range(n):
            s += input()
        print s
    else:
        s = 0
        for line in sys.stdin:
            line = line.split()
            for each in line:
                s += int(each)
        print s

