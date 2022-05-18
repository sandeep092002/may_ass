def pivotIndex(nums):
        sum=0
        pf=[]
        for i in nums:
            sum=sum+i
            pf.append(sum)
        for i in range(len(nums)):
            lsum=pf[i]-nums[i]
            rsum=pf[len(pf)-1]-pf[i]
            if lsum==rsum:
                return i
        return -1
nums=list(map(int,input().split()))
print(pivotIndex(nums))
