n= int(input())
for i in range(n):
    a,b = map(int , input().split())
    gap = abs(a-b)
    moves = gap //10 + (1 if gap % 10 else 0)
    print (moves)