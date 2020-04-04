'''
---------------------------------------------------------------------------
Question
---------------------------------------------------------------------------
Given an array nums, write a function to move all 0's to the end of it while 
maintaining the relative order of the non-zero elements.
---------------------------------------------------------------------------
'''


def moveZeroes(nums: [int]):
	'''
    n = len(nums) - 1
        for i in range(n,-1,-1):
            if nums[i] == 0:
                for j in range(i,n):
                    nums[j] = nums[j+1]
                nums[len(nums)-1] = 0 
            else:
                continue
        
    '''
    count = 0
    for i in range(0, len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1

    while count < len(nums):
        nums[count] = 0
        count += 1
     print(nums)


if __name__ == '__main__':
    arr = [0,1,0,3,12]
    moveZeroes(arr)
