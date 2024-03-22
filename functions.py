import random
import string

def generate_password(number_of_characters: int) -> list:
    password = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's']
    
    number_of_characters = int(number_of_characters)
    for characters in range(number_of_characters):
        password.append(random.choice(alphabet))
    
    print(number_of_characters)
    return password
        