n = int(input())
data = list(map(int, input().split()))
p = data[0]
levels = set(data[1:])
data = list(map(int, input().split()))
q = data[0]
levels.update(data[1:])
if len(levels) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
