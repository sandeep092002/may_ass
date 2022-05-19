def subarraySum(nums, k) -> int:
        n=len(nums)
        if n==0:
            return 0
        count=0
        dic={}
        curr_sum=0
        for i in range(n):
            curr_sum+=nums[i]
            if(curr_sum==k):
                count+=1
                print("subarray is",nums[:i+1])
                break
            if(curr_sum-k in dic):
                #count+=dic[curr_sum-k]
                x=list(dic.keys())
                print("subarray is",nums[x.index(curr_sum-k)+1:i+1])
            if(curr_sum in dic):
                dic[curr_sum]+=1
            else:
                dic[curr_sum]=1
        if count==0:
                print('No sub array found')
        #return count
nums=list(map(int,input().split()))
k=int(input())
subarraySum(nums,k)
