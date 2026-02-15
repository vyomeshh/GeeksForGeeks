'''Given an array arr[] of positive integers, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets among m students such that -
      i. Each student gets exactly one packet.
     ii. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum and return that minimum possible difference.
Examples:
Input: arr = [3, 4, 1, 9, 56, 7, 9, 12], m = 5
Output: 6Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 by choosing following m packets :[3, 4, 9, 7, 9].
Input: arr = [7, 3, 2, 4, 9, 12, 56], m = 3Output: 2Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 by choosing following m packets :[3, 2, 4].
Input: arr = [3, 4, 1, 9, 56], m = 5
Output: 55
Explanation: With 5 packets for 5 students, each student will receive one packet, so the difference is 56 - 1 = 55.
Constraints:
1 ≤ m <= arr.size ≤ 105
1 ≤ arr[i] ≤ 109'''class Solution:
    def findMinDiff(self, arr, m):
        n = len(arr)
        
        # 1. Base cases: If students are more than packets or no packets exist
        if m == 0 or n == 0:
            return 0
        if n < m:
            return -1
        
        # 2. Sort the array
        # This brings packets with similar chocolate counts close to each other
        arr.sort()
        
        # 3. Initialize minimum difference with a large value
        min_diff = float('inf')
        
        # 4. Sliding Window: Check every group of m consecutive packets
        # The first packet in the group is at index i
        # The last packet in the group is at index i + m - 1
        for i in range(n - m + 1):
            diff = arr[i + m - 1] - arr[i]
            
            if diff < min_diff:
                min_diff = diff
                
        return min_diff