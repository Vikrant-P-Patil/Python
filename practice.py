#WHILE LOOP QUESTIONS#

#print number from 1 tp 100

# i= 1
# while i <=100:
#     print(i)
#     i +=1

#print numbers from 100 to 1

# i=100
# while i >=1: (stopping action)
#     print(i)
#     i -=1 

#print multiplication table of a numebr "n"

# n= int(input("Enter a number : "))
# i = 1
# while i <= 10:
#     print(n*i)
#     i += 1

#print elements of following list using loop

# list = [1,2,3,4,54,54,52,34,342]
# i = 0
# while i < len(list):
#     print(list[i])
#     i += 1

#search for number x in this tuple using loop

# tuple = (1,2,23,54,78,9756,423)
# x= 78
# i=0
# while i < len(tuple):
#     if tuple[i] == x:
#         print("FOUND at index" , i)
#         break
#     else:
#         print("Finding..")
#     i += 1

#continue example

# i=0
# while i<=5:
#     if (i==3):
#         i += 1
#         continue 
#         #here the 3 iterator does not print
#     print(i)
#     i+=1

#FOR LOOP QUESTIONS#

#print the elements of the following list using loop

# nums=[1,32,4,5,3,23,4324,42]
# for num in nums :
#     print(num)

#search for a number x in this tuple using loop

# idx=0
# x=324
# numbers=[1,32,5,6,76554,324,64,21,432]
# for n in numbers:
#     if x == n :
#         print("FOUND AT" ,idx)
#         break
#     idx += 1

#write a program to find the sum of first n numbers (using WHILE)

n=5
sum=0
i=1
while i <=n:
    sum+=i
    i +=1

print(sum)

#write a program to find factorial of first n natural numbers(using FOR)


n=5
factorial=1
i=1
while i <=n:
    factorial*=i
    i +=1

print(factorial)



