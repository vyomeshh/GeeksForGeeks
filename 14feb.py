'''Given an array arr[] where each element denotes the length of a board, and an integer k representing the number of painters available. Each painter takes 1 unit of time to paint 1 unit length of a board.

Determine the minimum amount of time required to paint all the boards, under the constraint that each painter can paint only a contiguous sequence of boards (no skipping or splitting allowed).

Examples:

Input: arr[] = [5, 10, 30, 20, 15], k = 3
Output: 35
Explanation: The optimal allocation of boards among 3 painters is - 
Painter 1 → [5, 10] → time = 15
Painter 2 → [30] → time = 30
Painter 3 → [20, 15] → time = 35
Job will be done when all painters finish i.e. at time = max(15, 30, 35) = 35
Input: arr[] = [10, 20, 30, 40], k = 2
Output: 60
Explanation: A valid optimal partition is - 
Painter 1 → [10, 20, 30] → time = 60
Painter 2 → [40] → time = 40
Job will be complete at time = max(60, 40) = 60
Input: arr[] = [100, 200, 300, 400], k = 1
Output: 1000
Explanation: There is only one painter, so the painter must paint all boards sequentially. The total time taken will be the sum of all board lengths, i.e., 100 + 200 + 300 + 400 = 1000.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104
1 ≤ k ≤ 105'''
class Solution:
    def minTime(self, arr, k):
        # Helper function to check if all boards can be painted 
        # within 'limit' time using at most 'k' painters.
        def is_possible(limit):
            painters_count = 1
            current_boards_sum = 0
            
            for board in arr:
                if current_boards_sum + board <= limit:
                    # Current painter can take this board
                    current_boards_sum += board
                else:
                    # Need a new painter
                    painters_count += 1
                    current_boards_sum = board
                    
                    # If we exceed k painters, this limit is impossible
                    if painters_count > k:
                        return False
            return True

        # Binary search range
        low = max(arr)       # Min possible time (max element)
        high = sum(arr)      # Max possible time (sum of all elements)
        ans = high
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if is_possible(mid):
                # This time works! Let's try to find an even smaller time.
                ans = mid
                high = mid - 1
            else:
                # Not enough painters for this time limit, increase time.
                low = mid + 1
                
        return ans