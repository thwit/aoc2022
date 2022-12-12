import aocd
import helper
import numpy as np
import networkx as nx

day = 12
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')
WIDTH = len(data[0])

def gen_hmap_graph(data):
    heightmap = {
        (x, y): h
            for y, line in enumerate(data)
            for x, h in enumerate(line)
    }

    S = None
    E = None

    for pos, val in heightmap.items():
        if val == 'S':
            S = pos
            heightmap[pos] = 'a'
        if val == 'E':
            E = pos
            heightmap[pos] = 'z'
        if S and E:
            break
            
    G = nx.DiGraph()

    for (x, y), h in heightmap.items():
        dirx = [1, -1, 0, 0]
        diry = [0, 0, 1, -1]
        
        for dx, dy in zip(dirx, diry):
            if ord(heightmap.get((x+dx, y+dy), '#')) <= ord(h) + 1:
                G.add_edge((x, y), (x + dx, y + dy))
    return heightmap, G, S, E


def part1(data):
    _, G, S, E = gen_hmap_graph(data)
    return len(nx.shortest_path(G, S, E)) - 1
        
    
def part2(data):
    hmap, G, _, E = gen_hmap_graph(data)
    dists = []
    poss = [pos for pos, h in hmap.items() if h == 'a' ]
    
    for pos in poss:
        try:
            dists.append(len(nx.shortest_path(G, pos, E)) - 1)
        except:
            continue
    
    return min(dists)


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)