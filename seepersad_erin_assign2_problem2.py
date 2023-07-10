#Tip Calculator
"""
Erin Seepersad  2/09/23	CSCI-UA 2 - 006
Assignment #2 Problem #2

"""
"""
print("****Tip Calculator****')
      #syntax error- missing the correct delimiter at the end ('') or ("")

# ask user for input
bill = float(input("How much was your bill? "))
tipP = float(input("How much do you want to tip? (Ex: 18) "))
people = input("How many people are splitting the bill? (Minimum is 1) ")
#runtime- mentioned in line 25
print()

# calculate tip, total, and amount per person
percent = (tipp/100)
#runtime error- ran at first but stopped running because tipp is not defined only tipP
tip = bill / percent
#logic- you are supposed to multiply
total = bill + tip
pp = total/people
#runtime error- because people above is currently a string and not a float  

# display results
print(tipP + "% tip is $" + format(total, '.2f')
#runtime error- it is supposed to be commas since python cannot add a float and str
#parentheses not closed- syntax error
#logic- you need tip in the parentheses not total
print("The total amount is $" + format(tip, '.2f'))
#logic error- you need total in ther parenthese not tip
print("Each person will pay $" + format(pp, '.2s'))
#runtime- '.2s' is supposed to be '.2f'
      """
#Correct Code
print("****Tip Calculator****")
bill= float(input("how much was your bill? "))
tipP = float(input("how much do you want to tip? (ex:18) "))
people = float(input("How many people are splitting the bill? (Minimum is 1) "))
print()
percent = (tipP/100)
tip = bill* percent
total = bill + tip
pp = total / people
print(tipP,"% tip is $", format(tip, '.2f'))
print("The total amount is $" + format(total, '.2f'))
print("Each person will pay $" + format(pp, '.2f'))
