from heapq import heapify, heappop,heappush
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, a, b, c):
        a.sort()
        b.sort()
        seen, pq, res = set(), list(), list()
        i,j = len(a)-1, len(b)-1
        seen.add((i,j))
        pq.append((-(a[i]+b[j]), (i,j)))
        for _ in range(c):
            ele, (i,j)= heappop(pq)
            res.append(-ele)
            for ni, nj in [(i-1,j),(i,j-1)]:
                if ni>= 0 and nj>=0 and (ni,nj) not in seen:
                    heappush(pq, (-(a[ni]+b[nj]),(ni,nj)))
                    seen.add((ni,nj))
        return res
      
# Time: O(nlogn)
# Space: O(n)
