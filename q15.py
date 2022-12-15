import aocd
import helper
import numpy as np
import time

day = 15
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')

def dist(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
         
class Parallelogram:
    def __init__(self, cx, cy, r):
        self.cx = cx
        self.cy = cy
        self.u = (cx, cy - r)
        self.d = (cx, cy + r)
        self.l = (cx - r, cy)
        self.r = (cx + r, cy)
        self.rad = r    
        
    def area_in_y(self, y):
        
        if y < self.u[1] or y > self.d[1]:
            return set()
            
        E = set()
        for x in range(self.cx - self.rad, self.cx + self.rad):
            if dist(self.cx, self.cy, x, y) <= self.rad:
                E.add((x, y))
            
        return E

         
def part1(data, yy):
    S = dict()
    E = set()
    PG = []
    for line in data:
        s, b = list(map(helper.ints, line.split(':')))
        S[(s[0], s[1])] = b
    
    for (sx, sy), (bx, by) in S.items():
        maxdist = dist(sx, sy, bx, by)
        PG.append(Parallelogram(sx, sy, maxdist))
        pg = PG[-1]
        E = E | pg.area_in_y(yy)
        if by == yy:
            E.remove((bx, by))
    
    return len(E)         
    
def part2(data, ma):
    S = dict()
    for line in data:
        s, b = list(map(helper.ints, line.split(':')))
        S[(s[0], s[1])] = dist(s[0], s[1], b[0], b[1])
        
    for y in range(ma):
        ranges = []
        for (sx, sy), d in S.items():
            if abs(y-sy) > d:
                continue
            
            d_ = d - abs(y-sy)
            
            ranges.append((max(0, sx-d_), min(ma, sx+d_)))
        
        ranges.sort()
        new_ranges = []
        for low, high in ranges:
            if not new_ranges or low > new_ranges[-1][1]:
                new_ranges.append((low, high))
                continue
            
            high = max(high, new_ranges[-1][1])
            low = new_ranges[-1][0]
            new_ranges = new_ranges[:-1]
            new_ranges.append((low, high))
            
        if len(new_ranges) > 1:
            print((new_ranges[0][1]+1) * 4000000 + y)

answer_a = part1(data, 2000000)
answer_b = part2(data, 4000000)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)