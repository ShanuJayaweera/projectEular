array = [10, 5, 88, 3, 99, 4, 1]

for n in range(len(array) - 1, 0, -1):
    for i in range(n):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
print(array)