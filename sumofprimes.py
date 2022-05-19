import math
def primes(n):
    sieve=[True]*n
    prefix=[0]*n
    sieve[0]=sieve[1]=False
    x=int(math.sqrt(n))
    for i in range(2,x+1):
        if sieve[i]:
            for j in range(i*i,n,i):
                sieve[j]=False
    for i in range(2,n):
        if sieve[i]:
            prefix[i]=prefix[i-1]+i
        else:
            prefix[i]=prefix[i-1]
    return prefix
m=int(input())
pf=primes(m+1)
print(pf[m])
