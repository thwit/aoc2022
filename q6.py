import aocd

data = aocd.get_data(day=6, year=2022)

def part1(data, n=4):
    for i in range(len(data)-n):
        if len(set(list(data[i:i+n]))) == n:
            return i+n
    
def part2(data):
    return part1(data, 14)

print(part1(data))
print(part2(data))