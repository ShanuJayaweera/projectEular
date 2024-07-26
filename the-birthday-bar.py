s = [4, 2, 5, 4]
d = 4
m = 1

count = 0
for i in range(len(s) - m + 1):
    if sum(s[i:i + m]) == d:
        count += 1
print(count)
