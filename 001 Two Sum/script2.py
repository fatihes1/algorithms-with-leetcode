# Function params => nums: List[int], target: int
# Data type that the function returns => List[int]

def twoSum(nums, target):
    previousMap = {} # val : index

    for i, num enumerate(nums):
        difference = target - num
        if difference in previousMap:
            return [previousMap[difference], i]
        previousMap[num] = i
    return