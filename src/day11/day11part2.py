import argparse
import sys
import math
import time

def main(args):
    with open('data/day11/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    monkeys = []
    currentMonkey = None
    for line in inputFileContents.split('\n'):
        if line.startswith('Monkey'):
            currentMonkey = dict()
            currentMonkey['inspections'] = 0
        else:
            line = line.strip()
            if not line:
                monkeys.append(currentMonkey)
            elif line.startswith('Starting items: '):
                currentMonkey['items'] = [int(item) for item in line.split('Starting items: ')[1].split(', ') ]
            elif line.startswith('Operation: '):
                currentMonkey['operation'] = eval('lambda old: '+ line.split('new = ')[1])
            elif line.startswith('Test: '):
                currentMonkey['divisible'] = int(line.split('Test: divisible by ')[1])
            elif line.startswith('If true: throw to monkey'):
                currentMonkey['if_true'] = int(line.split('If true: throw to monkey ')[1])
            elif line.startswith('If false: throw to monkey'):
                currentMonkey['if_false'] = int(line.split('If false: throw to monkey ')[1])
    monkeys.append(currentMonkey)
    worryMod = math.prod(monkey['divisible'] for monkey in monkeys)
    st = time.process_time()
    for _ in range(10000):
        for monkey in monkeys:
            for item in monkey['items']:
                worry = item
                worry = monkey['operation'](worry)
                worry %= worryMod
                throwTo = monkey['if_true'] if worry % monkey['divisible'] == 0 else monkey['if_false']
                monkeys[throwTo]['items'].append(worry)
                monkey['inspections'] += 1
            monkey['items'] = []
    bestMonkeys = sorted(monkey['inspections'] for monkey in monkeys)[-2:]
    print([monkey['inspections'] for monkey in monkeys])
    print(bestMonkeys[0] * bestMonkeys[1])
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))