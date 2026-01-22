import string
import secrets
import random

def generate_password(length):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    password=[
        secrets.choice(s1),
        secrets.choice(s2),
        secrets.choice(s3),
        secrets.choice(s4)
    ]
    chars=s1+s2+s3+s4
    password+=[secrets.choice(chars) for _ in range(length-4)]
    random.shuffle(password)
    print("Your password: ","".join(password))
    
plen = int(input("Enter password length: "))
generate_password(plen)