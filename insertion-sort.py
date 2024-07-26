array = [10, 5, 88, 3, 99, 4, 1]

for i in range(1, len(array)):

    while array[i-1] > array[i] and i > 0:
        array[i-1], array[i] = array[i], array[i-1]
        i -= 1
        print(i)
