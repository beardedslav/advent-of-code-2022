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
    score = []
    x, y = len(grid), len(grid[0])
    for _ in range(x):
        score.append([1] * y)
    for x_ in range(x):
        for y_ in range(y):
            score_ = 0
            for x__ in range(x_-1, -1, -1):
                score_+=1
                if grid[x__,y_] >= grid[x_,y_]:
                    break
            score[x_][y_] *= score_
            score_ = 0
            for x__ in range(x_+1, x):
                score_+=1
                if grid[x__,y_] >= grid[x_,y_]:
                    break
            score[x_][y_] *= score_
            score_ = 0
            for y__ in range(y_-1, -1, -1):
                score_+=1
                if grid[x_,y__] >= grid[x_,y_]:
                    break
            score[x_][y_] *= score_
            score_ = 0
            for y__ in range(y_+1, y):
                score_+=1
                if grid[x_,y__] >= grid[x_,y_]:
                    break
            score[x_][y_] *= score_
    print(max(max(row) for row in score))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))