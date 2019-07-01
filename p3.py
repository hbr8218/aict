
n = int(input("enter a no. of columns: "))
i  = 1
if n%2 == 0:
    while n-2*i != 0: # (n-2*i) is no. of spaces in each rows
        print ('*'*i,' '*(n-2*i),'*'*i)
        i = i+1
else:
    while n-2*i-1 != 0: # (n-2*i) is no. of spaces in each rows
        print ('*'*i,' '*(n-2*i-1),'*'*i)
        i = i+1
