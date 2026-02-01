n,k,l,c,d,p,nl,np = map (int,input().split())
req1 = (k*l)//nl
req2 = (c*d)
req3 = p//np
print((min(req1,req2,req3)//n))
