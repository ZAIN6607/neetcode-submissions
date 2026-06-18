class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        sum=0
        ans=len(nums)
        flag=0
        for i in range(0,len(nums)):
            sum+=nums[i]
            while(sum>=target):
                flag=1
                ans=min(ans,i-left+1)
                sum-=nums[left]
                left+=1
        if flag==0:
            return 0
        return ans
            
        
        
        

            

        