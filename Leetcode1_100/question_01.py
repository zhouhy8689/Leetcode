'''
两数之和
给定一个整数数组nums
和一个目标值target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
示例:
nums = [2, 7, 11, 15], target = 9
因为nums[0] + nums[1] = 2 + 7 = 9,所以返回[0, 1]
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        解题思路：
        1. 创建一个字典mapping
        2. 将原数组构造成枚举类型，遍历数组中的元素，
        3. 如果target - value 不在数组中，则以value为key,下标为值存入mapping
        4. 如果target - value 在字典中，返回列表
        """
        mapping = {}
        for index, value in enumerate(nums):  #
            diff = target - value
            if diff in mapping:
                return [mapping[diff], index]
            else:
                mapping[value] = index

if __name__ == '__main__':
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))