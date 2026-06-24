class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        path=[]
        seen= set()
        nums.sort()
        
        def backtrack(start):

            x=tuple(path[:])
            if x not in seen:
                ans.append(path[:])
                seen.add(x)
            if start==len(nums):

                return
  
            for i in range(start,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()
        backtrack(0)
        return ans

            
        