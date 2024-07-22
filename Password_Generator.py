import random
import string

alphabets = string.ascii_letters
numbers = string.digits
special_symbols = string.punctuation

password_char = int(input('How many alphabets do you want in your password: '))
password_num = int(input('How many numbers do you want in your password: '))
password_special_char = int(input('How many special characters do you want: '))

password_generate = []

for _ in range(password_char):
    password_generate.append(random.choice(alphabets))
for _ in range(password_num):
    password_generate.append(random.choice(numbers))
for _ in range(password_special_char):
    password_generate.append(random.choice(special_symbols))

random.shuffle(password_generate)
password = ''.join(password_generate)

print(f'Your Generated Password is: {password}')
