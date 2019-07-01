
l = int(input("enter no. of coloums:"))
b = int(input("enter no. or rows:"))
for i in range(b):
    if i == 0 or i==b-1:
        print ('*'*l)
    else:
        print ('*',' '*(l-4),'*')
