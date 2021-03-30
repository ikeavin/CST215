#Created by Kevin Ahlstrom on 3/30/21 for CST-215

def encrypt(target, num):
    result = ""
    for i in range(len(target)):
        char = target[i]
        if char == " " or char == ',' or char == '.' or char == '?' or char== '!' or char== "'":
            result += char
        elif ord(char) >= 97:
            result += chr((ord(char) + num-97) % 26 + 97)
        elif ord(char) >= 65:
            result += chr((ord(char) + num-65) % 26 + 65)
    return result
    

print("Hi, my name is Kevin.")
print(encrypt("Hi, my name is Kevin.", 13))
