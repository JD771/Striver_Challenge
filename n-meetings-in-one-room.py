def maximumMeetings(self,n,start,end):
        # code here
        ans = []
        for i in range(n):
            ans.append([end[i],start[i]])
        ans.sort(key = lambda i:i[0])
        count = 1
        e = ans[0][0]
        
        for i in range(1,n):
            if ans[i][1]> e:
                count+=1
                e = ans[i][0]
        return count
      
# Time: O(nlogn)
# Space: O(n)
