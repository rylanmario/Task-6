#Name: Task 6.py
#Author: Rylan Fessey
#Date created: October 30th, 2022
#Date modified: November 2nd, 2022
#Purpose: This program will take a number and tell the user if it is prime or not.

# Credit: Andre for helping with some debugging



#The import math allows you to do extra math functions
import math


#Function will remain true when numbers are prime and will be false when they are not prime.
def isPrime(x: int) -> bool:
    limit = math.ceil(math.sqrt(x)) + 1

    if x == 1:
        return False
    if x == 2:
        return True
    if (x % 2) == 0:
        return False

    for i in range(3, limit, 2):
        if (x % i) == 0:
            return False

    return True

#This function will format the output for the prime and non prime numbers.
def outputList(prefix: str, items: list) -> None:
    length = len(items)
    print(prefix, end="")
    for i in range(length - 1):
        print(str(items[i]), end=",")

    if length != 0:
        print(str(items[length - 1]))


#This asks the user to print the numbers and make sure they dvide them with a comma.
typednumbers = input("Enter your numbers, followed by a comma:").split(',')
numberselection = []
for i in typednumbers:
    numberselection += [int(i)]

#This sorts the numbers so it looks cleaner
numberselection.sort()

primenumbers = []
nonPrimenumbers = []

#This sorts the numbers into lists.
for i in numberselection:
    if (isPrime(i)):
        primenumbers += [i]
    else:
        nonPrimenumbers += [i]

#Tells the user what numbers are prime and what aren't.
outputList("The numbers that are prime are: ", primenumbers)
outputList("the numbers that are not prime are: ", nonPrimenumbers)