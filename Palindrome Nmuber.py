# 判断是否为回文数
# 翻转后若数字过大, 会遇到整数溢出的问题, 即只翻转数字的一半
# 如何判断已经翻转了一半: 原始数字除以 10，然后给反转后的数字乘上 10，当原始数字小于反转后的数字时


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or x % 10 == 0 and x != 0:
            return False
        if x == 0:
            return True
        if x > 0:
            tem = 0
            while x:
                tem = tem * 10 + x % 10
                x = x // 10
            if x  < tem * 10:       # 判断条件 待完善
                return True
        return False


print(Solution().isPalindrome(123))
