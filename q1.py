import aocd

data = sorted(list(map(lambda x: sum(list(map(int, x.split()))), aocd.get_data(day=1, year=2022).split('\n\n'))))
print(data[-1], sum(data[-3:]))


#myanswer = abs(x) + abs(y)
#print(myanswer)
#aocd.submit(myanswer, part='B', day=1, year=2022)