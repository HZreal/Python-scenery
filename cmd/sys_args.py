"""
命令行flag参数
"""

"""
sys.argv
适用于 一些简单自用且不那么正规的场景，快速构建命令行参数
"""

import sys

args = sys.argv
print("排除运行主文件参数，其他参数列表为:", args)
# 参数个数
args_length = len(sys.argv) if sys.argv else 0
print("参数总数：", args_length)
