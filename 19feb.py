'''Given an array arr[] of integers and a range [low, high], find all the numbers within the range that are not present in the array. return the missing numbers in sorted order.

Examples:

Input: arr[] = [10, 12, 11, 15], low = 10, high = 15
Output: [13, 14]
Explaination: Numbers 13 and 14 lie in the range [10, 15] but are not present in the array.
Input: arr[] = [1, 4, 11, 51, 15], low = 50, high = 55
Output: [50, 52, 53, 54, 55]
Explaination: Numbers 50, 52, 53, 54 and 55 lie in the range [50, 55] but are not present in the array.
Constraints:
1 ≤ arr.size(), low, high ≤ 105
1 ≤ arr[i] ≤ 105'''
class Solution:
    def missingRange(self, arr, low, high):
        # 1. Convert the array to a set
        # This allows for O(1) average time complexity when checking 
        # if a number exists in the array.
        present_nums = set(arr)
        
        missing_numbers = []
        
        # 2. Iterate through every integer in the target range [low, high]
        for num in range(low, high + 1):
            # 3. If the number is not in the set, it's one of our missing values
            if num not in present_nums:
                missing_numbers.append(num)
        
        # The list is already sorted because we iterated from low to high
        return missing_numbers