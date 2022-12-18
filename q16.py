import aocd
import helper
import numpy as np
import networkx as nx

day = 16
data = aocd.get_data(day=day, year=2022)
data = helper.readfile()
data = data.split('\n')

def flow(G, node, minute):
    return G.nodes[node]['pressure']
    
def flow_potential(G, node, minute):
    return (30 - minute) * G.nodes[node]['pressure']
    

def get_target_node(G, node, minute, shortest_paths):
    max_flow = -1
    max_flow_node = None
    
    for n in G.nodes:
        if n == node:
            continue
        dist = shortest_paths[node][n] + 1
        if minute + dist >= 30:
            continue
            
        if flow_potential(G, n, minute + dist) > max_flow:
            max_flow = flow_potential(G, n, minute + dist)
            max_flow_node = n
    
    return max_flow_node

def get_pressure(G):
    node = 'AA'
    shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
    
    minute = 0
    
    pressures = []
    released = 0
    opens = []
    
    visited = set(node)
    
    G.nodes[node]['flow'] = 0
    
    Q = [node]
    
    while minute <= 30 and len(Q) != 0:
        node = Q.pop(0)
        for e in G[node]:
            target = e
            
            #print(G.nodes, e)
            f = G.nodes[node]['flow'] + flow_potential(G, target, minute + 2)
            if G.nodes[target]['flow'] < f:
                G.nodes[target]['flow'] = f
            
            
            Q.append(target)
             
        
        
            

def part1(data):
    G = nx.DiGraph()
    for line in data:
        namepressure, to = line.split(';')
        pressure = helper.ints(namepressure)[0]
        name = namepressure.split()[1]
        to = to.replace(',', ' ')
        to = to.split()[4:]
        G.add_node(name, pressure=pressure, flow=-100000)
        
        for t in to:
            G.add_edge(name, t)
            
    G_ = nx.DiGraph()
    
    nodespressure = [n for n in G.nodes if G.nodes[n]['pressure'] > 0]
    nodespressure.append('AA')
    
    shortest_paths = dict(nx.all_pairs_shortest_path_length(G))
    
    for n in nodespressure:
        G_.add_node(n, pressure=G.nodes[n]['pressure'], flow=-100000)
        for n_ in nodespressure:
            if n == n_:
                continue
            G_.add_edge(n, n_, weight=shortest_paths[n][n_])
            
    
    
            
     
    return get_pressure(G_)
        
        
        
    
def part2(data):
    pass


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day year=2022)
#aocd.submit(answer_b, part='B', day=day year=2022)