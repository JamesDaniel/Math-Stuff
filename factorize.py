
num = 8

print('Factors of %d are:' % (num))
for i in range(1, num):
    if num%i == 0:
        print ('%d x %d' % (i, num//i))
        