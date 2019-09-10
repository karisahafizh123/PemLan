#page5
# first
"""
def spam():
eggs = 12
return eggs
print spam()
"""
# second
def spam():
  eggs = 12
  return eggs
print(spam())
##########


#page7
# comment
monty = True
python = 1.234
monty_python = python ** 2
##########


#page11
parrot = "Norwegian Blue"
print(len(parrot))
#14

# String methods: len(), lower(), upper(), str()

parrot = "Norwegian Blue"
print(parrot.lower()) 
print(parrot.upper())

# to string
pi=3.14
print(str(pi))

# review
ministry = "The Ministry of Silly Walks"
print(len(ministry))
print(ministry.upper())
##########


#page13
from datetime import datetime
now = datetime.now()
print(now)

# member, bukan method
print(now.year)
print(now.month)
print(now.day)

print('%s-%s-%s' % (now.year, now.month, now.day))
print('%s/%s/%s' % (now.day, now.month, now.year))

print(now.hour)
print(now.minute)
print(now.second)

print('%s:%s:%s' % (now.hour, now.minute, now.second))
print('%s/%s/%s %s:%s:%s' % (now.day, now.month, now.year,now.hour, now.minute, now.second))
##########


#page15
# raw_input
def clinic():
    print("You've just entered the clinic!")
    print("Do you take the door on the left or the right?")
    answer = input("Type left or right and hit 'Enter'.").lower()
    if ((answer == "left") or (answer == "l")):
        print("This is the Verbal Abuse Room, you heap of parrot droppings!")
    elif ((answer == "right") or (answer == "r")):
        print("Of course this is the Argument Room, I've told you that already!")
    else:
        print("You didn't pick left or right! Try again.")
        clinic()
        
clinic()
##########


#page17
bool_one   = False and False
bool_two   = -(-(-(-2))) == -2 and 4 >= 16**0.5
bool_three = 19 % 4 != 300 / 10 / 10 and False
bool_four  = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2
bool_five  = True and True

# -----
bool_one   = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'
bool_two   = True or False
bool_three = 100**0.5 >= 50 or False
bool_four  = True or True
bool_five  = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1
##########


#page19
answer = "Left"
if answer == "Left":
    print("This is the Verbal Abuse Room, you heap of parrot droppings!")

# Will the above print statement print to the console?

# ---
def using_control_once():
    if True:
        return "Success #1"
    
def using_control_again():
    if True:
        return "Success #2"
    
print(using_control_once())
print(using_control_again())
##########


#page21
# condition
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
    
print(greater_less_equal_5(4))
print(greater_less_equal_5(5))
print(greater_less_equal_5(6))

# review
def the_flying_circus():
    if 5 == 5:    # Start coding here!
        # Don't forget to indent
        # the code inside this block!
        return True
    elif True and True :
        # Keep going here.
        # You'll want to add the else statement, too!
        return False
    else :
        return False
##########


#page23
pyg = 'ay'
original = input('Enter a word:')
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)] 
    print(new_word)
else:
    print('empty')
##########


#page25
def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08
    print("With tax: %f" % bill)
    return bill

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15
    print("With tip: %f" % bill)
    return bill

meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)
##########


#page27
# Functions call functions
def one_good_turn(n):
    return n + 1

def deserves_another(n):
    return one_good_turn(n) + 2

# ---

def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING!"
    else:
        return "Can you speak up?"
    
shout("I'M INTERESTED IN SHOUTING")

# ---
def cube(number):
    return number**3

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False
##########


#page29
def biggest_number(*args):
    print(max(args))
    return(max(args))

def smallest_number(*args):
    print(min(args))
    return(min(args))

def distance_from_zero(arg):
    print(abs(arg))
    return(abs(arg))

biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)
# ---
maximum = max(2.3,4.1,6)
minimum = min(2.3,4.1,6)
absolute = abs(-42)

print(maximum)
##########


#page31
def is_numeric(num):
    return ((type(num) == int) or (type(num) == float))
    
# ---
def distance_from_zero(a):
    if ((type(a) == int) or (type(a) == float)):
        return abs(a)
    else:
        return "Nope"
##########


#page35
suitcase = []
suitcase.append("sunglasses")

# Your code here!
suitcase.append('a')
suitcase.append('b')
suitcase.append('c')

list_length = len(suitcase) # Set this to the length of suitcase

print("There are %d items in the suitcase." % (list_length))
print(suitcase)

"""
There are 4 items in the suitcase.
['sunglasses', 'a', 'b', 'c']
"""
##########


#page37
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")   # Use index() to find "duck"

# Your code here!
animals.insert(duck_index,"cobra")

print(animals) # Observe what prints after the insert operation
# ['aardvark', 'badger', 'cobra', 'duck', 'emu', 'fennec fox']
##########


#page39
# dictionary key value notasi object {}
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print(residents['Puffin']) # Prints Puffin's room number
# Your code here!
print(residents['Sloth'])
print(residents['Burmese Python'])
##########


#page41
# key - animal_name : value - location 
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
                'Sloth' : 'Rainforest Exhibit',
                'Bengal Tiger' : 'Jungle House',
                'Atlantic Puffin' : 'Arctic Exhibit',
                'Rockhopper Penguin' : 'Arctic Exhibit'}

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin']='Arctic Exhibit Mod'

print(zoo_animals)
##########


#page43
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for item in names: print(item)
# ---
# indent first element dalam dict dalam {}, spt di bhs lain
webster = {
     "Aardvark" : "A star of a popular children's cartoon show.",
     "Baa" : "The sound a goat makes.",
     "Carpet": "Goes on the floor.",
     "Dab": "A small amount."
}
for key in webster:
    print(webster[key])
##########


#page45
for letter in "Codecademy": print(letter)
# Empty lines to make the output pretty
print()
print()

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i": print(letter)
##########


#page47
# take 2
prices = {
    "banana" : 4,   "apple"  : 2,
    "orange" : 1.5, "pear"   : 3,
}
stock = {
    "banana" : 6,   "apple"  : 0,
    "orange" : 32,  "pear"   : 15,
}

for key in prices:
    print(key)
    print("price: %s" % prices[key])
    print("stock: %s" % stock[key])
    
total = 0
for key in prices:
     print(prices[key]*stock[key])
     total += prices[key]*stock[key]
print(total)
##########


#page49
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0]
}

students = [lloyd,alice,tyler]
for student in students:
    print(student['name'])
    print(student['homework'])
    print(student['quizzes'])
    print(student['tests'])
##########


#page51
lloyd = { "name": "Lloyd", "homework": [90.0, 97.0, 75.0, 92.0],
          "quizzes": [88.0, 40.0, 94.0], "tests": [75.0, 90.0] }
alice = { "name": "Alice", "homework": [100.0, 92.0, 98.0, 100.0],
          "quizzes": [82.0, 83.0, 91.0], "tests": [89.0, 97.0] }
tyler = { "name": "Tyler", "homework": [0.0, 87.0, 75.0, 22.0],
          "quizzes": [0.0, 75.0, 78.0], "tests": [100.0, 100.0] }
# ---
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total/len(numbers)
def get_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return 0.1*homework + 0.3*quizzes + 0.6*tests
def get_letter_grade(score):
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >=60: return "D"
    else: return "F"
def get_class_average(students):
    results = []
    for student in students: results.append(get_average(student))
    return average(results)
##########


#page55
# 1
n = "Hello"
def string_function(s):
    return s+' world'

print(string_function(n))

# 2
def list_function(x):
    x[1]+=3
    return x

n = [3, 5, 7]
print(list_function(n))

# 3
n = [3, 5, 7]

def list_extender(lst):
    lst.append(9);
    return lst

print(list_extender(n))
##########


#page57
range(6) # => [0,1,2,3,4,5]
range(1,6) # => [1,2,3,4,5]
range(1,6,3) # => [1,4]
# range(stop)
# range(start, stop)
# range(start, stop, step)

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

y = []
for i in range(3):
        y.append(i)

print(my_function(y)) # [0, 1, 2]
# [0, 2, 4]
##########


#page59
# 3 operator + agak beda di python buat list
m = [1, 2, 3]
n = [4, 5, 6]

def join_lists(x,y): return x + y

print(join_lists(m, n))
# [1, 2, 3, 4, 5, 6]

# 4 List of Lists
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results=[]
    for numbers in lists:
        for num in numbers: results.append(num)
    return results

print(flatten(n))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
##########


#page61
# .join method uses the string to combine the items in the list.
from random import randint

board = []
for x in range(5): board.append(["O"] * 5)

def print_board(board):
    for row in board: print(" ".join(row))

print("Let's play Battleship!")
print_board(board)

# ---
def random_row(board): return randint(0, len(board) - 1)
def random_col(board): return randint(0, len(board[0]) - 1)
ship_row = random_row(board)
ship_col = random_col(board)
#print ship_row
#print ship_col
##########


#page65
# ---
# 4 
choice = input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  
    choice = input("Sorry, I didn't catch that. Enter again: ")
# ---
# 5 break
count = 0

while True:
    print(count)
    count += 1
    if count >= 10:
        break
# ---
##########


#page67
# 7
from random import randint
# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
guesses_left = 3
while guesses_left > 0:
    guess = int(input("Your guess: "))
    if (guess == random_number):
        print('You win!')
        break
    guesses_left -=1
else:
    print('You lose.')
##########


#page69
# 3
phrase = "A bird in the hand..."
for char in phrase:
    if ((char == "A") or (char =="a")):
        print("X")
    else:
        print(char)
print
# The , character after our print statement means that 
# our next print statement keeps printing on the same line. 
# plus 1 space
# ---
# 4 Looping over a dictionary
d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}
for key in d:
    print(key + " " + d[key])
##########


#page71
# 7 
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']
print('You have...')
for f in fruits:
    if f == 'tomato':
        print('A tomato is not a fruit!') # (It actually is.)
        break
    print('A', f)
else:
    print('A fine selection of fruits!')
# spt else while, kl break tidak dirun, kl exit normal yes
# ---
##########


#page73
# 1
def is_even(x):
    if x % 2 == 0 : return True
    else: return False
# ---

# 2        
def is_int(x):
    delta = x - int(x)
    if delta == 0.0: return True
    else: return False
    
print(is_int(7.0))
print(is_int(7.9))
print(is_int(-1.2))
##########


#page75
# 5
def is_prime(x):
    if x < 2 : return False
    for n in range(x-2):
        if x % (n+2) == 0: return False
    return True
print(is_prime(9))
print(is_prime(11))
# ---
# 6
def reverse(text):
    varlength = len(text)
    textrev = ""
    for i in range(varlength): textrev += text[varlength-1-i]
    return textrev
print(reverse('abc@def'))
# You may not use reversed or [::-1] to help you with this.
# ---
##########


#page77
# 8
def censor(text,word):
    textlist = text.split()
    textlist_new = []
    for item in textlist:
        if item != word:
            textlist_new.append(item)
        else:
            textlist_new.append("*" * len(item))
    return " ".join(textlist_new)
print(censor("this hack is wack hack", "hack"))
# ---
# 9
def count(sequence,item):
    varcount = 0
    for i in sequence:
        if i == item: varcount += 1
    return varcount
print(count([1,2,1,1], 1))
##########


#page79
# 12
def remove_duplicates(varlist):
    newlist = []
    for var in varlist:
        if var not in newlist: newlist.append(var)
    return newlist
print(remove_duplicates([1,1,2,2]))
# ---
# 13 sorted()
# The median is the middle number in a sorted sequence of numbers. If you are given a sequence with 
# an even number of elements, you must average the two elements surrounding the middle.
# sorted([5, 2, 3, 1, 4]) --> [1, 2, 3, 4, 5]
def median(varlist):
    sortedlist = sorted(varlist)
    length = len(varlist)
    if length % 2 == 1:
        return sortedlist[int((length+1) / 2 - 1) ]
    else:
        return (sortedlist[int(length/2 - 1)] + sortedlist[int(length/2)])/2.0

print(median([1,1,2]))   # 1
print(median([7,3,1,4])) # 3.5
##########


#page80
grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
def print_grades(grades):
    for grade in grades: print(grade)
def grades_sum(scores):
    total = 0
    for score in scores: total += score
    return total
def grades_average(grades):
    return grades_sum(grades)/float(len(grades))
print_grades(grades)
print(grades_sum(grades))
print(grades_average(grades))
##########


#page81
def grades_average(grades):
    sum_of_grades = grades_sum(grades)
    average = sum_of_grades / float(len(grades))
    return average

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    variance /= float(len(scores))
    return variance

def grades_std_deviation(variance): return variance ** 0.5

variance = grades_variance(grades)

print(print_grades(grades))
print(grades_sum(grades))
print(grades_average(grades))
print(grades_variance(grades))
print(grades_std_deviation(variance))
##########


#page83
my_dict = {
    "Name": "Otong",
    "Age": 23,
    "Title": "Dr"
}
print(my_dict.items())  # [('Age', 23), ('Name', 'Otong'), ('Title', 'Dr')]
print(my_dict.keys())   # ['Age', 'Name', 'Title']
print(my_dict.values()) # [23, 'Otong', 'Dr']
for key in my_dict: print(key, my_dict[key])
# Age 23
# Name Otong
# Title Dr
# You should use print a, b rather than print a + " " + b
##########


#page85
# 4
c = ['C' for x in range(5) if x < 3]
print(c) # ['C', 'C', 'C']

# ---------------------------------------------------------
# 5
cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4 == 0]
print(cubes_by_four) # [8, 64, 216, 512, 1000]

# ---------------------------------------------------------
# 6
l = [i ** 2 for i in range(1, 11)]  # Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l[2:9:2]) # [9, 25, 49, 81] -- 2 belakang, 1 diloncat

# list slicing
# [start:end:stride]
# Where start describes where the slice starts (inclusive), end is where it ends (exclusive), 
# and stride describes the space between items in the sliced list. For example, a stride of 2 
# would select every other item from the original list to place in the sliced list.
# start & end --> index
##########


#page87
# 9
letters = ['A', 'B', 'C', 'D', 'E']
print(letters[::-1]) #['E', 'D', 'C', 'B', 'A'] right to left
# ---------------------------------------------------------
# 10
my_list = range(1, 11)

backwards = my_list[::-1]

# ---------------------------------------------------------
# 11
to_one_hundred = range(101)

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens) #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

# ---------------------------------------------------------
# 12
to_21 = range(1,22)

odds = to_21[::2]
middle_third = to_21[7:14]
##########


#page88
# ekivalen
lambda x: x % 3 == 0
def by_three(x): return x % 3 == 0
# ---------------------------------------------------------
# filter
my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))
# yg bs di bagi 3 -> [0, 3, 6, 9, 12, 15]
# ---------------------------------------------------------
##########


#page89

languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(filter(lambda x: x=="Python", languages)) # ['Python']
# ---------------------------------------------------------
cubes = [x**3 for x in range(1, 11)]
print(filter(lambda x: x % 3 == 0, cubes))
# ---------------------------------------------------------
squares = [x**2 for x in range(1,11)]
print(filter(lambda x: x > 30 and x <=70, squares)) # [36, 49, 64]
# ---------------------------------------------------------
##########


#page91
# List Slicing
str = "ABCDEFGHIJ"
# str[start:end:stride] -> start, end, stride = 1, 6, 2
# ---------------------------------------------------------
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
rev_garbled = garbled[::-1]
message = rev_garbled[::2]
print(message)
# ---------------------------------------------------------
# Lambda
my_list = range(16)
print(filter(lambda x: x % 3 == 0, my_list))
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != 'X',garbled)
print(message)
##########


#page93
one = 0b1; two = 0b10; three = 0b11; four = 0b100; five = 0b101; six = 0b110; 
seven = 0b111; eight = 0b1000; nine = 0b1001; ten = 0b1010; eleven = 0b1011; twelve = 0b1100
print(eight)
# ---------------------------------------------------------
print(bin(1)) #0b1
print(bin(2)) #0b10
print(bin(3)) #0b11
print(bin(4)) #0b100
print(bin(5)) #0b101
# ---------------------------------------------------------
print(int("1",2))     # 1
print(int("10",2))    # 2
print(int("111",2))   # 7
print(int("0b100",2)) # 4
print(int(bin(5),2))  # 5
# print(out the decimal equivalent of the binary 11001001.
print(int("0b11001001",2)) # 201
# base 2 semua, pakei 0b atau gak, sama
##########


#page95
# mask
def check_bit4(input): # input reserved?
    mask = 0b1000
    desired = input & mask
    if desired > 0: return "on"
    else: return "off"
# ---------------------------------------------------------
a = 0b10111011
mask = 0b100
print(bin(a | mask)) # 0b10111111
print(bin(a ^ mask)) # 0b10111111
# ---------------------------------------------------------
a = 0b11101110
mask = 0b11111111   #flip *semua* bit a
print(bin(a ^ mask)) # 0b10001 
# ---------------------------------------------------------
def flip_bit(number,n):
    mask = (0b1 << (n-1))
    result = number ^ mask
    return bin(result)
#xor kalau mask 1 nge-flip; kalo mask 0 tetap
##########


#page97
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous
    def description(self):
        print("I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor))
    def is_edible(self):
        if not self.poisonous: print("Yep! I'm edible.")
        else: print("Don't eat me! I am super poisonous.")
# ---------------------------------------------------------
lemon = Fruit("lemon", "yellow", "sour", False)
lemon.description()
lemon.is_edible()
##########


#page99
class Animal(object):
    """Makes cute animals."""
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry
# Note that self is only used in the __init__() function *definition*; 
# we don't need to pass it to our instance objects.
zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)
print(zebra.name, zebra.age, zebra.is_hungry)        # Jeffrey 2 True
print(giraffe.name, giraffe.age, giraffe.is_hungry)  # Bruce 1 False
print(panda.name, panda.age, panda.is_hungry)        # Chad 7 True
##########


#page101
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print(zebra.name, zebra.age, zebra.is_alive)        #Jeffrey 2 True
print(giraffe.name, giraffe.age, giraffe.is_alive)  #Bruce 1 True
print(panda.name, panda.age, panda.is_alive)        #Chad 7 True
#is_alive member variable; name,age instance variables
##########


#page103
class Animal(object):
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(self):
        print(self.name)
        print(self.age)
hippo = Animal("Nil",5)
hippo.description()
sloth = Animal("slothName", 6)
ocelot = Animal("ocelotName",7)
print(hippo.health)  # good
print(sloth.health)  # good
print(ocelot.health) # good
#member variable = class variable (bukan instance, available to all inst)
##########


#page104
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name
    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart.")
    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")
##########


#page105
my_cart1 = ShoppingCart("Otong")
my_cart2 = ShoppingCart("Udjang")

my_cart1.add_item("Obeng",2000)  # Obeng added.
my_cart1.add_item("Obeng",1000)  # Obeng is already in the cart.
print(my_cart1.items_in_cart)    # {'Obeng': 2000} 

my_cart2.add_item("Sapu",2000)  # Sapu added.
my_cart2.add_item("Sapu",1000)  # Sapu is already in the cart.
print(my_cart2.items_in_cart)    # {'Obeng': 2000, 'Sapu': 2000} 

my_cart1.add_item("Sapu",5000)  # Sapu is already in the cart.
print(my_cart1.items_in_cart)    # {'Obeng': 2000, 'Sapu': 2000}

my_cart2.items_in_cart = {'Buku': 3000}
print(my_cart2.items_in_cart)    # {'Buku': 3000}
print(my_cart1.items_in_cart)    # {'Obeng': 2000, 'Sapu': 2000}

my_cart2.add_item("Sapu",1000)  # Sapu added.
print(my_cart2.items_in_cart)    # {'Sapu': 1000, 'Buku': 3000}

my_cart1.add_item("Dodol",10000) # Dodol added.
print(my_cart1.items_in_cart)     # {'Obeng': 2000, 'Sapu': 2000, 'Dodol': 10000}
print(my_cart2.items_in_cart)     # {'Sapu': 1000, 'Buku': 3000}
##########


#page107
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id
    def display_cart(self):
        print("I'm a string that stands in for the contents of your shopping cart!")
class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print("I'm a string that stands in for your order history!")
monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()           # Customer.display_cart
monty_python.display_order_history()  # ReturningCustomer
##########


#page109
class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print("Hello, %s" % other.name)
class CEO(Employee):
    def greet(self, other):
        print("Get back to work, %s!" % other.name)
ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo) # Hello, Emily
ceo.greet(emp) # Get back to work, Steve!
##########


#page111
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00
class PartTimeEmployee(Employee):
    def calculate_wage(self,hours):
        self.hours = hours
        return hours * 12.00
    def full_time_wage(self,hours):
        return super(PartTimeEmployee,self).calculate_wage(hours)
milton = PartTimeEmployee("Milton")
print(milton.full_time_wage(10))
##########


#page112
class Triangle(object):
    number_of_sides = 3
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
    def check_angles(self):
        sum_angle = self.angle1 + self.angle2 + self.angle3
        if sum_angle == 180: return True
        else: return False
class Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle1 = self.angle
        self.angle2 = self.angle
        self.angle3 = self.angle
my_triangle = Triangle(90,30,60)
print(my_triangle.number_of_sides) # 3 inherited
print(my_triangle.check_angles())  # True
##########


#page113
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model; self.color = color; self.mpg = mpg
    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)
    def drive_car(self): self.condition = "used"

class ElectricCar(Car):
    def __init__(self,model,color,mpg,battery_type):
        super(ElectricCar,self).__init__(model,color,mpg)
        self.battery_type = battery_type
    def drive_car(self): self.condition="like new"
        
my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")

print(my_car.condition) # new 
my_car.drive_car()     # 
print(my_car.condition) # like new

my_car1 = Car("DeLorean", "silver", 88)
print(my_car1.condition)      # new
print(my_car1.model)          # DeLorean    
print(my_car1.display_car())  # This is a silver DeLorean with 88 MPG.

my_car1.drive_car()
print(my_car1.condition)      # used
##########


#page117
my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

for i in my_list: my_file.write(str(i) + "\n")
    
my_file.close()

# "r+" as a second argument to the function so the 
# file will allow you to read and write
##########


#page119
# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file = open("text.txt", "w")

# Write to the file
write_file.write("Not closing files is VERY BAD.")
write_file.close()

# Try to read from the file
print(read_file.read())
read_file.close()
##########




