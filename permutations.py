# Recursion
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def func(ds, idx, nums):
            if idx== n:
                ds.append(nums[:])
                return
            for i in range(idx,n):
                nums[i],nums[idx] = nums[idx], nums[i]
                func(ds, idx+1, nums)
                nums[i],nums[idx] = nums[idx], nums[i]
        ds = []
        nums.sort()
        func(ds, 0, nums)
        return ds
      
# Time: O(nlogn + n!*n)
# Space: O(n!)
