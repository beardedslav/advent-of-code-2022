import argparse
import sys
import time
import numpy as np

def main(args):
    with open('data/day8/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    st = time.process_time()
    grid = inputFileContents.split('\n')
    grid = np.array([[int(c) for c in row] for row in grid])
    visible = []
    x, y = len(grid), len(grid[0])
    for _ in range(x):
        visible.append([1] * y)
    for x_ in range(x):
        for y_ in range(y):
            if x_ in (0, x-1) or y_ in (0, y-1):
                continue
            else:
                visible[x_][y_] = int(any(all( height < grid[x_][y_] for height in section ) for section in [grid[0:x_,y_], grid[x_+1:x,y_], grid[x_,0:y_], grid[x_,y_+1:y]]))
    print(sum(sum(row) for row in visible))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))