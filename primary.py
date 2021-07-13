# author: <Mya Walker>
# date: <7/8/21>

# -------------------- Section 1 -------------------- #

# Input | Saving String Responses to Variables

# Objectives:
#   1. Name in Reverse
#       a. Prompts input from the user in the form of a first name and last name.
#           Save these values to variables first_name and last_name.
#       b. Print the first and last names in reverse order.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> first name... elia
#   >> last name... deppe
#   deppe, elia
#
# ---- WRITE CODE BELOW ---- #


first_name= (input('Please enter your first name: '))

last_name=(input('Now enter your last name: '))


print(last_name, first_name)



#   2. Pyramid
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> $
#
#   $
#   $$
#   $$$
#   $$
#   $
#
# ---- WRITE CODE BELOW ---- #

print()
print()
print()

sign =input('Can you please enter a symbol? :')
print(sign)
print(sign*2)
print(sign*3)
print(sign*2)
print(sign)

print()
print()
print()



#   3. Parallelogram
#       a. Prompt input from the user in the form of a single character. Save to a variable named symbol.
#       b. Using the symbol, create a pyramid like you see in the example output. (Think, how can you make
#           duplicates of text symbol?)
#
# ----- EXAMPLE OUTPUT ----- #
#   >> @
#
#   @
#   @@
#   @@@
#   @@@@
#    @@@
#     @@
#      @
#
# ---- WRITE CODE BELOW ---- #

symbol =input('Can I get a new symbol? :')

print()
print(symbol)
print(symbol*2)
print(symbol*3)
print(symbol*4)
print('',symbol*3)
print(' ',symbol*2)
print('  ',symbol)
print()
print()
print()

# -------------------- Section 2 -------------------- #

# Casting | Getting Integers and Floats from the User

# Objectives:
#   1. Comparison
#       a. Prompt the user to enter a number, and save it to a variable named num1. DO NOT CAST IT.
#       b. Prompt the user to enter a number, and save it to a variable named num2. CAST IT TO AN INTEGER.
#       c. Prompt the user to enter a number, and save it to a variable named num3. CAST IT TO A FLOAT.
#       d. Print out each variable multiplied by 10.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> num1... 45
#   >> num2... -132.45
#   >> num3... 2132.24
#
#   num1 (str)   | 45454545454545454545
#   num2 (int)   | -1320
#   num3 (float) | 21322.4
#
# ---- WRITE CODE BELOW ---- #

num1 = input('Enter a whole number: ')
num2 = int(input('Enter another whole number: '))
num3 = float(input('Enter another new number it can be a decemal: '))


print()

x= num1*10
print(x)
print('This is the number as a String multiplied by ten.')

print()

x= num2*10
print(x)
print('This is the number as a Integer multiplied by ten.')

print()

x= num3*10
print(x)
print('This is the number as a Float multiplied by ten.')


# Objectives:
#   2. Diameter of a Circle
#       a. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       b. Compute the diameter, and print it to the user.
#           diameter = radius * 2
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 12.3
#
#   diameter = 24.6
#
# ---- WRITE CODE BELOW ---- #

print()
print()
print()


num = float(input('enter a radius: '))
x=num *2
print(x)
print('The new number is the old number turned into a diameter.')



# Objectives:
#   3. Area of a Circle
#       a. Define a function named area_circle(). Accept the parameters listed below.
#           Name   | Type(s)         | Description
#           radius | Integer / Float | The radius of the circle.
#
#           The function should compute the area of a circle, and print it to the terminal.
#               area = 3.14 * radius ** 2
#       b. Prompt input from the user to enter a radius. Save this value to a
#           variable named num as an integer or float.
#       c. Compute the radius by calling the function area_circle(), sending num as a parameter.
#
# ----- EXAMPLE OUTPUT ----- #
#   >> radius... 44.2
#
#   area of the circle: 6134.4296
#
# ---- WRITE CODE BELOW ---- #

print()

rad= float(input('enter a new radius: '))
def area_circle():
    area = 3.14*rad**2
    print(area)
area_circle()
print('This is the area of a circle based on the radius you just entered.')

# -------------------- Section 4 -------------------- #
#
# Create a conversation with a faux (fake) AI, using input and print().
# See the example in example.py

print()


name = input('What\'s your name? ')
print('Hello! ' + name + ', my name is L.T. short for LapTop!')

print('Nice to meet you.')

print()

hobbie = input('What do you like to do on your free time ' + name + '? ')
print()
print('That\'s so cool ' + name + '. I never really had the chance to ' + hobbie + ' much before. But I do like to watch My Hero Academia, and Haikyuu.')
print()

print('Well its been real... But I but I have to go.'
'See you.')
