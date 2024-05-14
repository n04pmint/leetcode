
## Method # 1

nums = [1,3,5,7,4]
target = 5

def twoSum(nums, target):
    for n in range(0, len(nums)):
        for n2 in range(1, len(nums)):
            if nums[n] + nums[n2] == target:
                return n , n2
        
        
print(twoSum(nums, target))
 
# Method # 2

nums = [1,3,5,7,4]
target = 5

def twoSums(nums, target):
    seen = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in seen:
            return seen[diff], i
        else:
            seen[nums[i]] = i

print(twoSums(nums, target))


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 