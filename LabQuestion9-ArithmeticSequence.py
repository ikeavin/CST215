#Created by Kevin Ahlstrom on 3/3/2021

def arithmetic_sequence(firstTerm, difference, amountOfTerms):
    for i in range(0, amountOfTerms):
        print(firstTerm + (i * difference))

first = int(input("First term: "))
diff = int(input("Common difference: "))
amt = int(input("Amount of terms: "))
arithmetic_sequence(first, diff, amt)
