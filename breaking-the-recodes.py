arr = [10,5,20,20,4,5,2,25,1]

minimum = arr[0]
maximum = arr[0]

max = 0
min = 0
for i in range(1, len(arr)):

    if maximum < arr[i]:
        maximum = arr[i]
        max += 1

    if minimum > arr[i]:
        minimum = arr[i]
        min += 1
print(min)


