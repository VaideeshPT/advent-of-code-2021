with open('input.txt') as data:
    data = data.readlines()
    data = [reading.strip() for reading in data]
    length = len(data[0])

def to_int(value):
    result = sum([int(number)*(2**index) for index, number in enumerate(value[::-1])])
    return result

def part1(data):
    gamma_rate = ''
    epsilon_rate = ''

    for index in range(length):
        temp_dict = {'1':0, '0':0}
        for reading in data:
            temp_dict[reading[index]] += 1
        gamma_rate += max(temp_dict, key = temp_dict.get)
        epsilon_rate += min(temp_dict, key = temp_dict.get)
    power_consumption = to_int(gamma_rate) * to_int(epsilon_rate)

    return power_consumption

print(part1(data)) #2003336

def part2(a,b):
    oxygen_rating = ''
    co2_rating = ''
    return a+b

print(part2(10,20))
