import random
import string

Password = "Your Cool Kid Password is:"




# get random string password with letters, digits, and symbols
def get_random_password_string(length):
    password_characters = string.ascii_letters + string.punctuation
    password = ''.join(random.choice(password_characters) for i in range(length))
    print(password)

get_random_password_string(15)
get_random_password_string(15)
get_random_password_string(15)

