n=int(input())
for i in range(t):
  a,b=map(int,input().split())
  s=input()
  freq=[0]*26
  for ch in s:
    freq[ord(ch)-ord('a')]+=1
  odd_count=sum(f % 2 for f in freq)
  if odd_count <= k + 1:
    print("YES")
  else:
    print("NO")    
