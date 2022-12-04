from aocd import get_data
from parse import parse, findall, search

data = get_data(day=2, year=2022)

# first_line = search("{}\n", data)[0]
parsed = [(tuple(r)) for r in findall("{:w} {:w}", data)]
# ns = [int(x) for x in data.split('\n')]

outcome = {
    'A': {'X': 3, 'Y': 6, 'Z': 0},
    'B': {'X': 0, 'Y': 3, 'Z': 6},
    'C': {'X': 6, 'Y': 0, 'Z': 3},
}

played = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

score = 0
for other, me in parsed:
    if me == 'X':
        for k, v in outcome[other].items():
            if v == 0:
                me = k

    elif me == 'Y':
        for k, v in outcome[other].items():
            if v == 3:
                me = k

    elif me == 'Z':
        for k, v in outcome[other].items():
            if v == 6:
                me = k

    score += outcome[other][me] + played[me]

print(score)