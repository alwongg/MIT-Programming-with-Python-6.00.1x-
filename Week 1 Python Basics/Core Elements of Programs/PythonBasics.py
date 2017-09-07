# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Write a piece of Python code that prints out the string 'hello world' 
if the value of an integer variable, happy, is strictly greater than 2.
"""

if happy > 2:
    print("hello world")
    
    
"""
Assume that two variables, varA and varB, are assigned values, either numbers or strings.

Write a piece of Python code that evaluates varA and varB, and then prints out one of the following messages:

"string involved" if either varA or varB are strings

"bigger" if varA is larger than varB

"equal" if varA is equal to varB

"smaller" if varA is smaller than varB
"""

if type(varA) == str or type(varB) == str:
    print("string involved")
    
elif varA > varB:
    print("bigger")
     
elif varA == varB:
    print("equal")
    
elif varA < varB:
    print("smaller")

"""   
Below are some short Python programs. For each program, answer the associated question.

Try to answer the questions without running the code. Check your answers, then run the code for the ones you get wrong.

This question is going to ask you what some simple loops print out. If you're asked what code like this prints:

num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
write what it prints out, separating what appears on a new line by a comma and a space. So the answer for the above code would be:

5, 4

If a given loop will not terminate, write the phrase 'infinite loop' (no quotes) in the box. Recall that you can stop an infinite loop in your program by typing CTRL+c in the console.

Note: What does +=, -=, *=, /= stand for?
"""

# 1.

num = 0
while num <= 5:
    print(num)
    num += 1

print("Outside of loop")
print(num) 

# answer = 0, 1, 2, 3, 4, 5, Outside of loop, 6

# 2

numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))

# answer = infinite loop

# 3

num = 10
while num > 3:
    num -= 1
    print(num) 

# answer = 9, 8, 7, 6, 5, 4, 3

# 4

num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')
# Note: If the command break is executed within a loop, it halts evaluation of the loop at that point and passes control to the next expression. Test some break statements inside different loops if you don't understand this concept!

# answer = 10, 9, 8, 7, Breaking out of loop, Outside of loop

# 5

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

# answer = infinite loop

