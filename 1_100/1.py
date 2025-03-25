#1. 两数之和
def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(0, len(nums)):
        try:
            return [i,nums[i+1::].index(target - nums[i])+i+1]
        except:
            continue

print(twoSum([2,7,11,15],9))