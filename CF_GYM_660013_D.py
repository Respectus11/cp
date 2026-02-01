n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    num1 = str(a) + "0" * b
    num2 = str(c) + "0" * d
    if len(num1) > len(num2):
        print(">")
    elif len(num1) < len(num2):
        print("<")
    else:
        if num1 > num2:
            print(">")
        elif num1 < num2:
            print("<")
        else:
            print("=")
