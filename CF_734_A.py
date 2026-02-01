n= int(input())
s= input()
acount=0
dcount =0
for i in s:
    if i=="A":
        acount+=1
    elif i== "D":
        dcount+=1
if acount>dcount:
    print("Anton")
elif acount<dcount:
    print("Danik")
else:
    print ("Friendship")