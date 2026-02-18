'''You are given an array of intervals arr[][], where each interval is represented by two integers [start, end] (inclusive). Return the maximum number of intervals that overlap at any point in time.

Examples :

Input: arr[][] = [[1, 2], [2, 4], [3, 6]]
Output: 2
Explanation: The maximum overlapping intervals are 2(between (1, 2) and (2, 4) or between (2, 4) and (3, 6))
 
Input: arr[][] = [[1, 8], [2, 5], [5, 6], [3, 7]]
Output: 4
Explanation: The maximum overlapping intervals are 4 (between (1, 8), (2, 5), (5, 6) and (3, 7))
Constraints:
2 ≤ arr.size() ≤ 2 * 104
1 ≤ arr[i][0] < arr[i][1] ≤ 4*106'''
class Solution:
    def overlapInt(self, arr):
        starts = []
        ends = []
        
        # 1. Collect all start and end points
        for interval in arr:
            starts.append(interval[0])
            ends.append(interval[1])
        
        # 2. Sort both independently
        starts.sort()
        ends.sort()
        
        max_overlap = 0
        current_overlap = 0
        
        i = 0  # Pointer for starts
        j = 0  # Pointer for ends
        n = len(arr)
        
        # 3. Use Two Pointers to simulate a "Sweep Line"
        while i < n:
            # If a meeting starts at the same time or before another ends,
            # it's an overlap (because intervals are inclusive).
            if starts[i] <= ends[j]:
                current_overlap += 1
                max_overlap = max(max_overlap, current_overlap)
                i += 1
            else:
                # A meeting has finished, decrease the current count
                current_overlap -= 1
                j += 1
                
        return max_overlap