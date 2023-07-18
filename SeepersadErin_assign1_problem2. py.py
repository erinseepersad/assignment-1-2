"""
Erin Seepersad 1/30/2023 CSCI-UA - 006
Assignment #1 Problem #2
"""
#variable inputs
name1=input("Please enter a name: ")
name2= input("Please enter another name: ")
name3= input("Please enter one more name: ")

print("Here are your names in every possible order:")
print("---------------------------------------------")


#number 1
print("1. ", end="")
print(name1, name2, name3, sep=",")

#number 2
print()
print("2. ", end="")
print(name1, name3, name2, sep=" <> ")

#number 3
print()
print("3. ", end="")
print(name2, name1, name3, sep=" and ", end="!")
print()

#number 4
print()
print("4.", end=" %")
print(name2,"% %" ,name3, "% %", name1,"%", sep="")
print()

# numbers 5
print("5. ",name3)
print(name2)
print(name1)
# number 6
print()
print("6. ",name3, sep="*")
print("   ",name1, sep="*")
print("   ",name2, sep="*")

