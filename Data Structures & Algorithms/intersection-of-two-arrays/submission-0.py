class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic1 = defaultdict(int)
        dic2 = defaultdict(int)
        ans = []
        
       
        for i in nums1:
            dic1[i] += 1
        for i in nums2:
            dic2[i] += 1
        
        
        for i in dic1:
            if i in dic2:
                
                ans.extend([i])
        
        return ans

        
        