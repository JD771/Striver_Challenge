def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)):
            k-=1
            if k==0: return nums[i]
            
# Time: O(nlogn)
# Space: O(1)
