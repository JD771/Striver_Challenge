def fractionalknapsack(self, W,Items,n):
        
        # code here
        # Greedy Approach 
        Items.sort(key=lambda i:i.value/i.weight, reverse =True)
        curweight = 0
        profit = 0
    
        for i in range(n):
            if (curweight+ Items[i].weight) < W:
                profit+= Items[i].value
                curweight+= Items[i].weight
            else:
                remaining = W- curweight
                profit += (Items[i].value/Items[i].weight)* remaining
                break
        return profit
      
# Time: O(nlogn)
# Space: O(1)
