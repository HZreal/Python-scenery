# 命令行参数

# sys.argv
import sys
args = sys.argv
# 参数个数
args_length = len(sys.argv) if sys.argv else 0

print("排除运行主文件参数，其他参数列表为:", args)

print("参数总数：", args_length)


# argparse
import argparse
# 构建一个命令行参数解析对象
parser = argparse.ArgumentParser(description='命令行参数')
parser.add_argument('--arg1', '-a1', type=int, help='参数1，非必须参数')
parser.add_argument('--arg2', '-a2', type=str, help='参数2，非必须参数,包含默认值', default='xag')
parser.add_argument('--arg3', '-a3', type=str, help='参数3，必须参数', required=True)

# 解析参数,获取所有的命令行参数（Namespace），然后转为字典
args = vars(parser.parse_args())

# 获取所有参数
print("所有命令行参数为:")
for key in args:
    print(f"命令行参数名:{key}，参数值:{args[key]}")


# getopt
from getopt import getopt
# 获取参数
# sys.argv[1:]：获取除脚本文件名外的所有命令行参数
# opts：存有所有选项及其输入值的元组列表
# args：去除有用的输入以后剩余的部分
opts, args = getopt(sys.argv[1:], 'i:u:p:d:', ['ip=', 'user=', 'pwd=', 'db='])

# 获取参数值
# 短参数
# python3 4_getopt.py -i 127.0.0.1 -u root -p 123456 -d mysqldb
# 长参数
# python3 4_getopt.py --ip 127.0.0.1 -u root -p 123456 -d mysqldb
ip_pre = [item[1] for item in opts if item[0] in ('-i', '--ip')]
ip = ip_pre[0] if len(ip_pre) > 0 else None
print("参数ip：", ip)

user_pre = [item[1] for item in opts if item[0] in ('-u', '--user')]
user = user_pre[0] if len(user_pre) > 0 else None
print("参数user：", user)

pwd_pre = [item[1] for item in opts if item[0] in ('-p', '--pwd')]
pwd = pwd_pre[0] if len(pwd_pre) > 0 else None
print("参数pwd：", pwd)

db_pre = [item[1] for item in opts if item[0] in ('-d', '--db')]
db = db_pre[0] if len(db_pre) > 0 else None
print("参数db：", db)

# 测试
# 短参数
# python3 4_getopt.py -i 127.0.0.1 -u root -p 123456 -d mysqldb
# 长参数
# python3 4_getopt.py --ip 127.0.0.1 --user root --pwd 123456 --db mysqldb


# click第三方依赖库
# import click

# 安装依赖
# pip3 install -U click

# @click.command()
# @click.option('--arg1', default='111', help='参数arg1，默认值为「111」')
# @click.option('--arg2', type=int, help='参数arg2')
# @click.option('--arg3', type=str, help='参数arg3')
# def start(arg1, arg2, arg3):
#     """
#     基于参数arg1、参数arg2、参数arg3运行项目
#     :param arg1:
#     :param arg2:
#     :param arg3:
#     :return:
#     """
#     print("参数arg1值为:", arg1)
#     print("参数arg2值为:", arg2)
#     print("参数arg3值为:", arg3)



# 对于一些简单自用且不那么正规的场景，个人觉得可以考虑用 sys.argv 模块快速构建命令行参数；而对一些参数多、面向用户的正式生产环境，建议利用 argparse 模块或 click 依赖来创建命令行参数