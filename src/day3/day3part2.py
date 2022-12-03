import argparse
import sys
import time
import string

PRIORITIES = {letter :  value+1 for value, letter in enumerate(string.ascii_letters)}

def main(args):
    st = time.process_time()
    with open('data/day3/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    print(sum(sum(PRIORITIES[letter] for letter in group) for group in (set(group[0]) & set(group[1]) & set(group[2]) for group in zip(*(iter(inputFileContents.split('\n')),) * 3))))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))