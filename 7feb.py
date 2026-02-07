'''Given an integer array arr[]. Find the maximum value of the sum of i*arr[i] for all 0 ≤ i ≤ arr.size()-1. The only operation allowed is to rotate(clockwise or counterclockwise) the array any number of times.

Examples :

Input: arr[] = [3, 1, 2, 8]
Output: 29
Explanation: Out of all the possible configurations by rotating the elements: arr[] = [3, 1, 2, 8] here (3*0) + (1*1) + (2*2) + (8*3) = 29 is maximum.
Input: arr[] = [1, 2, 3]
Output: 8
Explanation: Out of all the possible configurations by rotating the elements: arr[] = [1, 2, 3] here (1*0) + (2*1) + (3*2) = 8 is maximum.
Input: arr[] = [4, 13]
Output: 13
Constraints:
1 ≤ arr.size() ≤ 104
1 ≤ arr[i] ≤ 20'''
class Solution:
    def maxSum(self, arr):
        n = len(arr)
        
        # 1. Calculate the sum of all array elements
        cum_sum = sum(arr)
        
        # 2. Calculate the value for the initial configuration (S0)
        curr_val = 0
        for i in range(n):
            curr_val += i * arr[i]
            
        # Initialize max result with the initial configuration value
        max_val = curr_val
        
        # 3. Iterate to calculate values for subsequent rotations.
        # We simulate moving the last element to the front n-1 times.
        # To match the logic of "next rotation", we consider the element 
        # that moves from index n-1 to index 0.
        for i in range(1, n):
            # In the previous step, the element at index (n-i) was at the end.
            # Now it moves to the front.
            last_element = arr[n - i]
            
            # Formula: Next_Val = Curr_Val + Sum - (n * last_element)
            curr_val = curr_val + cum_sum - (n * last_element)
            
            if curr_val > max_val:
                max_val = curr_val
                
        return max_val