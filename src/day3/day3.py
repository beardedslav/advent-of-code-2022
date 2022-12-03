import argparse
import sys
import time
import string

PRIORITIES = {letter :  value+1 for value, letter in enumerate(string.ascii_letters)}

def main(args):
    st = time.process_time()
    with open('data/day3/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.readlines()
    st = time.process_time()
    print(sum(sum( PRIORITIES[letter] for letter in set(s[:len(s)//2])&set(s[len(s)//2:])) for s in inputFileContents ))

    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))