def nextSmaller(arr,n):    
    ans, s = [], []
    dic = {}
    s.append(arr[0])
    for i in range(1, n,1):
        if len(s)==0: 
            s.append(arr[i])
            continue
        while s and arr[i] < s[-1]:
            dic[s[-1]]= arr[i]
            s.pop()
            
            if len(s)==0: break
            #if nex>= s[-1]: s.append(ele)
        s.append(arr[i])
   
    while s:
        dic[s[-1]] = -1
        s.pop()
    for i in range(n):
        ans.append(dic[arr[i]])
    return ans

arr= [1, 0, 2, 1, 2, 0]
nextSmaller(arr,6)

#Time: O(n)
# Space: O(n)
