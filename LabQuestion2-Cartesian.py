#Created by Kevin Ahlstrom on 01/05/2021 for CST-215
import random

#function to go through list of given sets and make
#a list containing cartesian product
def cartesian (setA, setB, setC):
    listA = [];
    for a in set1:
        for b in set2:
            for c in set3:
                listA.append([a,b,c])
    print(listA)
                
    
    
#create random sets with 3 integers
set1 = {random.randint(0,100),random.randint(0,100),random.randint(0,100)}
set2 = {random.randint(0,100),random.randint(0,100),random.randint(0,100)}
set3 = {random.randint(0,100),random.randint(0,100),random.randint(0,100)}
cartesianList = []
#print sets to console
print(set1)
print(set2)
print(set3)
print(" ")
cartesian(set1, set2, set3)



