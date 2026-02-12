'''You are given an array heights[] representing the heights of towers and another array cost[] where each element represents the cost of modifying the height of respective tower.

The goal is to make all towers of same height by either adding or removing blocks from each tower.
Modifying the height of tower 'i' by 1 unit (add or remove) costs cost[i].
Return the minimum cost to equalize the heights of all the towers.

Examples:

Input: heights[] = [1, 2, 3], cost[] = [10, 100, 1000]
Output: 120
Explanation: The heights can be equalized by either "Removing one block from 3 and adding one in 1" or "Adding two blocks in 1 and adding one in 2". Since the cost of operation in tower 3 is 1000, the first process would yield 1010 while the second one yields 120.
Input: heights[] = [7, 1, 5], cost[] = [1, 1, 1]
Output: 6
Explanation: The minimum cost to equalize the towers is 6, achieved by setting all towers to height 5.
Constraints:
1 ≤ heights.size() = cost.size() ≤ 105
1 ≤ heights[i] ≤ 104
1 ≤ cost[i] ≤ 103'''
class Solution:
    def minCost(self, heights, cost):
        # N might be passed as an argument in some versions of this problem
        # If the signature is minCost(self, heights, cost, N), add N to the arguments.
        
        # Zip heights and costs together and sort by height
        # This allows us to process towers in order of increasing height
        towers = sorted(zip(heights, cost))
        
        # Calculate the total weight (sum of all costs)
        total_weight = sum(cost)
        
        # Find the weighted median
        # The optimal height is where the cumulative cost reaches half the total weight
        current_weight = 0
        median_weight = (total_weight + 1) // 2
        target_height = towers[0][0]
        
        for h, c in towers:
            current_weight += c
            if current_weight >= median_weight:
                target_height = h
                break
        
        # Calculate the total cost to modify all towers to the target_height
        min_total_cost = 0
        for h, c in zip(heights, cost):
            min_total_cost += abs(h - target_height) * c
            
        return min_total_cost