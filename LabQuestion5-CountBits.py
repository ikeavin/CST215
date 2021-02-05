#Created by Kevin Ahlstrom on 01/05/2021 for CST-215

def countBits(n):
    initialN = n
    setBits = 0
    nAsBinary = ""
    while(n > 0):     
        nAsBinary = str(n%2) + nAsBinary
        if n % 2 == 1:
            setBits+=1
        n = n//2
    print(f'{initialN} in binary: {nAsBinary}, Amount of set bits: {setBits} ')


countBits(1)
countBits(2)
countBits(3)
countBits(4)
countBits(7)
countBits(8)
countBits(63)
countBits(64)
