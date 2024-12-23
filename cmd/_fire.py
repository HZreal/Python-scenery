"""
命令行flag参数
"""

"""
第三方 google 的 fire 命令行开发框架。简洁优雅，质量高
适用于 一些参数多、面向用户的正式生产环境
函数支持
类支持
"""

import fire


def get_max(num1: int, num2: int):
    return num1 if num1 >= num2 else num2


class Calculator:
    def multiply(self, number: int, count: int):
        return number * count




def use_fire():
    # 函数式
    # fire.Fire(get_max)
    # 终端调用脚本  python _fire.py 12 22
    # 终端调用脚本  python _fire.py -num1 12 -num2 22

    # 类式
    fire.Fire(Calculator)
    # 终端调用脚本  python _fire_.py multiply 3 4
    # 终端调用脚本  python _fire_.py multiply -number 3 -count 4
    # 终端调用脚本  python _fire_.py multiply --number=3 --count=4


if __name__ == '__main__':
    use_fire()
