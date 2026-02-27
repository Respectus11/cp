n = int(input())
string = "codeforces"
for i in range(n):
    s =input()
    count =0
    for i in range(len(string)):
        if s[i] !=string[i]:
            count+= 1
    print(count)