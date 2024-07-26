array = [10, 5, 88, 3, 99, 4, 1]

i = 0
while i < len(array)/2:
    temp = array[i]
    array[i] = array[len(array)-1-i]
    array[len(array) - 1 - i] = temp
    i +=1
