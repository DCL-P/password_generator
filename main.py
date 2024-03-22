from random import *
from functions import *

number_of_characters = input('select the amount of characters in your password:  ')

try:
    int(number_of_characters)
    print(generate_password(number_of_characters))
except ValueError:
    print('NOPE')

