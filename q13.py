import aocd
import helper
import numpy as np
import ast
import functools

day = 13
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n\n')

RIGHT = 1
WRONG = -1

def test_ints(a, b):
    if a < b:
        return RIGHT
    elif a == b:
        return None
    elif a > b:
        return WRONG
    
def test_lists(aa, bb):
    maxrange = max(len(aa), len(bb))
    for i in range(maxrange):
        if i >= len(aa) and i < len(bb):
            return RIGHT
        elif i >= len(bb) and i < len(aa):
            return WRONG
            
        a = aa[i]
        b = bb[i]
        
        if isinstance(a, int) and isinstance(b, int):
            res = test_ints(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            res = test_lists(a, b)
        elif isinstance(a, list) and isinstance(b, int):
            res = test_lists(a, [b])
        else: # int and list
            res = test_lists([a], b) 
        
        if res is not None:
            return res    
    
def part1(data):
    ids = []
    pairs = []
    
    for pair in data:
        a, b = pair.split('\n')
        pairs.append([ast.literal_eval(a), ast.literal_eval(b)])
    
    for i, (aa, bb) in enumerate(pairs):
        if test_lists(aa, bb) == RIGHT:
            ids.append(i+1)
    return sum(ids)
    
def part2(data):
    data.append('[[2]]\n[[6]]')
    
    packets = []
    
    for pair in data:
        a, b = pair.split('\n')
        packets.extend([ast.literal_eval(a), ast.literal_eval(b)])
    packets = sorted(packets, key=functools.cmp_to_key(test_lists),reverse=True)
    
    ids = []
    for i, packet in enumerate(packets):
        if packet == [[2]] or packet == [[6]]:
            ids.append(i+1)
            
    return np.prod(ids)

answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)