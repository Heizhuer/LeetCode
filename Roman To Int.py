# I - 1    V - 5
# X - 10   L - 50
# C - 100  D - 500  M - 1000
# IV = 4 and IX = 9
# XL = 40 and XC = 90
# CD = 400 and CM = 900


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        total = 0
        # 如果前一位数字比后一位数字小, 则减, 反之加
        for i in range(len(s) - 1):
            if base[s[i]] < base[s[i+1]]:
                total -= base[s[i]]
            else:
                total += base[s[i]]
        return total + base[s[-1]]


print(Solution().romanToInt('MCMXCIV'))
