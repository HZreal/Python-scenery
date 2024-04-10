# 此题与 leetcode题1 近似，但数组为非递减序列[1, 2, 2, 3, 4, 5, 5, 6, 7]


# 二分查找  时间复杂的度 O(nlog(n))  空间复杂度 O(1)
def twoSum1(nums: list, target: int):
    n = len(nums)
    for i in range(n):               # 时间复杂度 O(n)
        low = i + 1
        high = n - 1
        while low <= high:            # 通过二分查找，查找target-nums[i]，时间复杂度 O(log(n))
            mid = (low + high) // 2
            if nums[mid] == target - nums[i]:
                return [i + 1, mid + 1]
            elif nums[mid] > target - nums[i]:   # 在左半边继续找
                high = mid - 1
            else:                       # 在由半边继续找
                low = mid + 1


# 双指针
def twoSum2(nums: list, target: int):
    pass



res = twoSum1([1, 2, 2, 3, 4, 5, 5, 6, 7], 10)
print(res)















