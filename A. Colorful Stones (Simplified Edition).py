a = input().strip()
b = input().strip()
place = 0  
for c in b:
    if a[place] == c:
        place += 1
        if place == len(a):  
            break
print(place + 1)  
