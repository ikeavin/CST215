#Created by Kevin Ahlstrom on 01/05/2021 for CST-215

def countBits(n):
    initialN = n
    setBits = 0
    nAsBinary = ""
    while(n > 0):     
        nAsBinary = nAsBinary + str(n%2)
        if n % 2 == 1:
            setBits+=1
        n = n//2
    print(f'{initialN} in binary: {nAsBinary}, Amount of set bits: {setBits}')


print(countBits(1))
print(countBits(2))
print(countBits(3))
print(countBits(4))
print(countBits(7))
print(countBits(8))
print(countBits(63))
print(countBits(64))
