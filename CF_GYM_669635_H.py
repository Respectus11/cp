s_h, s_m = map(int, input().split(":"))
t_h, t_m = map(int, input().split(":"))
s_m -= t_m
if s_m < 0:
    s_m += 60
    s_h -= 1
s_h -= t_h
if s_h < 0:
    s_h += 24
print(f"{s_h:02d}:{s_m:02d}")
