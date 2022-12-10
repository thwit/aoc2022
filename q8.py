import aocd
import re
import numpy as np
import math
import time

def ints(string):
    return [*map(int, re.findall(r'\d+', string))]

start = time.time()
data = aocd.get_data(day=8, year=2022)
#data = "30373\n25512\n65332\n33549\n35390"
data = data.split('\n')
nrow = len(data)
ncol = len(data[0])

trees = [[int(tree) for tree in d] for d in data]
       
def scenic_score(trees, r, c):
    scores = []
    vis = 0
    minr = trees[r][c]
    for r_ in range(r+1, nrow):
        if trees[r_][c] < minr:
            vis += 1
        else:
            vis += 1
            
            break
            
    scores.append(vis)
    vis = 0
    for r_ in range(r-1, -1, -1):
        if trees[r_][c] < minr:
            vis += 1
        else:
            vis += 1
            break
    scores.append(vis)
    vis = 0      
    for c_ in range(c+1, ncol):
        if trees[r][c_] < minr:
            vis += 1
        else:
            vis += 1
            break
    scores.append(vis)
    vis = 0    
    for c_ in range(c-1, -1, -1):
        if trees[r][c_] < minr:
            vis += 1
        else:
            vis += 1
            break
    scores.append(vis)
    score = math.prod(scores) if r!= 0 and r != nrow -1 and c != 0 and c != ncol - 1 else 0
    #print(r, c, scores, score)
    vis = 0
    return score
    
    
    
def part2(trees):    
    mask = [[-1 for tree in d] for d in trees]
    
    for r in range(nrow):
        for c in range(ncol):
            mask[r][c] = (scenic_score(trees, r, c))
    
    
    return np.amax(mask)
    
def part1(trees):
    trees = np.array(trees)
    mask = np.zeros_like(trees)
    
    for _ in range(4):
        for i in range(len(trees[0])):
            mask[i] = mask[i] | np.array([trees[i, j] > max(trees[i, :j], default=-1) for j in range(len(trees[i]))])
        
        trees = np.rot90(trees)
        mask = np.rot90(mask)
        
    return mask.sum()

myanswer = part1(trees)
print(myanswer)

#aocd.submit(myanswer, part='A', day=9 year=2022)