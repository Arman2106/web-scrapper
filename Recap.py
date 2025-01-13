print("Hello World")    #Hello World
print() #prints a blank line
#this is a comment  #comments are used to explain the code and are not executed by the compiler

'''MULTILINE COMMENT    #this is a multiline comment
MULTILINE COMMENT'''

#Variables
x = 5   #int    #int values are written without a decimal point
y = "Hello" #string #string values are written in single or double quotes
z = 5.0 #float  #float values are written with a decimal point
a = True #boolean   #True and False are case sensitive
b = False #boolean
c = 4 + 5j #complex number

print()

print(x)    #5  #int values are written without a decimal point
print(y)    #Hello  #string values are written in single or double quotes    
print(z)    #5.0    #float values are written with a decimal point
print(a)    #True   #boolean values are case sensitive
print(b)    #False  #boolean values are case sensitive
print(c)    #(4+5j) #complex numbers are written in the form of a+bj    #a is the real part and b is the imaginary part

print()

#To check the type of a variable
print(type(x))  #<class 'int'>
print(type(y))  #<class 'str'>
print(type(z))  #<class 'float'>
print(type(a))  #<class 'bool'>
print(type(b))  #<class 'bool'>
print(type(c))  #<class 'complex'>

print()

#Type Conversion/casting
x = float(x)    #int to float
z = int(z)  #float to int
print(x)    #5.0
print(z)    #5

print()

#Strings_functions
x = "Hello World"   #string
print(x)    #Hello World
print(x[0]) #H  #indexing
print(x[2:5]) #llo  #slicing
print(x[2:]) #llo World #slicing
print(x[:5]) #Hello   #slicing
print(x[-5:-2]) #Wor    #negative indexing starts from the end of the string
print(len(x)) #11   #length of the string
print(x.lower()) #hello world   #upper() and lower() are case sensitive
print(x.upper()) #HELLO WORLD   #upper() and lower() are case sensitive
print(x.strip()) #Hello World  #removes any whitespace from the beginning or the end
print(x.replace("H", "J")) #Jello World  #replaces a string with another string
print(x.split(" ")) #['Hello', 'World']  #splits the string into substrings if it finds instances of the separator  
print(x.split("o")) #['Hell', ' W', 'rld']  #splits the string into substrings if it finds instances of the separator
print("Hello" in x) #True  #checks if a certain phrase or character is present in a string
print("Hello" not in x) #False    #checks if a certain phrase or character is not present in a string
print("Hello" + "World") #HelloWorld  #concatenation
print("Hello", "World") #Hello World  #concatenation

print()

#String Formatting
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))  #My name is John, and I am 36
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item number {} for {} rupees."  #{} are placeholders for the variables
print(myorder.format(quantity, itemno, price))   #I want 3 pieces of item number 567 for 49.95 dollars.

print()

#Operators
x = 5
y = 3
print(x + y)    #8 #addition
print(x - y)    #2 #subtraction
print(x * y)    #15    #multiplication
print(x / y)    #1.6666666666666667   #division
print(x % y)    #2 #modulus #returns the remainder of the division
print(x ** y)   #125   #exponentiation
print(x // y)   #1 #floor division #returns the quotient without the remainder

print()

#Comparison Operators
print(x == y)   #False   
print(x != y)   #True    
print(x > y)    #True   
print(x < y)    #False
print(x >= y)   #True   
print(x <= y)   #False

print()

#Logical Operators
print(x > 3 and x < 10) #True    #returns True if both statements are true
print(x > 3 or x < 4)   #True    #returns True if one of the statements is true
print(not(x > 3 and x < 10))    #False   #reverse the result, returns False if the result is true

print()

#Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)   #True    #returns True because z is the same object as x
print(x is y)   #False   #returns False because x is not the same object as y, even if they have the same content
print(x == y)   #True    #to demonstrate the difference between "is" and "==": this comparison returns True because x is equal to y
print(x is not y) #True    #returns True because x is not the same object as y
print(x is not z) #False   #returns False because x is the same object as z
g = None    #None is a special constant in Python that represents the absence of a value or a null value
print(g is None)    #True    #returns True because g is None
print(g is not None)    #False   #returns False because g is None

print()

#Membership Operators
x = ["apple", "banana"]
print("banana" in x)    #True    #returns True because a sequence with the value "banana" is in the list
print("orange" not in x) #True    #returns True because a sequence with the value "pineapple" is not in the list

print()

#Bitwise Operators
x = 10  
y = 4   
print(x & y)    #AND
print(x | y)    #OR
print(x ^ y)    #XOR
print(~x)       #NOT
print(x << 2)   #Zero fill left shift   #this two example is for binary shift 
print(x >> 2)   #Signed right shift

print()

#operator precedence
x = 5
y = 10
z = 15
print(x + y * z)    #155  #multiplication has a higher precedence than addition
print((x + y) * z)  #225  #use parentheses to force the order of operations

print()

#Conditional Statements
a = 33
b = 200
if b > a:
    print("b is greater than a")    #b is greater than a
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

print()

#Short Hand If
if a > b: print("a is greater than b")

print()

#Short Hand If-Else
print("A") if a > b else print("B")    

print()

#Multiple Conditions
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")  #Both conditions are True    

print()

#Nested If
x = 41
if x > 10:
    print("Above ten")
if x > 20:
        print("and also above 20!") #Above ten, and also above 20!

print()

#nested if-else
x = 35
if x > 10:
    print("Above ten")
if x > 20:
    print("and also above 20!") #Above ten, and also above 20!
elif x > 30:
    print("and also above 30")  #Above ten, and also above 20 , and thirty
else:
    print("but not above 40")   #Above ten, and also above 20 , and thirty but not above 40
    
print()

#Loops

#For Loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)    #apple, banana, cherry

print()

#Looping Through a String
for x in "banana":
    print(x)    #b, a, n, a, n, a
    
print()

#Break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break   #apple, banana

print()

#Continue Statement

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue    #apple, cherry
    print(x)

print()

#Range Function
for x in range(6):
    print(x)    #0, 1, 2, 3, 4, 5
    
print()

for x in range(2, 6):
    print(x)    #2, 3, 4, 5
    
print()

for x in range(2, 30, 3):
    print(x)    #2, 5, 8, 11, 14, 17, 20, 23, 26, 29
    
print()

#Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished!")
    
print()

#Nested Loops
num_1 = 4 , 5 , 6 
num_2 = 7 , 8 , 9
for x in num_1:
    for y in num_2:
        print(x, y) #4 7, 4 8, 4 9, 5 7, 5 8, 5 9, 6 7, 6 8, 6 9

print()

#Pass Statement
for x in [0, 1, 2]:
    pass    #having an empty loop like this, would raise an error without the pass statement

print()

#While Loop
i = 1
while i < 6:
    print(i)
    i += 1 #1, 2, 3, 4, 5

print()

#Break Statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break   #1, 2, 3
    i += 1

print()

#Continue Statement
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue    #1, 2, 4, 5, 6
    print(i)
    
print()

#Else in While Loop
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")    #1, 2, 3, 4, 5, i is no longer less than 6
    
print()

#Functions
def my_function():
    print("Hello from a function") #Hello from a function

my_function()

print()

#Arguments
def my_function(fname):
    print(fname + "Rungta")
    
my_function("R1") #R1Rungta
my_function("R2") #R2Rungta

print()