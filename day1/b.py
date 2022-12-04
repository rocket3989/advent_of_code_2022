from aocd import get_data
from parse import parse, findall, search

data = get_data(day=1, year=2022)

# first_line = search("{}\n", data)[0]
# parsed = [(tuple(r)) for r in findall("{:d},{:d}", data)]
# ns = [int(x) for x in data.split('\n')]

curr = 0
arr = []
for line in data.split('\n'):
    if line.strip() == '':
        arr.append(curr)
        curr = 0

    else:
        curr += int(line)

arr.sort()

print(sum(arr[-3:]))