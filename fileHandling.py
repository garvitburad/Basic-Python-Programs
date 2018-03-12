handle = open('E:/test.txt')

count = 0
for line in handle:
    print line
    count += 1
count = str(count)
print 'line count =', count
