'''Given a garden with n flowers planted in a row, that is represented by an array arr[], where arr[i] denotes the height of the ith flower.You will water them for k days. In one day you can water w continuous flowers. Whenever you water a flower its height increases by 1 unit. You have to maximize the minimum height of all flowers after  k days of watering.

Examples:

Input: arr[] = [2, 3, 4, 5, 1], k = 2, w = 2
Output: 2
Explanation: The minimum height after watering is 2.
Day 1: Water the last two flowers -> arr becomes [2, 3, 4, 6, 2]
Day 2: Water the last two flowers -> arr becomes [2, 3, 4, 7, 3]
Input: arr[] = [5, 8], k = 5, w = 1
Output: 9
Explanation: The minimum height after watering is 9.
Day 1 - Day 4: Water the first flower -> arr becomes [9, 8]
Day 5: Water the second flower -> arr becomes [9, 9]
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ w ≤ arr.size()
1 ≤ k ≤ 105
1 ≤ arr[i] ≤ 109'''
class Solution:
    def maxMinHeight(self, arr, k, w):
        n = len(arr)
        
        # Helper function to check if a minimum height 'target' is possible
        def can_achieve(target):
            days_spent = 0
            # diff array handles range updates in O(1)
            # It tracks where the watering effect for a window ends
            diff = [0] * (n + 1)
            added_height = 0
            
            for i in range(n):
                # Update the effect of previous watering windows ending here
                added_height -= diff[i]
                
                # Current actual height of the flower
                current_h = arr[i] + added_height
                
                if current_h < target:
                    # How many more days do we need for this flower?
                    needed = target - current_h
                    days_spent += needed
                    
                    # If we exceed the allowed days k, this target is impossible
                    if days_spent > k:
                        return False
                    
                    # Apply the watering: it affects flowers from i to i + w - 1
                    added_height += needed
                    if i + w < n:
                        diff[i + w] += needed
                        
            return days_spent <= k

        # Binary search for the maximum possible "minimum height"
        low = min(arr)
        high = min(arr) + k
        result = low
        
        while low <= high:
            mid = low + (high - low) // 2
            if can_achieve(mid):
                result = mid
                low = mid + 1 # Try to push for an even higher minimum
            else:
                high = mid - 1 # Target too high, lower the expectation
                
        return result