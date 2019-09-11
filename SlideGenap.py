#page4
  print ("Welcome to Python!")
  my_variable = 10
  my_int = 7
  my_float = 1.23
  my_bool = True
  # change value
  my_int = 7
  my_int = 3
  print (my_int)


#page6
# single line comment
"""test
multi lines comment
"""
addition = 72 + 23
subtraction = 108 - 204
multiplication = 108 * 0.5
division = 108 / 9
# addition
count_to = 5000 + 6000.6
print (count_to)
# square, exponentiation, to the power of
eggs = 10**2
print (eggs)
# modulo
spam = 5 % 4
print (spam)
# 1, modulo

#page8
meal = 44.50
# 6.75%
tax = 0.0675
# 15%
tip = 0.15
meal = meal + meal * tax
total = meal + meal * tip
print("%.2f" % total)

#page10
caesar = "Graham"
print (caesar)
# Escaping characters
abc = 'This isn\'t flying, this is falling with style!'
print (abc)
"""
The string "PYTHON" has six characters,
numbered 0 to 5, as shown below:
+---+---+---+---+---+---+
| P | Y | T | H | O | N |
+---+---+---+---+---+---+
  0   1   2   3   4   5
So if you wanted "Y", you could just type
"PYTHON"[1] (always start counting from 0!)
"""
fifth_letter = "MONTY"[4]
print (fifth_letter)
# Y


#page12
# to string, printing variables, string concatenation
print ("Spam " + "and " + "eggs")
# error
print ("The value of pi is around " + str(3.14))
string_1 = "Camelot"
string_2 = "place"
print ("Let's not go to %s. 'Tis a silly %s." % (string_1, string_2))
# string formatting
name = "Mike"
print ("Hello %s" % (name))
# string formatting, tanda %s dan %
# fungsi raw_input (input dari keyboard pas runtime)
name = input("What is your name?")
quest = input("What is your quest?")
color = input("What is your favorite color?")
print ("Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color))


#page22
print ("Welcome to the Pig Latin Translator!")
original = input("Enter a word:")
if len(original) > 0 and original.isalpha():
    print (original)
else:
    print ("empty")
    
    
#page26
def square(n):
    squared = n**2
    print ("%d squared is %d." % (n, squared))
    return squared
square(10)
# ---
def power(base, exponent):  # Add your parameters here!
    result = base**exponent
    print ("%d to the power of %d is %d." % (base, exponent, result))
power(37,4)  # Add your arguments here!


#page28
# 1
import math
print (math.sqrt(25))
# 2
from math import sqrt
print (sqrt(25))
from math import *
print (sqrt(25))
# 3
import math            
everything = dir(math) # Sets everything to a list of things from math
print (everything)       # Prints 'em all!
"""
['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']
"""


#page30
