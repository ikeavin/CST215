#Created by Kevin Ahlstrom on 2/10/2021
import random

def gcd(num1, num2):
    r = num1 % num2
    while num2:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1

def rand_gcd():
    num1 = random.randint(0, 9999999)
    num2 = random.randint(9, 9999999)

    if num1 < num2:
        g = gcd(num1, num2)
        print(f'GCD of {num2} and {num1} is {g}')
    else:
        g = gcd(num2, num1)
        print(f'GCD of {num1} and {num2} is {g}')
    
    
for x in range(0, 100):
    rand_gcd()
