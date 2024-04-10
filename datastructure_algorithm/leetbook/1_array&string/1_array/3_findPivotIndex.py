# LC
# 寻找数组的中心索引
# 给你一个整数数组 nums ，请计算数组的 中心下标 。
# 数组 中心下标 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。
# 如果中心下标位于数组最左端，那么左侧数之和视为 0 ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。
# 如果数组有多个中心下标，应该返回 最靠近左边 的那一个。如果数组不存在中心下标，返回 -1 。
# 链接：https://leetcode-cn.com/leetbook/read/array-and-string/yf47s/

# 本题与主站 1991 题相同：https://leetcode-cn.com/problems/find-the-middle-index-in-array/


# 初步解决方案
class Solution1:
    """先计算总和，随着遍历的过程，不断修改左值和右值，并比较两者是否相等"""

    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)
        for i in range(len(nums)):
            if i == 0:                 # 0位置需特别考虑
                left_sum = 0
            else:
                left_sum += nums[i - 1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        return -1


# 比较条件改为-----> 左值*2+当前值是否等于总和     优势：不必考虑索引0
class Solution2:
    """先计算总和，随着遍历的过程，仅计算左值，判断l左值×2+当前值是否等于总和"""

    def pivotIndex(self, nums: list[int]) -> int:
        all_sum = sum(nums)
        left = 0
        for i in range(len(nums)):
            if left * 2 + nums[i] == all_sum:
                return i
            else:
                left += nums[i]
        return -1




if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    res = Solution1().pivotIndex(nums)
    print(res)