'''Given a binary array arr[] containing only 0s and 1s and an integer k, you are allowed to flip at most k 0s to 1s. Find the maximum number of consecutive 1's that can be obtained in the array after performing the operation at most k times.

Examples:

Input: arr[] = [1, 0, 1], k = 1
Output: 3
Explanation: By flipping the zero at index 1, we get the longest subarray from index 0 to 2 containing all 1’s.
Input: arr[] = [1, 0, 0, 1, 0, 1, 0, 1], k = 2
Output: 5
Explanation: By flipping the zeroes at indices 4 and 6, we get the longest subarray from index 3 to 7 containing all 1’s.
Input: arr[] = [1, 1], k = 2
Output: 2
Explanation: Since the array is already having the max consecutive 1's, hence we dont need to perform any operation. Hence the answer is 2.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ k ≤ arr.size()
0 ≤ arr[i] ≤ 1'''
class Solution:
    def maxOnes(self, arr, k):
        n = len(arr)
        left = 0
        zero_count = 0
        max_len = 0
        
        for right in range(n):
            # If current element is 0, increment the count of zeros
            if arr[right] == 0:
                zero_count += 1
            
            # If zeros exceed k, shrink the window from the left
            while zero_count > k:
                if arr[left] == 0:
                    zero_count -= 1
                left += 1
            
            # Update the maximum length found so far
            # The current valid window is from index 'left' to 'right'
            current_len = right - left + 1
            if current_len > max_len:
                max_len = current_len
                
        return max_len