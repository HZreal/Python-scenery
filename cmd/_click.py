"""
命令行flag参数
"""

"""
第三方 click
适用于 一些参数多、面向用户的正式生产环境
"""

import click

# 安装依赖
# pip3 install -U click

@click.command()
@click.option('--arg1', default='111', help='参数arg1，默认值为「111」')
@click.option('--arg2', type=int, help='参数arg2')
@click.option('--arg3', type=str, help='参数arg3')
def start(arg1, arg2, arg3):
    """
    基于参数arg1、参数arg2、参数arg3运行项目
    :param arg1:
    :param arg2:
    :param arg3:
    :return:
    """
    print("参数arg1值为:", arg1)
    print("参数arg2值为:", arg2)
    print("参数arg3值为:", arg3)
