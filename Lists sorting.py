a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
i = 0
b = []
for items in a:
    if a[i]<= 5:
        b.append((a[i]))
        i = i+1
print(b)


