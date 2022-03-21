with open('input.txt') as data:
	data = data.readlines()
	
data_array = [int(element.strip()) for element in data]

def part1(data_array):
    result = sum(a < b for a, b in zip(data_array, data_array[1:]))
    return result

print(part1(data_array)) #1298

def part2(data_array):
    result = sum(a < b for a, b in zip(data_array, data_array[3:]))
    return result

print(part2(data_array)) #1248
