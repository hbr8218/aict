def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n*fact(n-1)

s = ((fact(1)+fact(5)+fact(10)) + fact(37)+fact(67)+fact(93))
print (s)
