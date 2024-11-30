# Devops-funda

This is my 1st repo of Devops
#list in python

# marks1 = 94.4

# marks2 = 87.5

# marks3 = 95.2

# marks4 = 66.4

# marks5 = 45.1

marks = [94.4,87.5,95.2,66.4,45.1]#this is example of list
print(marks)#[94.4, 87.5, 95.2, 66.4, 45.1]
print(type(marks)) #<class 'list'>
print(marks[0])#index concept #94.4
print(marks[1])#87.5

# student = ["karan" , 95.4, 17,"odisha"]

# print(student)

#"strings" are immutable(can't change) in python and
str = "hello"
print(str[0])
str[0]="y"#TypeError: 'str' object does not support item assignment
#"lists" are mutable(change) in python

student = ["karan", 95.4, 17, "odisha"]
print(student[0]) # This will print "karan"
student[0] = "arjun" # Correct syntax to modify the first element
print(student) # This will print the updated list
print(len(student))#4

student = ["karan", 95.4, 17, "odisha"]
print(student[5])#IndexError: list index out of range

marks=[85,96,76,63,48]
print(marks[ 1 : 4 ])#[96, 76, 63]
print(marks[ 1 : len(marks) ])#[96, 76, 63, 48]
print(marks[1:])##[96, 76, 63, 48]
print(marks[-3:-1])#negetive index slicing[76,63]

# list methods

# list = [2,1,3]

# list.append(4) #list.append -adds one element at the end

# print(list)

# print(list.sort())#none

# list.sort()

    # sort() sorts the list in place (modifies the original list) and returns None.
    # So, when you print list.sort(), it outputs None.

#print(list.append(4))#none

#list.append(4)

    # append() also modifies the list in place by adding an element to the end, and it returns None.
    # When you print list.append(4), it outputs None because append() doesn't return the list.

list=[1,3,5]
print(list.sort(reverse=True))
print(list)#[5, 3, 1]

list = ["banana" ,"litchi" , "apple"]
print(list.sort())#None #['apple', 'banana', 'litchi']
print(list)

list=['a','b','c','d','e']
list.reverse()
print(list)#['e', 'd', 'c', 'b', 'a']

list = [2,1,3]
list.insert(1,5)
print(list)#[2, 5, 1, 3]

list = [2,1,3,1]
list.remove(1)#[2, 3, 1]
#list.pop(3)#[2, 1, 3]
print(list)

#tuples in python(immutable sequences of values)
tup = (87,64,33,95,76)
print(tup[0])#87
print(tup[1])#64
tup[0] = 5#'tuple' object does not support item assignment(immuatable)
print(type(tup))

tup = () # we can create empty tupple
print(tup)#()
print(type(tup))#<class 'tuple'>

tup = (1) # if we want print single value then we need to add value+comma need to add
print(tup)#(1)
print(type(tup))#<class 'int'>

tup = (1,) # if we want print single value then we need to add value+comma need to add
print(tup)#(1,)
print(type(tup))#<class 'tuple'>

# for no need add comma in multiple line

tup = (1,2,3,4) # if we want print single value then we need to add value+comma need to add
print(tup)#(1, 2, 3, 4)
print(type(tup))#<class 'tuple'>

tup = (1,2,3,4)
print(tup[1:3])#(2, 3)

#tupple methods
tup = (2,1,3,1)
print(tup.index(1))#1(returns index of first occurrence)
print(tup.count(1))#2(counts total occurrences)

#let's practice
#wap to ask the user to enter names of their 3 favorite movies & store them in a list
films = ["rocky" , "harry-porter" , "narnia" ]
print(films)
print(type(films))

movies = []
mov1 = input("enter 1st movies: ")
mov2 = input("enter 2nd movies: ")
mov3 = input("enter 3rd movies: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(list(movies))
print(movies)

# #enter 1st movies: narnia

# enter 2nd movies: rocky

# enter 3rd movies: harry-porter

# ['narnia', 'rocky', 'harry-porter']

movies = []
movies.append(input("enter 1st movies: "))
movies.append(input("enter 2nd movies: "))
movies.append(input("enter 3rd movies: "))
print(movies)

#wap to check if a list contains a palindrome of elements.(hint:use copy()method)
list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
print("palindrome")
else:
print("not palindrome")
#------------------------------------------------------
x=[1,2,3,2,1]
copy_x=x.copy()
copy_x.reverse()
if(copy_x==x):
print("palindrome")
else:
print("not palindroma")
#---------------------------------------------
y = [1, "abc", "abc", 1]
copy_y = y.copy()

# Reverse and then print the reversed list

copy_y.reverse()
print(copy_y) # This will print the reversed `copy_y`

# Reassign a fresh copy of `y` to `copy_y` and print it

copy_y = y.copy()
print(copy_y) # This will print `copy_y` as it was originally

if(copy_y==y):
print("palindrome")
else:
print("not palindroma")

#---------------------------------------------------  
#wap to count the number of students with the "a " grade in the following tuple.
grade = ("c","d","a","a","a","b","b","a")
print(grade.count("a"))#4

#store the above values in a list & sort them from "a" to "d"

grade = ["c","d","a","a","a","b","b","a"]
grade.sort()#sort is used for uniformally given the result
print(grade)#['a', 'a', 'a', 'a', 'b', 'b', 'c', 'd']
