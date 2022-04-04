import numpy as np

data = np.genfromtxt('input_6.txt', dtype=int, encoding=None, delimiter=",")

days = 80

def part1(data):

    for day in range(days):
        data = data - 1
        append_condition = np.sum(data < 0)
        data = np.where(data < 0, 6, data)
        
        if append_condition:
            data = np.hstack([data, 8 * np.ones(append_condition)])

    return len(data)


print(part1(data)) #362740