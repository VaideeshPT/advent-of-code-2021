with open('input.txt') as data:
    data = data.readlines()
    data = [reading.strip().split() for reading in data]
    data = [(reading[0], int(reading[1])) for reading in data]

horizontal = 0

def part1(data):
    depth = 0
    global horizontal
    for command, value in data:
        if command == 'forward':
            horizontal += value
        elif command == 'down':
            depth += value
        else:
            depth -= value
    return horizontal * depth

print(part1(data)) #1893605

def part2(data):
    depth, aim = 0, 0
    global horizontal
    for command, value in data:
        if command == 'down':
            aim += value
        elif command == 'up':
            aim -= value
        else:
            depth += aim * value

    return horizontal * depth

print(part2(data)) #2120734350