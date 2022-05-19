class Solution:
    def subArraySum(self,arr, n, s): 
        if n==0:
            return 0
        count=0
        dic={}
        curr_sum=0
        for i in range(n):
            curr_sum+=arr[i]
            if(curr_sum==s):
                count+=1
                return 1,i+1
                
            if(curr_sum-s in dic):
                count+=dic[curr_sum-s]
                x=list(dic.keys())
                y=x.index(curr_sum-s)+2
                return y,i+1
            if(curr_sum in dic):
                dic[curr_sum]+=1
            else:
                dic[curr_sum]=1
        if count==0:
                return -1

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
