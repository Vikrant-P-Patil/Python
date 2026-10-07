#LOOPS#

#WHILE LOOP:
    #repeat the loop until the specified condition is true.

i= 1
while i<= 5 :
    print(i)
    if (i==3):
        break
    i += 1
print("loop ended")

    #the COUNT varialbe = ITERATOR
    #looping process = ITERATION

    #for the loop to stop the condition should be false.

    #BREAK#
    #used to terminate the loop when encountered.

    #CONTINUE# 
    #in the current iteration and contues execution of the loop with the next iteration.

    #basically skips the iterator if the given condition in loop is true.


#FOR LOOP:
    #used for sequntial traversal 
    #for travelling in lists, string, tuple,etc

str = "toronto"
for ch in str:
    if ch == "o" :
        print("o found")
        break
    print(ch)
else:
    print("END")

    #RANGE FUNCTION#
    #range()
    #it returns a sequence of numbers starting from 0 by default and increments by 1(by default) and stops before a specified number.

for el in range(5):
    print(el)

range(10) 
# 10 = stopping valye and is not included

range(1,10)
# 1 = starting valu and it is invlcluded

range(1,10,2)
# 2 = step value, the next number printed will be a step up by 2

    
    #PASS STATEMENT#
    #it is a null statement that does nothing , it is used as a placeholder for future code.
    
for i in range(5):
    pass

