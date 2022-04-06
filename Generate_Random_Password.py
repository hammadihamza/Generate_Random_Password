import string
import random

total = string.ascii_letters + string.digits
length = int(input('Please provide password length\n'))
Special_Char = input('Do you want your password to have special characters Yes|No?\n').lower()
if Special_Char == 'yes':
    total += string.punctuation
    print("".join(random.sample(total,length)))
elif Special_Char == 'no':
    print("".join(random.sample(total,length)))
else:
    print('Please provide a valid choice')
