#Created by Kevin Ahlstrom on 01/05/2021 for CST-215

t = True;
f = False;

#AND
print("A          B        | A AND B"); 
print("A = " + str(t)+ ",  B = " + str(t) +" | " + str((t and t)));
print("A = " + str(t)+ ",  B = " + str(f) +"| " + str((t and f)));
print("A = " + str(f)+ ", B = " + str(t) +" | " + str((f and t)));
print("A = " + str(f)+ ", B = " + str(f) +"| " + str((f and f)));

#OR
print(" ");
print("A          B        | A OR B");
print("A = " + str(t)+ ",  B = " + str(t) +" | " + str(t or t));
print("A = " + str(t)+ ",  B = " + str(f) +"| " + str(t or f));
print("A = " + str(f)+ ", B = " + str(t) +" | " + str(f or t));
print("A = " + str(f)+ ", B = " + str(f) +"| " + str(f or f));

#NAND
print(" ");
print("A          B        | A NAND B"); 
print("A = " + str(t)+ ",  B = " + str(t) +" | " + str(not(t and t)));
print("A = " + str(t)+ ",  B = " + str(f) +"| " + str(not(t and f)));
print("A = " + str(f)+ ", B = " + str(t) +" | " + str(not(f and t)));
print("A = " + str(f)+ ", B = " + str(f) +"| " + str(not(f and f)));

#NOR
print(" ");
print("A          B        | A NOR B");
print("A = " + str(t)+ ",  B = " + str(t) +" | " + str(not(t or t)));
print("A = " + str(t)+ ",  B = " + str(f) +"| " + str(not(t or f)));
print("A = " + str(f)+ ", B = " + str(t) +" | " + str(not(f or t)));
print("A = " + str(f)+ ", B = " + str(f) +"| " + str(not(f or f)));
#XOR

print(" ");
print("A          B        | A XOR B");
print("A = " + str(t)+ ",  B = " + str(t) +" | " + str(((t and t == False) and (t or t))));
print("A = " + str(t)+ ",  B = " + str(f) +"| " + str(((t and f  == False) and (t or f))));
print("A = " + str(f)+ ", B = " + str(t) +" | " + str(((t and f  == False) and (t or f))));
print("A = " + str(f)+ ", B = " + str(f) +"| " + str(((f and f == False) and (f or f))));

#NOT
print(" ");
print("A        | NOT A");
print("A = " + str(t)+ " | " + str(not(t)));
print("A = " + str(f)+ "| " + str(not(f)));
print(" ");
print("B        | NOT B");
print("B = " + str(t) +" | " + str(not(t)));
print("B = " + str(f) +"| " + str(not(f)));



    
    
