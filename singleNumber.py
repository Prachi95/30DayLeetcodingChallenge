'''
---------------------------------------------------------------------------
Question
---------------------------------------------------------------------------
Given a non-empty array of integers, every element appears twice except for one. 
Find that single one.
---------------------------------------------------------------------------
'''


def singleNumber(nums: [int]) -> int:
    arr = []
    for n in nums:
        if n not in arr:
            arr.append(n)
        else:
            arr.remove(n)
    return arr.pop()


if __name__ == '__main__':
    arr = [4,1,2,1,2]
    print(singleNumber(arr))
