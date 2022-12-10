import aocd
import helper
import numpy as np
import os

day = 9
data = aocd.get_data(day=day, year=2022)
data = data.split('\n')

def intsign(x):
    if x < 0:
        return -1
    if x > 0:
        return 1
    return 0



def part1(data, k=2):
    knots = [(0,0) for _ in range(k)]
    
    visited = set()
    visited.add((0,0))
    
    cmdx = {'U': 0, 'D': 0, 'R': 1, 'L': -1} 
    cmdy = {'U': 1, 'D': -1, 'R': 0, 'L': 0}
    
    for line in data:
        d, n = line.split()
        n = int(n)
        
        while n > 0:
            xh, yh = knots[0]
            xh += cmdx[d]
            yh += cmdy[d]
            
            knots[0] = (xh, yh)
            
            for i in range(1,k):
                xh, yh = knots[i-1]
                xt, yt = knots[i]
                
                xdir = (xh - xt)
                ydir = (yh - yt)
                
                if abs(xdir) > 1 or abs(ydir) > 1:
                    xt += intsign(xdir)
                    yt += intsign(ydir)
                    knots[i] = (xt, yt)
            
            visited.add(knots[-1])
            
            n -= 1
            
    xs = [x for x,_ in visited]
    ys = [y for _,y in visited]
    
    xlen = abs(min(xs)) + abs(max(xs))
    ylen = abs(min(ys)) + abs(max(ys))
    
    
    vmat = [['.'] * xlen] * ylen
    
    ox = abs(min(xs))
    oy = abs(min(xs))
    
    for x,y in visited:
        x_ = x+ox-1
        y_ = y+oy-1
        
        print(x_, y_, xlen, ylen)
        
        vmat[y+oy-1][x+ox-1] = '#'
    
    for v in vmat:
        print(v)
    
    
    
    return len(visited)
        
        
    
def part2(data):
    return part1(data, 11)


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)