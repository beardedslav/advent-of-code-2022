import argparse
import sys
import time

INSTRUCTION_COST = {'noop' : 1, "addx" : 2}

def main(args):
    with open('data/day10/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    x = 1
    signalStrength = 0
    cycle = 0
    nextCycle = 20
    for line in inputFileContents.split('\n'):
        instruction = line[:4]
        if cycle + INSTRUCTION_COST[instruction] >= nextCycle:
            signalStrength += x * nextCycle
            nextCycle += 40
        cycle += INSTRUCTION_COST[instruction]
        if instruction == 'addx':
            x += int(line[5:])
    print(signalStrength)    
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))