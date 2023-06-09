#1. Two Sums
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example 1:                                 Example 2:
# Input: nums = [2,7,11,15], target = 9      Input: nums = [3,2,4], target = 6
# Output: [0,1]                               Output: [1,2]

nums = [2,7,11,15]
target = 9
def twosums(nums,target):
    for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    return []

print(twosums(nums,target))