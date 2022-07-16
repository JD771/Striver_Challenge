def nextSmaller(arr, n):
    ans, s = [],[]
    for i in range(n-1, -1,-1):
        if len(s)==0: ans.append(-1)
        elif s[-1]<arr[i]: ans.append(s[-1])
        else:
            while s and s[-1]>=arr[i]: s.pop()
            if len(s)==0: ans.append(-1)
            else: ans.append(s[-1])
        s.append(arr[i])
    ans.reverse()
    return ans

#Time: O(n)
# Space: O(n)

