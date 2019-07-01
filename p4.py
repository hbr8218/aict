'''
def f(a):
    if a == 5:
        print ('Hi'* 5)
        print (';')
    elif a == 170:
        print ('Hello'*170)
        print ('*')
    elif a == 55:
        print ('wel'*55)
        print ('#')
    elif a == 17:
        print ('come'*17)
        print ('?')

f(5)
f(170)
f(55)
f(17)
'''
def f1(s):
    print (s[0]*s[1],'\n',s[2])

l = [('Hi',5,';'),('Hello',170,'*'),('wel',55,'#'),('come',17,'?')]
for i in l:
    f1(i)
