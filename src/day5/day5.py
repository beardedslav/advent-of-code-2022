import argparse
import sys
import time
from collections import deque

def main(args):
    with open('data/day5/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.readlines()
    lineNo = 0
    line = inputFileContents[lineNo]
    numContainers = len(line)//4
    ship = [deque() for _ in range(numContainers)]
    while '[' in line:
        for container in range(numContainers):
            try:
                if (line[container*4+1]) != ' ':
                    ship[container].appendleft(line[container*4+1])
            except:
                pass
        lineNo += 1
        line = inputFileContents[lineNo]
    st = time.process_time()
    lineNo += 2
    line = inputFileContents[lineNo]
    while 'm' in line:
        parsed = [int(inst) for inst in line.replace('move ', '').replace('from ', '').replace('to ', '').split(' ')]
        moving = deque()
        for _ in range(parsed[0]):
            moving.append(ship[parsed[1]-1].pop())
        ship[parsed[2]-1] += moving
        lineNo += 1
        try:
            line = inputFileContents[lineNo]
        except:
            break
    print(''.join(stack.pop() for stack in ship))

    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))