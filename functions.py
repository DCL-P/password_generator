import random

def generate_password(number_of_characters: int) -> list:
    password = []
    characters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '?', '!', '@', '#', '$', '%', '^', '&', '*']
    
    number_of_characters = int(number_of_characters)
    for characters in range(number_of_characters):
        password.append(random.choice(characters_list))
    
    generated_password = ''.join(password)
    return f'enjoy your new password!:  \033[93m{generated_password}\033[0m'
        