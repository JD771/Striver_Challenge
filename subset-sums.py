# Approach 1: Power Set
def subsetSums(self, arr, N):
		# code here
		if N==0: return
		n = 2**N -1
		for i in range(0, n):
		    ans = []
		    for j in range(0,N-1):
		        if i & (1<<j):
		            ans.append(arr[i])
	    return ans
    
# Time: O(2^n *n)
# Space: O(1)

# Approach 2: Recursion
class Solution:
	def subsetSums(self, arr, N):
		# code here
		#User function Template for python3
		def recursion(arr, N, i, summ, sumSubset):
		    if i==N:
		        sumSubset.append(summ)
		        return
		    recursion(arr, N, i+1, summ+ arr[i], sumSubset)
		    recursion(arr, N, i+1, summ, sumSubset)
	    
	    sumSubset = []
	    recursion(arr, N, 0, 0, sumSubset)
	    return sumSubset
    
# Time: O(2^N)
# Space: O(2^N)
