import numpy as np

with open('input.txt') as data:
    data = data.readlines()
    data = np.fromstring(data[0], dtype=int, sep = ',')

days = 80

def part1(data):

    for day in days:
        data = np.where(data == -1, 6)


        print(np.where(a < 4, -1, 100))