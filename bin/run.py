#!/usr/bin/env python3

import os
import sys
import argparse

# Subpackages integration section #############################################
SOURCE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
os.chdir(SOURCE_ROOT)
# Add library dirs into search path
for path in [SOURCE_ROOT]:
    if path not in sys.path:
        #    sys.path.append(path)
        sys.path.insert(1, path)    # inserting path after current dir
###############################################################################

from lib.DictLoader import DictLoader
from lib.Matrix import Matrix
from lib.Searcher import Searcher

#
# Base execution section
#
if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--size', help='Sets matrix size (default: %(default)s)',
                        nargs='?', const='localhost', default=15, type=int)
    args = parser.parse_args()

    print(args)

    words = DictLoader('words.txt')
    mx = Matrix(args.size)
    s = Searcher(mx, words)
    s.search()
