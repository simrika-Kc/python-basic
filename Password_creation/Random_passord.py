import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a strong password with the default length of 12 characters
strong_password = generate_password()
print(strong_password)
