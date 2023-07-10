#Ingredient Adjuster
"""
Erin Seepersad  2/09/23	CSCI-UA 2 - 006
Assignment #2 Problem #1

"""
#what is the original recipe
original= int(input("How many cookies does this recipe make? "))
ogsugar= float(input("How many cups of sugar does it need? "))
ogflour= float(input("How many cups of flour does it need? "))
ogbutter= float(input("How many cups of butter does it need? "))
print()
#adjusted cookie
newcookie=int(input("How many cookies do you want to make? "))
print()
#printing
print("   Original Recipe   ")
print("--------------------------")
print("* Makes", original, "cookies")
print("*", ogsugar, "cups of sugar")
print("*", ogflour, "cups of floour")
print("*", ogbutter, "cups of butter")
print()
print("    Adjusted Recipe    ")
print("-----------------------------")
print("* Makes", newcookie, "cookies")
#new conversions
newformula= newcookie/original
newsugar= ogsugar*newformula
newflour= ogflour*newformula
newbutter= ogbutter*newformula
#printing new recipe
print("*",format(newsugar, ".1f"), "cups of sugar")
print("*", format(newflour, ".1f"), "cups of flour")
print("*", format(newbutter, ".1f"), "cups of butter")

