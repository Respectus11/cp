n= int( input())
for i in range (n):
    a = input().split()
    if len(set(a))==1:
        print ("YES")
    else:
        print( "NO")