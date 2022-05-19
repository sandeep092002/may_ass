import math
n=int(input())
'''while n%2==0:
    print(2)
    n=n/2'''
#x=int(math.sqrt(n))
for i in range(2,int(math.sqrt(n))+1,2):
    while n%i==0:
        print(i)
        n=n/i
if n>2:
    print(int(n))
