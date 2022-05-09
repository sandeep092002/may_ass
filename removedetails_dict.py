n={'sandeep':['sandeep',20,'m'],'pavan':['pavan',20,'m'],'karthik':['karthik',20,'m']}
print(n)
while True:
    if len(n)==0:
        break
    name=input()
    if name in n:
        n.pop(name)
        print(n)
    else:print('Not found')
