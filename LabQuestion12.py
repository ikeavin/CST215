#Created on 3/24/2021 for CST-215 by Kevin Ahlstrom

setA = {1, 2, 3, 4}
setB = {1, 2, 3, 4, 5, 6}
setC = {5, 6, 7}

print(f'SetA: {setA}')
print(f'SetB: {setB}')
print(f'SetC: {setC}')
print(f'SetC Union SetA: {(setC.union(setA))}')
print(f'SetB Intersect SetC: {(setB.intersection(setC))}')
print(f'SetC Difference SetB: {(setC.difference(setB))}')
print(f'SetC Symm. Difference SetA: {(setC.symmetric_difference(setA))}')

def is_subset(A, B):
    diff_set = A.difference(B)
    return len(diff_set) == 0

print(is_subset(setA, setB))
print(is_subset(setB, setA))
