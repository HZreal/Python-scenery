# 将参数用命令行暴露处来
import argparse
import fire

def get_max(num1: int, num2: int):
    return num1 if num1 >= num2 else num2


# argparse库
parser = argparse.ArgumentParser(description='get_max Function')
parser.add_argument('num1', type=int, help='the first integer ')
parser.add_argument('num2', type=int, help='the second integer')


def use_argparse():

    args = parser.parse_args()
    max_num = get_max(args.num1, args.num2)
    print(max_num)

    # 终端调用脚本  python3 _argparse\&Fire_.py 19 22


# fire库
# 函数支持
# 类支持

class Calculator():
    def get_double(self, num_1):
        return 2 * num_1

    def get_num(self, num_2):
        return num_2


def use_fire():
    # 函数
    # fire.Fire(get_max)
    # 终端调用脚本  python3 _argparse&Fire_.py 12 22
    # 终端调用脚本  python3 _argparse&Fire_.py -num1 12 -num2 22

    # 类
    fire.Fire(Calculator)
    # 终端调用脚本  python3 _argparse&Fire_.py get_double 3
    # 终端调用脚本  python3 _argparse&Fire_.py get_num 3


if __name__ == '__main__':
    # use_argparse()
    use_fire()














