'''Given an array arr[] that contains positive and negative integers (may contain 0 as well). Find the maximum product that we can get in a subarray of arr[].

Note: It is guaranteed that the answer fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is [6, -3, -10] with product = 6 * (-3) * (-10) = 180.
Input: arr[] = [-1, -3, -10, 0, 6]
Output: 30
Explanation: The subarray with maximum product is [-3, -10] with product = (-3) * (-10) = 30.
Input: arr[] = [2, 3, 4] 
Output: 24 
Explanation: For an array with all positive elements, the result is product of all elements. 
Constraints:
1 ≤ arr.size() ≤ 106
-10  ≤  arr[i]  ≤  10'''
class Solution:
    def maxProduct(self, arr):
        n = len(arr)
        if n == 0:
            return 0
            
        # Initialize tracking variables with the first element
        max_so_far = arr[0]
        min_so_far = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            curr = arr[i]
            
            # If curr is negative, max and min will swap roles when multiplied
            if curr < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # The new max/min is either the current element itself 
            # or the product of the current element and the previous max/min
            max_so_far = max(curr, max_so_far * curr)
            min_so_far = min(curr, min_so_far * curr)
            
            # Global maximum updated at each step
            result = max(result, max_so_far)
            
        return result