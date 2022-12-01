import argparse
import sys

def main(args):
    with open('data/day1/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    splitInput = inputFileContents.split('\n')
    maxCalories = 0
    currentCalories = 0
    for food in splitInput:
        if not food:
            if currentCalories > maxCalories:
                maxCalories = currentCalories
            currentCalories = 0
        else:
            currentCalories += int(food)
    print(maxCalories)
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))