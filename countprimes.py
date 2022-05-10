def countprimes(x,y):
    d=0
    for p in range(x+1,y):
        c=0
        for q in range(2,p):
            if p%q==0:
                c=c+1
        if c==2:
            d=d+1
    return d

n=int(input())
l=[]
for i in range(n):
    x,y=input().split()
    l.append(countprimes(int(x),int(y)))
for j in l:
    print(j,end='\n')
