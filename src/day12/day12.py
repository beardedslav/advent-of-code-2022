import argparse
import sys
import time
import numpy as np

def val(chr):
    if not isinstance(chr, str):
        chr = chr[0] 
    if chr == 'S':
        return ord('a')
    if chr == 'E':
        return ord('z')
    return ord(chr)

def h(start, end):
    return abs(start[0]-end[0]) + abs(start[1]-end[1])

def reconstructPath(cameFrom, current, start):
    totalPath = 0
    while current != start:
        current = cameFrom[current]
        totalPath+=1
    return totalPath

def distance(heightmap, start, end):
    openSet = []
    openSet.append((start[0][0], start[1][0]))

    cameFrom = dict()
    gScore = np.full_like(heightmap, sys.maxsize, int)
    gScore[start] = 0
    fScore = np.full_like(heightmap, sys.maxsize, int)
    fScore[start] = h(start, end)

    while(openSet):
        openSet = list(reversed(sorted(openSet, key = lambda el: fScore[el])))
        current = openSet.pop()
        if current[0] == end[0] and current[1] == end[1]:
            return reconstructPath(cameFrom, current, start)

        candidates = []
        if current[0] - 1 >= 0:
            candidates.append((current[0]-1, current[1]))
        if current[0] + 1 < heightmap.shape[0]:
            candidates.append((current[0]+1, current[1]))
        if current[1] - 1 >= 0:
            candidates.append((current[0], current[1]-1))
        if current[1] + 1 < heightmap.shape[1]:
            candidates.append((current[0], current[1]+1))
        
        for candidate in candidates:
            if val(heightmap[candidate]) == val(heightmap[current]) or val(heightmap[candidate]) == val(heightmap[current])+1 or val(heightmap[candidate]) < val(heightmap[current]):
                tentativeGScore = gScore[current] + 1
                if tentativeGScore < gScore[candidate]:
                    cameFrom[(candidate)] = current
                    gScore[candidate] = tentativeGScore
                    fScore[candidate] = tentativeGScore + h(candidate, end)
                    if candidate not in openSet:
                        openSet.append(candidate)
    
def main(args):
    with open('data/day12/{}'.format(args.inputFileName)) as inputFile:
        inputFileContents = inputFile.read()
    heightmap = np.array([np.array(list(row)) for row in inputFileContents.split('\n')])
    st = time.process_time()
    start = np.nonzero(heightmap == 'S')
    end = np.nonzero(heightmap == 'E')
    print(distance(heightmap, start, end))
    et = time.process_time()
    print('Calc time: {:.6f}s'.format(et-st))
    
    return 0

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'File name')
    parser.add_argument('-f', '--inputFileName', help='Input file name', required=False, default='example.txt')
    args = parser.parse_args()
    sys.exit(main(args))