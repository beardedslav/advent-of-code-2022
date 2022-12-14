import argparse
import sys
import time

def main(args):
    with open('data/day4/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    contains = lambda pair1, pair2 : int((pair1[0]<= pair2[0] and pair1[1] >= pair2[1]) or (pair1[0]>= pair2[0] and pair1[1] <= pair2[1]))
    print(sum(map( lambda pair : contains(list(map(int,(pair[0].split('-')))), list(map(int,(pair[1].split('-'))))), map(lambda l: l.split(','),inputFileContents.split('\n')))))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))