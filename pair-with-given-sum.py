arr = [0,-1,2,-3,1]

x = -2

for i in range(len(arr)):
    cal = sum(arr[i:i+2])
    if cal == x:
        print("YES")
