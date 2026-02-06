'''You are given three arrays a[], b[], c[] of the same size . Find a triplet such that (maximum-minimum) in that triplet is the minimum of all the triplets. A triplet should be selected so that it should have one number from each of the three given arrays. This triplet is the happiest among all the possible triplets. Print the triplet in decreasing order.

Note: If there are 2 or more smallest difference triplets, then the one with the smallest sum of its elements should be displayed.

Examples:

Input: a[] = [5, 2, 8] , b[] = [10, 7, 12] , c[] = [9, 14, 6]
Output: [7, 6, 5]
Explanation: The triplet [5, 7, 6]  has difference (maximum - minimum)= (7 - 5) = 2 which is minimum of all triplets.  
Input: a[] = [15, 12, 18, 9] , b[] = [10, 17, 13, 8] , c[] = [14, 16, 11, 5]
Output: [11, 10, 9]
Explanation: Multiple triplets have the same minimum difference, and among them [11, 10, 9] has the smallest sum, so it is chosen.
Constraints:
1 ≤ a.size(), b.size() ,c.size() ≤ 105
1 ≤ a[i], b[i], c[i] ≤ 105'''
class Solution:
    def smallestDiff(self, a, b, c):
        # 1. Sort the arrays to allow logical traversal
        a.sort()
        b.sort()
        c.sort()
        
        n_a, n_b, n_c = len(a), len(b), len(c)
        i = j = k = 0
        
        # Initialize tracking variables
        # min_diff starts at infinity
        min_diff = float('inf')
        min_sum = float('inf')
        result_triplet = []
        
        # 2. Iterate until one array is exhausted
        while i < n_a and j < n_b and k < n_c:
            val_a, val_b, val_c = a[i], b[j], c[k]
            
            # Find current min and max in the triplet
            current_min = min(val_a, val_b, val_c)
            current_max = max(val_a, val_b, val_c)
            current_diff = current_max - current_min
            current_sum = val_a + val_b + val_c
            
            # 3. Update result based on criteria:
            # - Strictly smaller difference OR
            # - Same difference but smaller sum
            if current_diff < min_diff or (current_diff == min_diff and current_sum < min_sum):
                min_diff = current_diff
                min_sum = current_sum
                result_triplet = [val_a, val_b, val_c]
            
            # 4. Move the pointer of the smallest element forward.
            if val_a == current_min:
                i += 1
            elif val_b == current_min:
                j += 1
            else:
                k += 1
                
        # 5. Return the triplet sorted in decreasing order as requested
        result_triplet.sort(reverse=True)
        return result_triplet