import aocd
import helper
import numpy as np
import ast
import functools

day = 13
data = aocd.get_data(day=day, year=2022)
data1 = data.split('\n\n')
data2 = data.split('\n')
    
def compare(a, b):        
    match a, b:
        case int(), int():
            return a - b
        case list(), int():
            return compare(a, [b])
        case int(), list():
            return compare([a], b)
        case list(), list():
            for cmp in map(compare, a, b):
                if cmp != 0:
                    return cmp
            return len(a) - len(b)
            
def part1(data):
    pairs = [[ast.literal_eval(x) for x in pair.split('\n')] for pair in data]
    ids = [i+1 for i,(a,b) in enumerate(pairs) if compare(a,b) < 0 ]
    return np.sum(ids)
    
def part2(data):
    data = filter(lambda x: x, data + ['[[2]]', '[[6]]'])
    packets = sorted([ast.literal_eval(x) for x in data], key=functools.cmp_to_key(compare))
    ids = [i for i, packet in enumerate(packets, 1) if packet in [[[2]], [[6]]]]
    return np.prod(ids)

answer_a = part1(data1)
answer_b = part2(data2)

print(answer_a)
print(answer_b)