def subarraySum(nums, k) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        dic={}
        curr_sum=1
        for i in range(n):
            curr_sum*=nums[i]
            if(curr_sum==k):
                count+=1
            if(curr_sum/k in dic):
                count+=dic[curr_sum/k]
            if(curr_sum in dic):
                dic[curr_sum]+=1
            else:
                dic[curr_sum]=1
        return count
nums=list(map(int,input().split()))
k=int(input())
print(subarraySum(nums,k))
