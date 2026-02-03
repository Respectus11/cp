s = input().strip()
c = 'a'
t = 0
for char in s:
    cd = abs(ord(char) - ord(c))
    ccd = 26 - cd
    t+= min(cd,ccd)
    c= char
print(t)