class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs or '' in strs:
            return ''
        strs.sort(key=lambda x: len(x))
        shortest_str = strs[0]

        for i in range(len(shortest_str)):
            for str in strs:
                if str[i] != shortest_str[i]:
                    return shortest_str[:i]

        return shortest_str


print(Solution().longestCommonPrefix(['fix', 'five', 'file']))