"""
Erin Seepersad 1/30/2023 CSCI-UA - 006
Assignment #1 Problem #3
"""

print("4380000 tons of waste is the same as...")
print()


# variables
apple1= 0.17
car1= 1.5
chargingbull=7000
statueoflib=27156
empirestate=365000

#units
ton= 2000
kilo=2.20462
original=4380000

apple2= apple1*kilo
original2=original*ton

#commpute the code conversions
print("Apples:",          (original2/apple2))
print("Cars:",            (original/car1))
print("Charging Bulls:",  (original2/chargingbull))
print("Statue of Liberties:",(original/statueoflib))
print("Empire State Buildings:",(original/empirestate))

