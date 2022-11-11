# Programmer: Joseph Kasongo
# Program: Python Worksheet-1
# Version: Python 3.8.2
# First written: 09/01/2022, 09:48:00 PM
# # Last changed: 09/09/2022, 12:49:00 PM
print ("Python Lab 1a: The print function, Unicode values")
print ("\n")
print ("Joseph Kasongo")
print ("Lubumbashi")
print (4 * 11 * 29)
print (403 // 12)
print (403 % 12)
favNumber = 11
favMonth = "February"
print (favNumber)
print (favMonth)
print ("\u03a3" + " Greek Capital Letter Sigma")
print ("\u0398" + " Greek Capital Letter Theta")
print ("\u03a1" + " Greek Capital Letter Rho")
print ("\u03a8" + " Greek Capital Letter Psi")
print ("\u0395" + " Greek Capital Letter Epsilon")
print ("\u03dd" + " Greek Small Letter Digamma")
print ("\n")
print ("Python Lab 1b: Binary, Decimal, Hex")
print ("\n")
print (11, 29*4, "Favorite Numbers")
x = 29
print (x, bin(x), hex(x)) 
y = 0b100
z = 0x1D
print("If I change the value of x to a decimal number (for example: 29.429), I get a TypeError that says 'Float object cannot be interpreted as an integer'\n The reason why I get this error is because I am assigning a float value to a function that is expecting an integer value.")
print (y, z)
w = x + y + z
print ("the sum is " , w)
print (11, 29,"four", sep=',')
print (0, 1,'two', sep=' ')
