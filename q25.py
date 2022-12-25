import aocd
import helper
import numpy as np

day = 25
data = aocd.get_data(day=day, year=2022)
#data = helper.readfile()
data = data.split('\n')

def decimal_to_SNAFU(n):

    s = ''
    mapp = '012=-'
    while n > 0:
        n_ = n % 5
        
        if n_ == 0:
            s = '0' + s
        elif n_ == 1:
            s = '1' + s
        elif n_ == 2:
            s = '2' + s
        elif n_ == 3:
            s = '=' + s
            n += 2
        elif n_ == 4:
            s = '-' + s
            n += 1
        
        n //= 5
    return s
        

def SNAFU_to_decimal(snafu):
    s = reversed(list(snafu))
    num = 0
    exp = 0
    
    for c in s:
        if c == '2':
            num += 2 * 5 ** exp
        elif c == '1':
            num += 1 * 5 ** exp
        elif c == '-':
            num += -1 * 5 ** exp
        elif c == '=':
            num += -2 * 5 ** exp
        
        exp += 1
        
    return num
    
    

def part1(data):
    summ = 0
    for line in data:
        summ += SNAFU_to_decimal(line)
        #print(decimal_to_SNAFU(int(line)))
    return decimal_to_SNAFU(summ)
    
def part2(data):
    pass


answer_a = part1(data)
answer_b = part2(data)

print(answer_a)
print(answer_b)


#aocd.submit(answer_a, part='A', day=day, year=2022)
#aocd.submit(answer_b, part='B', day=day, year=2022)