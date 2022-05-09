n=int(input())
d={}
for i in range(n):
    print("Name    E-mail id")
    x=input().split()
    d[x[0]]=x[1]
print("Enter exit to stop and name to search")
while True:
    try:
        name=str(input())
        if name in d:
            print(name," = ",d[name])
        elif name=='exit':
            break
        else:
            print("Not found")
    except:
        break
