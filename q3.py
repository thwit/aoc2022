import aocd
import string
rawdata = aocd.get_data(day=3, year=2022)
data = rawdata.split("\n")
both = list(string.ascii_lowercase) + list(string.ascii_uppercase)

def part1(data):
    return sum([1 + both.index(list(set(d[:len(d)//2]).intersection(set(d[len(d)//2:])))[0]) for d in data])
    
def part2(data):
    return sum([1 + both.index(list(set(data[i]).intersection(set(data[i+1])).intersection(set(data[i+2])))[0]) for i in range(0, len(data), 3)])
    
myanswer = part2(data)
print(myanswer)
aocd.submit(myanswer, part='B', day=3, year=2022)