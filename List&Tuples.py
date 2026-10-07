#-------------------------------------LIST AND TUPLES--------------------------------------#

#it is a built in data type used to store set of values
marks=[12,13,14,13,87]
print(marks)

print(type(marks))  #type() is  used to give what type of variable is listed

print(marks[0])    #index[] is used to give output of that number, there can also be negative index which are number that start from the right side


print(len(marks))  #len() is used to give the length of the list

#1st element of list starts from 0

#list can store elements of different types together wheather integre or string

#strings are immuatable in python but we can mutate list in python

#LIST SLICING, basically sub list

print(marks[0:3])
#if the starting element is null, it asumes it to be 0

marks.append(4) #adds one element at the end

marks.short() #sorts in ascending order

marks.sort(reverse=True) #sorts in descending order

marks.reverse() #reverse list

marks.insert([]) #insert element at an index

marks.remove(1) #removes 1st occurance of element

marks.pop(2)  #removes element at an index

marks.copy() #it makes a shallow/duplicate copy of the list

#----------------------------------------TUPLES-------------------------------------------#

#A built in data type that lets us create immutable sequence of values

tup = (1,23,34,58) #use comma for single value to specify it is a tuple

tup[0]=2    #we can not do this

print(type(tup))
print(tup(0)) 

#we can also do tuple slicing just like in lists

tup.index(1) #returns index of first occurance 
#kitini baar wo number ka occurance aaya wo define karta hai tup.index()

tup.count(23) #counts the total occurances







