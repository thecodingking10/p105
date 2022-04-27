import csv
import math

with open("data.csv", newline="") as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[0]

def mean(data):
    total = 0
    total_entries = len(data)

    for x in data:
        total += int(x)

    mean = total / total_entries

    return mean

squared_list = []

for n in data:
    a = int(n) - mean(data)
    a = a ** 2

    squared_list.append(a)

sum = 0

for i in squared_list:
    sum += i

result = sum / (len(data) - 1)

standard_deviation = math.sqrt(result)
print("Standard Deviation is --> " + str(standard_deviation))