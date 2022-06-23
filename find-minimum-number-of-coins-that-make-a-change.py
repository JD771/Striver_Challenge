# Greedy Approach
# Fails at certain points
def min_coins(coins,V):
    count = 0
    ans = []
    coins.sort(reverse= True)
    for i in range(len(coins)):
        while coins[i]<= V:
            V-= coins[i]
            count+=1
            ans.append(coins[i])
    return (count, ans)

print(min_coins(coins,V))

# Time: O(V)
# Space: O(1)
