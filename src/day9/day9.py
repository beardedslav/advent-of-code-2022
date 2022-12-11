import argparse
import sys
import time

def cmp(a,b):
    return (a > b) - (a < b)

def main(args):
    with open('data/day9/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    tailPositions = {(0, 0)}
    headPos = (0, 0)
    tailPos = (0, 0)
    for line in inputFileContents.split('\n'):
        dir, dist = line.split(' ')
        dist = int(dist)
        for _ in range(dist):
            if dir == 'R':
                headPos = (headPos[0]+1, headPos[1])
            if dir == 'U':
                headPos = (headPos[0], headPos[1]+1)
            if dir == 'L':
                headPos = (headPos[0]-1, headPos[1])
            if dir == 'D':
                headPos = (headPos[0], headPos[1]-1)
            if headPos[0] == tailPos[0] or headPos[1] == tailPos[1]:
                if headPos[0] == tailPos[0]:
                    if abs(headPos[1]-tailPos[1]) == 2:
                        tailPos = (tailPos[0], tailPos[1] + (headPos[1]-tailPos[1])//2)
                elif headPos[1] == tailPos[1]:
                    if abs(headPos[0]-tailPos[0]) == 2:
                        tailPos = (tailPos[0] + (headPos[0]-tailPos[0])//2, tailPos[1])
            elif abs(headPos[0]-tailPos[0]) > 1 or abs(headPos[1]-tailPos[1]) > 1:
                tailPos = (tailPos[0] + cmp(headPos[0],tailPos[0]), tailPos[1] + cmp(headPos[1],tailPos[1]))     
            tailPositions.add(tailPos)
    print(len(tailPositions))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))