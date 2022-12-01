import argparse
import sys
import time

def main(args):
    with open('data/day1/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    res = sum(sorted(map(lambda s: sum(map(int, s.split(' ') )), ' '.join(inputFileContents.split('\n')).split('  ')))[-3:])
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    print(res)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))