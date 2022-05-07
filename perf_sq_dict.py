def perf_sq(x):
    c=0
    for i in range(1,(x//2)+1):
        if i*i==x:
            c=1
    if c==1:
        return True
    else:
        return False
n=int(input("Enter no of values: "))
l=[]
d={}
for i in range(n):
    l.append(int(input()))
for j in l:
    if perf_sq(j):
        d[j]='Yes'
    else:
        d[j]='No'
print(d)
