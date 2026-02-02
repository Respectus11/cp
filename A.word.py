n=input()
counter=0
for i in n:
    if i.islower():
        counter+=1
if len(n)-counter>counter:
    print(n.upper())
else:
    print(n.lower())