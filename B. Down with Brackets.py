def check(s):
    if not s:
        return False
    balance = 0
    for i, char in enumerate(s):
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0 and i != len(s) - 1:
            return False  
    return balance == 0 
for j in range(int(input())):
  s = input().strip()
  if check(s):
      print("NO")
  else:
      print("YES")