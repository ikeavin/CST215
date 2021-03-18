#Created by Kevin Ahlstrom on 3/17/2021


def recursive(current, iteration, iterations):
    if iteration == iterations:
        return ""
    return  str(round(current,2)) + " " + recursive(4 * (current / 3), iteration + 1, iterations)

def explicit(start, iterations):
    string =""
    for x in range(iterations):
        string += str(round(start,2)) + " "
        start = 4 * (start / 3)
        
    return string
        
print("Recursive")
print(recursive(5,0,20))
print("\n \n \nExlpicit")
print(explicit(5, 20))
