class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        def backtrack(i):
            ans.append(path[:])
            if i==len(nums):
                return ans

            for x in range(i,len(nums)):
                path.append(nums[x])
                backtrack(x+1)
                path.pop()
                
                
                
        backtrack(0)
        return ans
        