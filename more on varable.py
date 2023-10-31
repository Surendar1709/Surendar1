print("hello every one")
x=55
print(id(x))
name ='surendar'
print(id(name))
a=10
b=a
print(id(a))
print(id(b))
a=9
print('the addres of a',id(a))
print('the addres of b',id(b))
# we cannot create constant in python use something like highlite for constant variables
h=9.5
i=3
text='ssssss'
print(type(h))
print(type(i))
print(type(text))
# data types in python 
''' 1.NONE 2.NUMERIC 3.LIST 4.TUPLE 4.SET 5.STRING 6.RANGE 7.DICTIONARY'''
'''NONE variabels  not assign with any values'''
''' 2 .NUMARIC  
 int eg x=5
 flot eg x=7.8
 compelx (a+bi) eg 3+4j
 bool'''
m=4
print(type(m))
n=5.3
print(type(n))
# tuype converting  is done by command  variable=datatypename(variable )
m1=float(m)
print(type(m1),'m1 ic converted type of m int to float')
n1=int(n)
print(type(n1),'n1 ic converted type of n  float to int')
# to convet into complex
c=complex(m1,n1)
print('c is ',c,type(c))
#bool true or false
print(m<n)
print(int(True))
print(type(True))
bool=m>n
print(bool)