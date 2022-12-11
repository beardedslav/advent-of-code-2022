import argparse
import sys
import time

INSTRUCTION_COST = {'noop' : 1, "addx" : 2}

def main(args):
    with open('data/day10/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    x = 1
    cycle = 0
    instructions = (line for line in inputFileContents.split('\n'))
    currentInstruction = next(instructions)
    operation = currentInstruction[:4]
    lines = []
    for lineNo in range(6):
        line = []
        for pos in range(40):
            if lineNo * 40 + pos >= cycle + INSTRUCTION_COST[operation]:
                cycle += INSTRUCTION_COST[operation]
                if operation == 'addx':
                    x += int(currentInstruction[5:])
                currentInstruction = next(instructions)
                operation = currentInstruction[:4]
            if pos in range(x-1, x+2):
                line.append('#')
            else:
                line.append('.')
        lines.append(line)
    print('\n'.join(''.join(line) for line in lines)) 
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))