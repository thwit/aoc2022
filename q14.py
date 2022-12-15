import aocd
import helper
import numpy as np
import os

day = 14
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')

def tick(grid, x, y):
    #print()
    #print('new tick!')
    while True:
        if grid[y][x]:
            grid[y][x] = 1
            raise Exception('yeet')
        if not grid[y+1][x]:
            
           # print('down')
            y+=1
            continue
        elif not grid[y+1][x-1]:
            #print('left')
            y+=1
            x-=1
            continue
        elif not grid[y+1][x+1]:
           # print('right')
            y+=1
            x+=1
            continue
        #print('settle', x, y)
        grid[y][x] = 1
        break
        
    return grid

def part1(data):
    lines = []
    
    for line in data:
        points = line.split(' -> ')
        lines.append([[int(xy.split(',')[0]), int(xy.split(',')[1])] for xy in points])
        
    minx = 100000
    miny = 100000
    maxx = -100000
    maxy = -100000
    
    for line in lines:
        for x,y in line:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j][0] -= minx
            
    
    grid = [[0 for _ in range(maxx-minx+1)] for _ in range(maxy+1)]


    for line in lines:
        for i in range(1, len(line)):
            frm = line[i-1]
            to = line[i]
            if frm[0] == to[0]: # same x-value
                x = frm[0]
                frmy = min(frm[1], to[1])
                toy = max(frm[1], to[1])
                for y in range(frmy, toy+1):
                    #print(x, y)
                    grid[y][x] = 1
            elif frm[1] == to[1]: # same y-value
                y = frm[1]
                frmx = min(frm[0], to[0])
                tox = max(frm[0], to[0])
                for x in range(frmx, tox+1):
                    grid[y][x] = 1
    
    #for g in grid:
     #   print(g)
    seedx = 500 - minx
    seedy = 0
    i = 0
    while True:
        try:
            grid = tick(grid, seedx, seedy)
            i += 1
            #print(np.sum(grid))
        except:
            break
    return i
            
    
    
            
    
def part2(data):
    lines = []
    
    for line in data:
        points = line.split(' -> ')
        lines.append([[int(xy.split(',')[0]), int(xy.split(',')[1])] for xy in points])
        
    minx = 100000
    miny = 100000
    maxx = -100000
    maxy = -100000
    
    xlength = 400000
    
    for line in lines:
        for x,y in line:
            minx = min(minx, x)
            miny = min(miny, y)
            maxx = max(maxx, x)
            maxy = max(maxy, y)
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            lines[i][j][0] -= minx + xlength//2
            
    
    
    
    grid = [[0 for _ in range(xlength)] for _ in range(maxy+1)]
    grid.append([0 for _ in range(xlength)])
    grid.append([1 for _ in range(xlength)])
    


    for line in lines:
        for i in range(1, len(line)):
            frm = line[i-1]
            to = line[i]
            if frm[0] == to[0]: # same x-value
                x = frm[0]
                frmy = min(frm[1], to[1])
                toy = max(frm[1], to[1])
                for y in range(frmy, toy+1):
                    #print(x, y)
                    grid[y][x] = 1
            elif frm[1] == to[1]: # same y-value
                y = frm[1]
                frmx = min(frm[0], to[0])
                tox = max(frm[0], to[0])
                for x in range(frmx, tox+1):
                    grid[y][x] = 1
    
    for g in grid:
        break
        print(g)
        
    seedx = 500 - minx + xlength//2
    seedy = 0
    i = 0
    while True:
        try:
            grid = tick(grid, seedx, seedy)
            i += 1
            #print(np.sum(grid))
        except:
            break
    print()
    for g in grid:
        break
        print(g)

    return i
            
    


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)