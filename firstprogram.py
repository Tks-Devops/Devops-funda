'''print("hello world")
print("tulasi is my name")
print("am from odisha")
print("this is my first programme","hello world")
print(23)
print(23+56)
#variables
name = "tulasi"
age =29
price=25.99 
age2=age
print("name")
print( name )
print("my name is :",name)
print('my age is :',age)
print('my age is :',age2)
#rule of identifiers
print(type(name))
print(type(age))
print(type(price))
#data types
age =23
old = False
a = None
print(type(old))
print(type(a))
#key words (reserved words)
# print sum
a = 2
b = 5
sum =a+b
diff=a-b
print(sum)
print(diff)
""" comment for multiline using 3 comas """
#arithmetic operators
a=8
b=6
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #reminder modulo operator
print(a ** b) #a^b(a to the power) power opertor
#relational / comparison operator
a=50
b=20
print(a==b)#False
print(a!=b)#true (a not equal to b)
print(a>=b)#true
print(a<=b)#false
#assignment operatr
num = 10
num = num +10 #10+10
num+=10
num-=10
num*=10
num/=10
num%=5
num**=10
print("num :", num)
#logical operator
print(not False)
print(not True)
a=50
b=60
print(not(a<b))

val1 = True
val2 = True
print("ans operator:",val1 and val2)# and operator work for both value will true result will true

print("Or operator:" , (a==b) or (a>b))


#type conversion(ex-int value converse to float )
# basically conversion are two type 1.type conversion and type casting
#1.type conversion
a=2
b=4.25
sum = a+b
print (sum)# auto conversion 
# type casting- it is basically in this conversion manually need to perform
a="2"
b=1.25
print(a+b)

a = float("2")
b=4.25
print(a+b)
print(type(a))

a=3.14
a=str(a)

print(type(a))'''
#input function
'''input("where are you from :")
name=input("enter your name:")
print("welcome", name)#input only take as string if we want to print no then use type casting method

name = input("enter name :")
age =input ("enter age :")
marks = float (input("enter marks :"))

print("welcome",name)
print("age=",age)
print("marks=",marks) '''


#write a programme to input 2 number & print their sum
'''a=int(input("type 1st no :"))
b=int(input("type 2nd no :"))

print ("sum of 2 nos :" , a+b)'''

#wap to input side of a square & print its area
'''side = float(input("enter squre side :"))
print ("area :" , side * side)'''
#wap to input 2 floating point numbers & print their average.
'''a=float(input("enter u r 1st no :"))
b=float(input("enter u r 2st no :"))
print("avg :" , a+b/2)'''

#wap to input 2 it numbers , a and b.
#print true if a is greater then or equal to b . if not print false .
''''a= int(input("enter 1st int no : "))
b= int(input("enter 2st int no : "))

print("true/false:",a>=b)'''

#