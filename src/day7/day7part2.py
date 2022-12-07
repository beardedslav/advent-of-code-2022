import argparse
import sys
import time
from os import path

def main(args):
    with open('data/day7/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    dirSizes = dict()
    currentDirs = []
    for line in inputFileContents.split('\n'):
        lineData = line.split(' ')
        if lineData[0] == '$':
            if lineData[1] == 'cd':
                if lineData[2] == '..':
                    currentDirs.pop()
                else:
                    prefix = currentDirs[-1] if currentDirs else ''
                    dirPath = path.join(prefix,lineData[2])
                    currentDirs.append(dirPath)
                    dirSizes[dirPath] = 0
        elif lineData[0] != 'dir':
            for dir in currentDirs:
                dirSizes[dir] += int(lineData[0])
    print(min(v for _, v in dirSizes.items() if v > (30000000 - (70000000 - dirSizes['/']))))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))