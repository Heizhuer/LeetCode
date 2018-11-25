class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in mapping:
                # 防止stack为空的时候弹出值
                tem = stack.pop() if stack else '#'
                if mapping[i] != tem:
                    return False
            else:
                stack.append(i)
        return False if stack else True


print(Solution().isValid('(({{}[]))}'))