

x = int(input("Enter upper limit : "))
y = int(input("Enter lower limit : "))

for i in range(x,y):
    print(i , end = '  ')
#This is a for loop for print until the range the range is given . Here x is the upper limit and y is the lower limit
#The code will take x as starting period and y as ending like it will print until the y like if y =6 , it will print till 5

# Task 1

#Write a program that prints a countdown from 5 down to 1, and then prints "Blast off!" at the end.

z = 5
for i in range (z , 0 , -1):
    print(i)
print ("Blast off!")

# Task 2

#Ask the user to enter a number using input(). Then, use a for loop and an if statement to print only the even numbers from 1 up to that number.

x = int(input("Enter a limit : "))

for i in range (1 , x+1):
    if i % 2 == 0:
        print(i)

# Task 3

#Create a list of numbers, for example: numbers = [10, 20, 30, 40].
#Write a loop that goes through the list, adds all the numbers together, and prints the final total sum at the very end (it should print 100 for this list).

numbers = [1,2,3,4,5,6,7,8,9]

total = 0
for i in numbers:
    total += i
print(total)

