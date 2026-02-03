n = int(input())
teams = [list(map(int, input().split())) for i in range(n)]
count = 0
for i in range(n):        
    for j in range(n):    
        if i != j:
            if teams[i][0] == teams[j][1]:
                count += 1
print(count)
