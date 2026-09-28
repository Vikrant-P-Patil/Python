#Use for loop and range to print numbers from 1 to 10

for i in range(1,11):
    print(i)

#Use range to print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)

#Use range to print all even numbers from 1 to 20
for i in range(0, 20, 2):
    print(i)

#Use range to print all odd numbers from 1 to 20
for i in range(1, 20, 2):
    print(i)

#Take a number from the user a and using a for loop print its multiplication table
number=int(input("Enter a number to get its multiplication table :"))
for i in range(1,11):
    print(number*i)

#Use range to calculate the sum of numbers from 1 to 50
total = 0

for i in range(1,51):
    total=total+i
    
print(total)

#Print all elements of the following list using for loop
cities=["nashik","pune","mumbai","nagpur"]
for city in cities:
    print(city)

#Print the name of each student using a for loop
students=['Rahul','Amit','Priya','Sneha','Rohan']
for student in students:
    print(student)

#Print each number in the following list using loop
numbers = [112,7,18,23,490,89]
for number in numbers:
    print(number)

#Use for loop to print only even numbers in the following list
digits= [112,7,8,23,490,89]
for digit in digits:
    if digit%2 == 0:
        print(digit)

#Use a for loop to print rach subject with the text 'I am Studying'
subjects=['Math','English','Hindi','Physics']
for subject in subjects:
    print("I am Studying "+ subject)





