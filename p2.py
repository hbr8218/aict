if __name__  ==  '__main__':
    n = int(input("enter no. of rows: "))
    for i in range(1,n+1):
        print (' '*(n-i),'*'*(2*i-1))
'''
r = 2
c = 3
m = [[0 for i in range(c)] for j in range(r)]
for i in range(r):
    for j in range(c):
        m[i][j] = int(input())
for i in range(r):
    for j in range(c):
        print (m[i][j],end=' ')
    print('\n')
'''
