# -*- coding: utf-8 -*-
import string
import random


def get_random_code(bit: int) -> str:
    """
    bit   生成随机串的位数
    """
    # 字母
    a = string.ascii_letters
    print('备选字母--->', a)
    # 数字
    b = string.digits
    print('备选数字--->', b)
    # 特殊字符
    c = string.punctuation
    print('备选特殊字符--->', c)

    # 生成的随机串，列表存储
    random_list = random.sample(a + b + c, bit)  # 返回列表
    print(len(random_list), random_list)

    # 列表转字符串
    random_str = ''.join(random_list)
    print(random_str)
    return random_str


def generate_count_number(count: int, bit: int = 6):
    """
    生成count个，bit位随机码
    """
    print('生成的个数count--->', count)
    print('生成的位数bit--->', bit)

    _bit = bit
    # print(f'%0{_bit}d')

    # bit位的随机数的最大范围
    max_num = 0
    while True:
        if _bit == 0:
            break
        _bit -= 1
        max_num += 9 * 10 ** _bit
    print(max_num)

    for i in range(count):
        # 6位
        # random_num = '%06d' % random.randint(0, 999999)

        # 10位
        # random_num = '%010d' % random.randint(0, 9999999999)

        # bit位
        random_num = f'''%0{bit}d''' % random.randint(0, max_num)

        # print(random_num)
        yield random_num


def random_from_selector(selector: list):
    """
    从列表中随机出一个元素返回
    """
    return random.choice(selector)


if __name__ == '__main__':
    # 生成32位随机串
    # random_str = get_random_code(32)

    # 生成count个，bit位随机码
    random_num_iterator = generate_count_number(count=3, bit=6)
    for random_num in random_num_iterator:
        print(random_num)

    # 从列表中随机弹出一个元素
    # pop_num = random_from_selector([12, 23, 43, 54, 35])
    # print(pop_num)
