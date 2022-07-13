def maxXorQueries(arr, queries):
	
	# Write your code here.
    ans = []
    arr.sort(reverse = True)
    for x,a in queries:
        res = 0
        for i in arr:
            if i<= a: res = max(res, x^i)
            else: res = -1
        ans.append(res)
    return ans


# Time: O(M*N logN)
# Space: O(M)
