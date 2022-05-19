#Write a python program to print a year is Leap year or not''
a=int(input('Enter the year: '))

#code snippet(means logic)
if (a%4==0 and a%100!=0) or a%400==0:
    print(a,"is a leap year")
else:print(a,"is not a leap year")

#Also we can use
"""if a%4==0:
    if a%100==0:
        if a%400==0:
            print(a,'is aLeap year')
        else:print(a,'is Not a leap year')
    else:print(a,'is a Leap year')
else:print(a,'is Not a leap year')"""
