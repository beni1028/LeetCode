#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        initial_number = x
        final_number = 0
        while x>0:
            num =  x%10
            final_number = final_number * 10 + num
            x = x//10
        if final_number == initial_number:
            return True
        return False

    # def isPalindrome(self, x: int) -> bool:
    #     if str(x)== str(x)[::-1]:
    #         return True
    #     return False
# @lc code=end

