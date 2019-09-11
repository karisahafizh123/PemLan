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

#page14
bool_one = True    # 17 < 328    
bool_two = True    # 100 == (2 * 50)
bool_three = True  # 19 <= 19 
bool_four = False  # -22 >= -18 
bool_five = False  # 99 != (98 + 1)
bool_one = False   # (20 - 10) > 15
bool_two = False   # (10 + 17) == 3**16
bool_three = False # 1**2 <= -1
bool_four = True   # 40 * 4 >= -4
bool_five = False  # 100 != 10**2
# -----
bool_one = 3 < 5     # True
bool_two = 3 > 5     # False
bool_three = 5 == 5  # True
bool_four = 3 != 3   # False
bool_five = 3 <= 3   # True


#page16
