from typing import List
class Solution:
    def maxSubArray(nums: List[int]) -> int:
        # Initialize our variables using the first element.
        current_subarray = max_subarray = nums[0]

        # Start with the 2nd element since we already used the first one.
        for num in nums[1:]:
            # If current_subarray is negative, throw it away. Otherwise, keep adding to it.
            current_subarray = max(num, current_subarray + num)
            max_subarray = max(max_subarray, current_subarray)

        return max_subarray
arr = [1, 2, 4]
def max(num, val):
        return num < val
print(max(5, 6))
# print(Solution.maxSubArray([-2,-1,-3]))
# print(Solution.append([-2,-1,-3], 8))
print(arr)
