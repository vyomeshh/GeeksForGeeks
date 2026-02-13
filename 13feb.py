'''Given a positive number n and a number d. Find the count of positive numbers smaller or equal to n such that the difference between the number and sum of its digits is greater than or equal to given specific value d.

Examples:

Input: n = 13, d = 2
Output: 4
Explanation:
There are 4 numbers satisfying the
Conditions. These are 10, 11, 12 and 13.
Input: n = 14, d = 3
Output: 5
Explanation:
There are 5 numbers satisfying the
Conditions. These are 10, 11, 12, 13 and 14.
Constraints:
1 ≤ n ≤ 109
1 ≤ d ≤ 109'''
class Solution:
    def getCount(self, n, d):
        # Helper to calculate the sum of digits of a number
        def get_digit_sum(num):
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            return s

        low = 1
        high = n
        smallest_x = -1
        
        # We use Binary Search because (x - digit_sum(x)) is a 
        # monotonically non-decreasing function.
        while low <= high:
            mid = low + (high - low) // 2
            
            # Check the condition: number - sum of its digits >= d
            if mid - get_digit_sum(mid) >= d:
                smallest_x = mid
                # Try to find an even smaller number that satisfies this
                high = mid - 1 
            else:
                # Value is too small, move to the right half
                low = mid + 1 
                
        # If no number satisfies the condition
        if smallest_x == -1:
            return 0
            
        # All numbers from smallest_x to n will satisfy the condition
        return n - smallest_x + 1