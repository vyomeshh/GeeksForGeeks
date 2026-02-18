'''Given an array of integers arr[]. You have to find the Inversion Count of the array. 
Note : Inversion count is the number of pairs of elements (i, j) such that i < j and arr[i] > arr[j].

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).
Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.
Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 104'''
class Solution:
    def inversionCount(self, arr):
        n = len(arr)
        # We'll use a helper function to perform merge sort and count inversions
        return self._merge_sort_count(arr, 0, n - 1)

    def _merge_sort_count(self, arr, l, r):
        count = 0
        if l < r:
            mid = (l + r) // 2
            
            # Count inversions in left half, right half, and during merge
            count += self._merge_sort_count(arr, l, mid)
            count += self._merge_sort_count(arr, mid + 1, r)
            count += self._merge(arr, l, mid, r)
            
        return count

    def _merge(self, arr, l, mid, r):
        left = arr[l:mid + 1]
        right = arr[mid + 1:r + 1]
        
        i = j = 0
        k = l
        inv_count = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                # If left[i] > right[j], then all elements in left[i:] 
                # are greater than right[j]
                arr[k] = right[j]
                inv_count += (len(left) - i)
                j += 1
            k += 1
            
        # Fill remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
            
        return inv_count