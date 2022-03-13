with open('input.txt') as data:
	data = data.readlines()

data_array = data_array = [int(element.strip()) for element in data]

#part1

result1 = sum(a < b for a,b in zip(data_array, data_array[1:]))
print(result1) #1298

#part2

result2 = sum(a < b for a,b in zip(data_array, data_array[3:]))
print(result2) #1248