'''Given an array arr[] of positive integers and an integer k. You have to find the maximum value for each contiguous subarray of size k. Return an array of maximum values corresponding to each contiguous subarray.

Examples:

Input: arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Output: [3, 3, 4, 5, 5, 5, 6]
Explanation: 
1st contiguous subarray [1, 2, 3], max = 3
2nd contiguous subarray [2, 3, 1], max = 3
3rd contiguous subarray [3, 1, 4], max = 4
4th contiguous subarray [1, 4, 5], max = 5
5th contiguous subarray [4, 5, 2], max = 5
6th contiguous subarray [5, 2, 3], max = 5
7th contiguous subarray [2, 3, 6], max = 6
Input: arr[] = [5, 1, 3, 4, 2], k = 1
Output: [5, 1, 3, 4, 2]
Explanation: When k = 1, each element in the array is its own subarray, so the output is simply the same array'''
from collections import deque

class Solution:
    def maxOfSubarrays(self, arr, k):
        n = len(arr)
        dq = deque()
        result = []
        
        for i in range(n):
            # 1. Remove indices that are out of this window
            if dq and dq[0] == i - k:
                dq.popleft()
            
            # 2. Remove indices of elements smaller than current element
            # because they will never be the maximum in this or future windows
            while dq and arr[dq[-1]] <= arr[i]:
                dq.pop()
            
            # 3. Add current element's index
            dq.append(i)
            
            # 4. The front of the deque is the max for the window
            # (We only start adding to result once the first window is complete)
            if i >= k - 1:
                result.append(arr[dq[0]])
                
        return result