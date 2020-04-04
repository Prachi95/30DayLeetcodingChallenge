'''
---------------------------------------------------------------------------
Question
---------------------------------------------------------------------------
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, 
replace the number by the sum of the squares of its digits, and repeat the process until the 
number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers.
---------------------------------------------------------------------------
'''


def isHappy(n: int) -> bool:
        val = 0
        sum = 0
        while n != 0:
            val = n % 10
            sum = sum + (val*val)
            n = (n - val)/10
                     
        if sum == 1:
            return True
        elif sum == 4:
            return False
        else:
            return isHappy(sum)

if __name__ == '__main__':
    num = 19
    print(isHappy(num))
