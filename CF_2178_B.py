t = int(input())
for _ in range(t):
    r = input()
    n = len(r)

    s_count = 0
    for c in r:
        if c == 's':
            s_count += 1

    # Case: all 'u'
    if s_count == 0:
        print(n // 2 + 1)
        continue

    ans = 0
    i = 0

    while i < n:
        if r[i] == 'u':
            j = i
            while j < n and r[j] == 'u':
                j += 1

            length = j - i
            left_s = (i > 0 and r[i - 1] == 's')
            right_s = (j < n and r[j] == 's')

            if left_s and right_s:
                if length % 2 == 1:
                    ans += 1
            else:
                ans += (length + 1) // 2

            i = j
        else:
            i += 1

    print(ans)
