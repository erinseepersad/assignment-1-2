#Place Value Madness
"""
Erin Seepersad  2/09/23	CSCI-UA 2 - 006
Assignment #2 Problem #3

"""
num1=int(input("Number #1: "))
num2=int(input("Number #2: "))

print()
#isolate the digits
newnum1= num1//100
newnum2= num1//10%10
newnum3= num1%10
total= newnum1 + newnum2 + newnum3

print("Add all the digits in Number #1: ")

print(newnum1 ,"+", newnum2, "+", newnum3, "=", total)
new2num1= num2//100
new2num2= num2//10%10
new2num3= num2%10
total= new2num1 + new2num2 + new2num3

print("Add all the digits in Number #2: ")

print(new2num1 ,"+" ,new2num2 ,"+", new2num3 , "=", total)
