'''
---------------------------------------------------------------------------
Question
---------------------------------------------------------------------------
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
---------------------------------------------------------------------------
'''


def maxSubArray(nums: [int]) -> int:
        maxNum = maxCur = nums[0]
        for i in range(1, len(nums)):
            maxCur = max(nums[i], maxCur+nums[i])
            maxNum = max(maxCur, maxNum) 
        return maxNum

if __name__ == '__main__':
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(maxSubArray(arr))
