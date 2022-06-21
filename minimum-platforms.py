def minimumPlatform(self,n,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        platforms_needed = 1
        count = 1
        i,j = 1, 0
        while i<len(arr) and j<len(dep):
            if dep[j]>= arr[i]:
                platforms_needed +=1
                i+=1
            elif dep[j]<arr[i]:
                platforms_needed-=1
                j+=1
            count = max(platforms_needed, count)
        return count
      
# Time: O(nlogn)
# Space: O(1)
