"""
命令行flag参数
"""

"""
内置的 argparse 命令行开发框架
适用于 一些参数多、面向用户的正式生产环境
"""



import argparse

# 构建一个命令行参数解析对象
parser = argparse.ArgumentParser(description='命令行参数')
parser.add_argument('--arg1', '-a1', type=int, help='参数1，非必须参数')
parser.add_argument('--arg2', '-a2', type=str, help='参数2，非必须参数,包含默认值', default='xag')
parser.add_argument('--arg3', '-a3', type=str, help='参数3，必须参数', required=True)

# 解析参数,获取所有的命令行参数（Namespace），然后转为字典
args = vars(parser.parse_args())
# 获取所有参数
for key in args:
    print(f"命令行参数名:{key}，参数值:{args[key]}")
