'''You are given a circular array arr[] of integers, find the maximum possible sum of a non-empty subarray. In a circular array, the subarray can start at the end and wrap around to the beginning. Return the maximum non-empty subarray sum, considering both non-wrapping and wrapping cases.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].
Input: arr[] = [5, -2, 3, 4]
Output: 12
Explanation: The circular subarray [3, 4, 5] gives the maximum sum of 12.
Constraints:
1 ≤ arr.size() ≤ 105
-104 ≤ arr[i] ≤ 104'''
class Solution:
    def maxCircularSum(self, arr):
        n = len(arr)
        
        # 1. Initialize variables
        # We need to track standard max (for non-wrapping)
        # and standard min (for wrapping).
        curr_max = 0
        curr_min = 0
        max_so_far = -float('inf') 
        min_so_far = float('inf')
        total_sum = 0
        
        for x in arr:
            total_sum += x
            
            # Standard Kadane's for Max Subarray
            curr_max += x
            if curr_max > max_so_far:
                max_so_far = curr_max
            if curr_max < 0:
                curr_max = 0
                
            # Standard Kadane's for Min Subarray
            curr_min += x
            if curr_min < min_so_far:
                min_so_far = curr_min
            if curr_min > 0:
                curr_min = 0
                
        # 2. Handle the "all negative" case
        # If all numbers are negative, max_so_far will be the largest single negative number.
        # total_sum - min_so_far would be 0, which is incorrect for "non-empty".
        if max_so_far < 0:
            return max_so_far
            
        # 3. Return the maximum of:
        # - The standard max subarray (max_so_far)
        # - The circular max (total_sum - min_so_far)
        return max(max_so_far, total_sum - min_so_far)