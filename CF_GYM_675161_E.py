n=int(input())
for i in range(n):
    a=int(input())
    if a >=1900:
        print("Division 1")
    elif 1600<=a<=1899:
        print("Division 2")
    elif 1400<=a<=1599:
        print("Division 3")
    elif  a<=1399:
        print("Division 4")
