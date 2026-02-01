n= int(input())
for i in range(n):
    s=input().strip()
    round = square =0
    move=0
    for j in s:
        if j=="(":
            round+=1
        elif j==')':
            if round>0:
                round-=1
                move+=1
        elif j=="[":
            square +=1
        elif j==']':
            if square>0:
                square-=1
                move+=1
    print(move)

