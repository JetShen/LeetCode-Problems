#217. Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Example 1:                     #Example 2:                      #Example 3:
#Input: nums = [1,2,3,1]        #Input: nums = [1,2,3,4]         #Input: nums = [1,1,1,3,3,4,3,2,4,2]
#Output: true                   #Output: false                   #Output: true

nums = [1,1,1,3,3,4,3,2,4,2]


def containsDuplicate(nums):
    if len(nums) == len(set(nums)):
        return False
    else:
        return True 
    
print(containsDuplicate(nums))