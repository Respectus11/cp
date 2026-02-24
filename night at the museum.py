n=input().strip()
pointer='a'
moves=0
for i in n:
    gap=abs(ord(pointer)-ord(i))
    moves+=min(gap,26 - gap)
    pointer=i
print(moves)