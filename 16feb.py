'''Given a 2D array arr[][], where arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a particular time.

Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.

Examples:

Input: arr[][] = [[1, 4], [10, 15], [7, 10]]
Output: true
Explanation: Since all the meetings are held at different times, it is possible to attend all the meetings.
Input: arr[][] = [[2, 4], [9, 12], [6, 10]]
Output: false
Explanation: Since the second and third meeting overlap, a person cannot attend all the meetings.
Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 2*106'''
class Solution:
    def canAttend(self, arr):
        # 1. Sort the meetings based on their start times
        # This ensures we only need to compare a meeting with its immediate predecessor.
        arr.sort(key=lambda x: x[0])
        
        # 2. Iterate through the sorted list
        for i in range(1, len(arr)):
            # If the current meeting starts before the previous one ends, it's an overlap.
            # Note: start == previous_end is allowed per problem statement.
            if arr[i][0] < arr[i-1][1]:
                return False
        
        # 3. If no conflicts are found, return True
        return True