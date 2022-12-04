from aocd import get_data
from parse import parse, findall, search

data = get_data(day=4, year=2022)

parsed = [(tuple(r)) for r in findall("{:d}-{:d},{:d}-{:d}", data)]

count = 0
for al, ar, bl, br in parsed:
    l, r = sorted([(al, ar), (bl, br)], key=lambda x: 10000*x[0] - x[1])
    
    if l[1] >= r[0]:
        count += 1

print(count)