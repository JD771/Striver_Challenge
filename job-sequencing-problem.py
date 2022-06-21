def JobScheduling(self,Jobs,n):
        # code here
        Jobs.sort(key= lambda i:i.profit)
        Jobs = Jobs[::-1]
        max_profit = 0
        count= 0
        res= [False]* 100
        for i in range(0,n):
            for j in range(Jobs[i].deadline-1,-1,-1):
                if not res[j]:
                    res[j] = True
                    max_profit += Jobs[i].profit
                    count+=1
                    break
        return [count, max_profit]
      
# Time: O(nlogn)
# Space: O(n)
