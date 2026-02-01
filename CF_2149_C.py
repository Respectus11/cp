n = int(input())
for i in range(n):
    a, b =map(int, input().split())
    arrr =set(map(int, input().split()))
    wanted =set(range(b))
    missing =len(wanted - arrr)
    if b in arrr:
        moves =max(missing, 1)
    else:
        moves =missing
    print(moves)
