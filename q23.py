import aocd
import helper
import numpy as np

day = 23
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')

def get_pos(p, direction):
    return (p[0] + direction[0], p[1] + direction[1])

def part1(data):
    elves = set()
    for row, line in enumerate(data):
        for col, c in enumerate(line):
            if c == '#':
                elves.add((row, col))
    
    NSWEALL = set([(1,0), (1, -1), (1,1), (-1,0), (-1, -1), (-1,1), (0,-1), (-1, -1), (1,-1), (0,1), (-1, 1), (1,1)])
    N = (-1, 0)
    S = (1, 0)
    W = (0,-1)
    E = (0, 1)
    
    NSWEPAIRS = [
    [(-1, 0), (-1, 1), (-1, -1)],
    [(1, 0), (1, 1), (1, -1)],
    [(0, -1), (1, -1), (-1, -1)],
    [(0, 1), (1, 1), (-1, 1)],
]

    NSWE = [N, S, W, E]
    
    i = 0
    new_elves = dict()
    
    for k in range(1, 10000000):
        if k % 100 == 0:
            print(k, len(new_elves), len(elves))
        new_elves = dict()
        for e in elves:
            nbs = [get_pos(e, d) for d in NSWEALL]
            
            if all([nb not in elves for nb in nbs]):
                continue
                
            nbs = [get_pos(e, d) for d in NSWEPAIRS[i % 4]]
            
            if all([nb not in elves for nb in nbs]):
                new_elves[e] = get_pos(e, NSWE[i % 4])
                continue
                
            nbs = [get_pos(e, d) for d in NSWEPAIRS[(i+1) % 4]]
            
            if all([nb not in elves for nb in nbs]):
                new_elves[e] = get_pos(e, NSWE[(i+1) % 4])
                continue
                
            nbs = [get_pos(e, d) for d in NSWEPAIRS[(i+2) % 4]]
            
            if all([nb not in elves for nb in nbs]):
                new_elves[e] = get_pos(e, NSWE[(i+2) % 4])
                continue
                
            nbs = [get_pos(e, d) for d in NSWEPAIRS[(i+3) % 4]]
            
            if all([nb not in elves for nb in nbs]):
                new_elves[e] = get_pos(e, NSWE[(i+3) % 4])
                continue
        
        new_pos = [p for p in new_elves.values()]
        
        if len(new_elves) == 0:
            print(k)
            break
        
        for p, new_p in new_elves.items():
            if new_pos.count(new_p) == 1:
                elves.remove(p)
                elves.add(new_p)
        
        
        i += 1
            
    minx = min([p[1] for p in elves])
    miny = min([p[0] for p in elves])
    maxx = max([p[1] for p in elves])
    maxy = max([p[0] for p in elves])
    
    #print(elves)
    
    for x in range(minx, maxx+1):
        for y in range(miny, maxy+1):
            if (y, x) in elves:
                print('#', end='')
            else:
                print('   ', end='')
        print()
    
    return (maxx-minx+1) * (maxy-miny+1) - len(elves)
            
    
    
    
def part2(data):
    pass


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)