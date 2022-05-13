def isarmstrong(n):
    s=0
    m=n
    while True:
        d=n%10
        s=s+(d*d*d)
        n=n//10
        if n<=0:
            break
    if m==s:
        return True
    else:
        return False
n=int(input("Enter a number: "))
print(isarmstrong(n))
        
