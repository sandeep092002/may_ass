def binarysearch(arr,l,u,k):
    if u>=l:
        mid=(l+u)//2
        if arr[mid]==k:
            return mid
        elif arr[mid]>k:
            return binarysearch(arr,l,mid-1,k)
        else:
            return binarysearch(arr,mid+1,u,k)
    else:
        return -1
arr=sorted(list(map(int,input().split())))
k=int(input("Enter searching number: "))
result=binarysearch(arr,0,len(arr)-1,k)
print(arr)
if result!=-1:
    print("Element is present at index",result)
else:
    print("Element is not present in array")
 
