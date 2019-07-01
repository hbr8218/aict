n = input('enter binary number : ')
sum = 0
k = 0
for i in range(len(n)):
    sum = sum + int(n[len(n)-1-i])*(2**k)
    k = k + 1
print (sum)
