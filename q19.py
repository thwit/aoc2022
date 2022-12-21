import aocd
import helper
import numpy as np

day = 19
data = aocd.get_data(day=day, year=2022)
data = data.split('\n')

def part1(data):
    ores = 1
    clays = 0
    obss = 0
    geos = 0
    
    blueprints = []
    for line in data:
        ore, clay, obs, geo = line[:-1].split('.')
        
        ore = helper.ints(ore)
        clay = helper.ints(clay)
        obs = helper.ints(obs)
        geo = helper.ints(geo)
        
        blueprints.append([ore, clay, obs, geo])
    
    
    quality_sum = 0
    
    for i, bp in enumerate(blueprints, 1):
        
        res = {'ore': 1, 'clay': 0, 'obs': 0, 'geo': 0}
        
        
        
        
        
    
def part2(data):
    pass


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)