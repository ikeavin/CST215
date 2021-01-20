#Created by Kevin Ahlstrom on 01/05/2021 for CST-215

t = True;
f = False;

print(" P \t|  Q \t| P and Q"); 
print(str(t)+ "\t| " + str(t) +"\t| " + str((t and t)));
print(str(t)+ "\t| " + str(f) +"\t| " + str((t and f)));
print(str(f)+ "\t| " + str(t) +"\t| " + str((f and t)));
print(str(f)+ "\t| " + str(f) +"\t| " + str((f and f)));

print(" ");
print(" P \t|  Q \t| P or Q");
print(str(t)+ "\t| " + str(t) +"\t| " + str(t or t));
print(str(t)+ "\t| " + str(f) +"\t| " + str(t or f));
print(str(f)+ "\t| " + str(t) +"\t| " + str(f or t));
print(str(f)+ "\t| " + str(f) +"\t| " + str(f or f));

print(" ");
print(" P \t| Q \t| If P, then Q");
if(t):
    print(str(t)+ "\t| " + str(t) +"\t| " + str(t));
else:
    print(str(t)+ "\t| " + str(t) +"\t| " + str(f));

if(t):
    print(str(t)+ "\t| " + str(f) +"\t| " + str(f));
else:
    print(str(t)+ "\t| " + str(f) +"\t| " + str(f));

if(f):
    print(str(f)+ "\t| " + str(t) +"\t| " + str(f));
else:
    print(str(f)+ "\t| " + str(t) +"\t| " + str(t));

if(f):
    print(str(f)+ "\t| " + str(f) +"\t| " + str(f));
else:
    print(str(f)+ "\t| " + str(f) +"\t| " + str(t));

print(" ");
print(" P \t| Q\t| P if and only if Q");

print(str(t)+ "\t| " + str(t) +"\t| " + str(t == t));
print(str(t)+ "\t| " + str(f) +"\t| " + str(t == f));
print(str(f)+ "\t| " + str(t) +"\t| " + str(f == t));
print(str(f)+ "\t| " + str(f) +"\t| " + str(f == f));


    
    
