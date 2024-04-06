from random import *
from functions import *

while True:
    number_of_characters = input('select the amount of characters in your password:  ')
    try:
        int(number_of_characters)
        print(generate_password(number_of_characters))
        break
    except ValueError:
        print()
        print('\033[91mu can only enter numbers!\033[0m')
        print()
        continue

