n=int(input("Enter no of values: "))
l=[]
d={}
for i in range(n):
    l.append(int(input()))
for j in l:
    if j%2==1:
        d[j]='No'
    else:
        d[j]='Yes'
print(d)
