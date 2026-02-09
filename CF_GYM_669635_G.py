from collections import Counter
n = int(input())
s = list(input().strip())
counter = Counter(s)
if n % 4 != 0:
    print("===")
else:
    target = n // 4
    if any(counter[x] > target for x in "ACGT"):
        print("===")
    else:
        for i in range(n):
            if s[i] == "?":
                for x in "ACGT":
                    if counter[x] < target:
                        s[i] = x
                        counter[x] += 1
                        break
        print("".join(s))
