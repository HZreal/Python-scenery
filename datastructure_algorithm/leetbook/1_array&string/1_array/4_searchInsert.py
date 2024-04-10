

def binary_search(nums: list, target: int) -> int:
    """二分查找算法"""
    low = 0
    high = len(nums) - 1
    while low <= high:
        # if low == high:
        #     print('--------------')
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1


res = binary_search([1, 3, 5, 7, 9, 11], 10)
print(res)


class Solution:
    """"""

    def searchInsert1(self, nums: list[int], target: int) -> int:
        """直接循环比较"""
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert2(self, nums: list[int], target: int) -> int:
        """二分查找"""

        # 当low == high == mid时，若此时对比失败，即查询失败不存在目标值，
        # 要么此时nums[mid] > target时high-=1，要么nums[mid] < target时low+=1，不论如何，此时的low值均是插入的索引位置
        # 如：   9, 11  索引值分别为7，8        target=10
        # 若此时low == high == mid == 7   查询失败，low = mid+1 = 8
        # 若此时low == high == mid == 8   查询失败，high = mid-1 = 7，low不变还是8

        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return low                # while终止条件是low>high，也是最后一次查询(low==high的情况)失败，

# res = Solution().searchInsert1([1, 3, 7, 8, 11, 17, 28, 39, 50], 29)
# print(res)





