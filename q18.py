import aocd
import helper
import numpy as np
from collections import deque

day = 18
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')         

def part1(data):
    cubes = set()
    for xyz in data:
        x, y, z = helper.ints(xyz)
        cubes.add((x, y, z))
        
    neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    
    tot_area = len(cubes) * 6
    
    for x, y, z in cubes:
        shared = 0
        for d in neighbors:
            if (x+d[0], y+d[1], z+d[2]) in cubes:
                tot_area -= 1
    
    return tot_area
    
def neighbours(p):
    nbs = []
    
    
    neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    for d in neighbors:
        nbs.append((p[0]+d[0], p[1]+d[1], p[2]+d[2]))

    return nbs
    
def bfs(p, cubes, rx, ry, rz):
    counter = 0
    
    q = deque()
    q.append(p)
    
    water = set()
    
    neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    
    while q:
        p = q.popleft()
        
        if p in water:
            continue
        
        water.add(p)
        
        nbs = neighbours(p)
        
        for nb in nbs:
            if nb not in cubes and nb[0] in rx and nb[1] in ry and nb[2] in rz:
                q.append(nb)
    
    return water
    
    
def part2(data):
    cubes = set()
    for xyz in data:
        x, y, z = helper.ints(xyz)
        cubes.add((x, y, z))
        
    neighbors = [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    
    minx = min([c[0] for c in cubes])-1
    miny = min([c[1] for c in cubes])-1
    minz = min([c[2] for c in cubes])-1
    
    
    rangex = range(min([c[0] for c in cubes])-1, max([c[0] for c in cubes])+2)
    rangey = range(min([c[1] for c in cubes])-1, max([c[1] for c in cubes])+2)
    rangez = range(min([c[2] for c in cubes])-1, max([c[2] for c in cubes])+2)
    
    
    
    water = bfs((minx, miny, minz), cubes, rangex, rangey, rangez)
    
    air = 0
    
    for x in rangex:
        for y in rangey:
            for z in rangez:
                if (x, y, z) not in water:
                    cubes.add((x, y, z))  


    tot_area = len(cubes) * 6
    
    for x, y, z in cubes:
        shared = 0
        for d in neighbors:
            if (x+d[0], y+d[1], z+d[2]) in cubes:
                tot_area -= 1                    
                    
    return tot_area


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)