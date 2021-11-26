
# Function params => nums: List[int], target: int
# Data type that the function returns => List[int]

def twoSum(nums, target):
    for i in range(len(nums)):
        for j in (range(i+1, len(nums))):
            if nums[i] + nums[j] == target:
                return [i, j]
