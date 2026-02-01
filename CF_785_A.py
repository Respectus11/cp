n = int(input())
counter =0 
for i in range(n):
    a = str(input())
    if a == "Tetrahedron":
        counter += 4
    elif a== "Cube":
        counter+=6
    elif a== "Octahedron":
        counter+=8
    elif a== "Dodecahedron":
        counter+=12
    elif a== "Icosahedron":
        counter +=20
print (counter)
    
