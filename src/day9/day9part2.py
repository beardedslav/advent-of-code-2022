import argparse
import sys
import time

def cmp(a,b):
    return (a > b) - (a < b)

def newTailPos(headPos, tailPos):
    newTailPos = tailPos
    if headPos[0] == tailPos[0] or headPos[1] == tailPos[1]:
        if headPos[0] == tailPos[0]:
            if abs(headPos[1]-tailPos[1]) == 2:
                newTailPos = (tailPos[0], tailPos[1] + (headPos[1]-tailPos[1])//2)
        elif headPos[1] == tailPos[1]:
            if abs(headPos[0]-tailPos[0]) == 2:
                newTailPos = (tailPos[0] + (headPos[0]-tailPos[0])//2, tailPos[1])
    elif abs(headPos[0]-tailPos[0]) > 1 or abs(headPos[1]-tailPos[1]) > 1:
        newTailPos = (tailPos[0] + cmp(headPos[0],tailPos[0]), tailPos[1] + cmp(headPos[1],tailPos[1])) 
    return newTailPos

def main(args):
    with open('data/day9/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    tailPositions = {(0, 0)}
    rope = [(0,0) for _ in range(10)]
    for line in inputFileContents.split('\n'):
        dir, dist = line.split(' ')
        dist = int(dist)
        for _ in range(dist):
            if dir == 'R':
                rope[0] = (rope[0][0]+1, rope[0][1])
            if dir == 'U':
                rope[0] = (rope[0][0], rope[0][1]+1)
            if dir == 'L':
                rope[0] = (rope[0][0]-1, rope[0][1])
            if dir == 'D':
                rope[0] = (rope[0][0], rope[0][1]-1)
            for i in range(9):
                rope[i+1] = newTailPos(rope[i], rope[i+1])
            tailPositions.add(rope[9])
    print(len(tailPositions))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))