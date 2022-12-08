import aocd
import re
import numpy as np
import math
import time

def ints(string):
    return [*map(int, re.findall(r'\d+', string))]

start = time.time()
data = aocd.get_data(day=8, year=2022)
data = "30373\n25512\n65332\n33549\n35390"
data = data.split('\n')
nrow = len(data)
ncol = len(data[0])

trees = [[int(tree) for tree in d] for d in data]

def part1(trees):
    vis = 0
    
    
    mask = [[0 for tree in d] for d in trees]

    
    for r in range(nrow):
        minr = -1
        for c in range(ncol):
            if trees[r][c] > minr:
                mask[r][c] += 1
                minr = trees[r][c]
            else:
                break
              
    for r in range(nrow):
        minr = -1
        for c in range(ncol-1, -1, -1):
            if trees[r][c] > minr:
                mask[r][c] += 1
                minr = trees[r][c]
            else:
                break
    
    for c in range(ncol):
        minr = -1
        for r in range(nrow):
            if trees[r][c] > minr:
                mask[r][c] += 1
                minr = trees[r][c]
            else:
                break
              
    for c in range(ncol):
        minr = -1
        for r in range(nrow-1, -1, -1):
            if trees[r][c] > minr:
                mask[r][c] += 1
                minr = trees[r][c]
            else:
                break
                
    for tt in mask:
        # print(tt)
        vis += np.sum(tt)
                
    return vis
       
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
    
def visibility(trees):
    trees = np.array(trees)
    mask = np.ones_like(trees)
    for i in range(len(trees)):
        for j in range(2, len(trees[0])):
            print(max(trees[i, :j]))
    
    for _ in range(4):
        for i in range(len(trees)):
            mask[i] += np.array([1 if trees[i, j] > max(trees[i, :j], default=-1) else 0 for j in range(2, len(trees[i]))])
        np.rot90(trees)
        np.rot90(mask)
        
    return sum(map(sum, mask))
        
            

    
    

myanswer = visibility(trees)

end = time.time()

print(myanswer)

#aocd.submit(myanswer, part='A', day=9 year=2022)