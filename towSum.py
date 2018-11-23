# 求数组中两数之和与目标值相等的索引


# 暴力法:数组过大, 时间较长
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        t = []
        for x in range(len(nums)):
            for y in range(len(nums)):
                if x != y and nums[x] + nums[y] == target:
                    t.extend([x, y])
        return t[::2]


s = Solution()
r = s.twoSum([i for i in range(10)], 5)
print(r)


# 两边哈希法
class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {value: index for index, value in enumerate(nums)}
        print(hash_map)

        for index1, value in enumerate(nums):
            if target - value in hash_map:
                index2 = hash_map[target - value]
                if index1 != index2:
                    return index1, index2


print(Solution2().twoSum([3, 3], 6))








# ##################################################################################
# class Solution1:
#     def twoSum(self, nums, target):
#         d = []
#         hash_map = {value: index for index, value in enumerate(nums)}
#         print(hash_map)
#         # for value in hash_map.values():
#         for value, index1 in hash_map.items():
#             # in 判断字典的key
#             if target - value in hash_map:
#                 index2 = hash_map[target - value]
#                 # index1 = hash_map[value]   # 会报错 原因未知
#                 if index1 != index2:
#                     d.extend([index1, index2])
#         return d[::2]
#
#
# # index1 index2 必须分开 不能再同一个字典上面取, 比如[3, 3] 6
# print(Solution1().twoSum([3, 3], 6))

