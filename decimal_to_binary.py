'''
n = int(input('enter number: '))
arr = []
while n>0:
    r = n%2
    arr.append(r)
    n=n//2
#print ((arr[::-1])
for i in arr[::-1]:
    print(i,end='')
print ('\n')
'''

############## second method ###################3333
n = int(input('enter number: '))
l1 = [0 for i in range(n+1)]
x = 0
while n>0:
    r = n%2
    l1[x] = r
    n = n//2
    x = x+1
y = x-1
while y>= 0:
    print(l1[y],end=',')
    y = y-1
