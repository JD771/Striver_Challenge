def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        s = []
        dic = {}
        s.append(nums2[0])
        for i in range(1, len(nums2)):
            nex = nums2[i]
            while s and s[-1]<nex: 
                dic[s[-1]]= nex
                s.pop()
            s.append(nex)
        for ele in s:
            dic[ele]= -1
        for i in range(len(nums1)):
            ans.append(dic[nums1[i]])

        return ans
      
# Time: O(n*m)
# Space: O(n)
