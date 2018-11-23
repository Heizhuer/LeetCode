# 翻转整数: 1234 ---> 4321
#          -1234 ---> -4321


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = {1: 1, 2: 10 ** 1, 3: 10 ** 2, 4: 10 ** 3, 5: 10 ** 4,
             6: 10 ** 5, 7: 10 ** 6, 8: 10 ** 7, 9: 10 ** 8, 10: 10 ** 9}
        total = 0

        for index, value in enumerate(str(x)[1:] if str(x).startswith('-') else str(x), 1):
            total += int(value) * r[index]

        if -2**31 < total < 2**31 - 1:
            return total if x > 0 else -total
        return 0


print(Solution().reverse(-234056000))


# 方案二
class Solution2:
    def reverse(self, x):
        if x < 0:
            flag = -1
        else:
            flag = 1

        x = x * flag
        result = 0

        while x:
            result = result * 10 + x % 10
            x = x // 10

        if -2**31 < result < 2**31 - 1:
            return result if flag == 1 else -result
        return 0


print(Solution2().reverse(234056000))