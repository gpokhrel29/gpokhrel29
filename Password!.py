import random
import string

def generate_password(length: int = 13):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for i in range (length))
    return password

password = generate_password()
print(f'Here is your generated password!: {password}')