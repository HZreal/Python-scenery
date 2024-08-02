# 有两个数组，求他们的公共最大长度子数组，返回其最大长度
# 如 num1 和 num2 分别为 [1, 2, 3, 2, 1], [3, 2, 1, 4, 7] 则最大子数组为[3,2,1]，最大长度为 3
# 动态规划问题

def find_max_length_common_subarray(num1, num2):
    m, n = len(num1), len(num2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if num1[i - 1] == num2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

# 测试
num1 = [1, 2, 3, 2, 1]
num2 = [3, 2, 1, 4, 7]
result = find_max_length_common_subarray(num1, num2)
print(f"最大公共子数组的长度为: {result}")