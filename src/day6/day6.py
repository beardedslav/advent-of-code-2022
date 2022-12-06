import argparse
import sys
import time
from collections import deque

NO_OF_UNIQUE_CHARS = 4

def main(args):
    with open('data/day6/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    inputFileContents = inputFileContents.strip()
    st = time.process_time()
    print(next(i + NO_OF_UNIQUE_CHARS for i in range(len(inputFileContents)-NO_OF_UNIQUE_CHARS) if len(set(inputFileContents[i:i+NO_OF_UNIQUE_CHARS])) == NO_OF_UNIQUE_CHARS))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))