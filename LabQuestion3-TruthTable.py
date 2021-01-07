#Created by Kevin Ahlstrom on 01/05/2021 for CST-215

t = True;
f = False;

print(" P  |  Q  | P and Q"); 
print(str(t)+ " | " + str(t) +" | " + str((t and t)));
print(str(t)+ " | " + str(f) +" | " + str((t and f)));
print(str(f)+ " | " + str(t) +" | " + str((f and t)));
print(str(f)+ " | " + str(f) +" | " + str((f and f)));

print(" ");
print(" P  |  Q  | P or Q");
print(str(t)+ " | " + str(t) +" | " + str(t or t));
print(str(t)+ " | " + str(f) +" | " + str(t or f));
print(str(f)+ " | " + str(t) +" | " + str(f or t));
print(str(f)+ " | " + str(f) +" | " + str(f or f));

print(" ");
print(" P  |  Q  | If P, then Q");
if(t):
    print(str(t)+ " | " + str(t) +" | " + str(t));
else:
    print(str(t)+ " | " + str(t) +" | " + str(f));

if(t):
    print(str(t)+ " | " + str(f) +" | " + str(t));
else:
    print(str(t)+ " | " + str(f) +" | " + str(f));

if(f):
    print(str(f)+ " | " + str(t) +" | " + str(t));
else:
    print(str(f)+ " | " + str(t) +" | " + str(f));

if(f):
    print(str(f)+ " | " + str(f) +" | " + str(t));
else:
    print(str(f)+ " | " + str(f) +" | " + str(f));

print(" ");
print(" P  |  Q  | P if and only if Q");

print(str(t)+ " | " + str(t) +" | " + str(t == t));
print(str(t)+ " | " + str(f) +" | " + str(t == f));
print(str(f)+ " | " + str(t) +" | " + str(f == t));
print(str(f)+ " | " + str(f) +" | " + str(f == f));


    
    
