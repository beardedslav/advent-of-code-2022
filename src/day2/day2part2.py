import argparse
import sys
import time

POINTS = {'A' : 1, 'B' : 2, 'C' : 3}

RESULT = {'X' : 0, 'Y' : 3, 'Z' : 6}

def score(line):
    p1, p2 = line.split(' ')
    return RESULT[p2] + (((POINTS[p1] + RESULT[p2]//3-1) % 3) or 3)

def main(args):
    st = time.process_time()
    with open('data/day2/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    print(sum( map( score, inputFileContents.split('\n'))))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))