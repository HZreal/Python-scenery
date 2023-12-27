"""
 @author: huang
 @date: 2023-12-26
 @File: data_representation_and_storage.py
 @Description: 
"""
import struct

data = b'\x01\x00\x00\x00\x00\x00\x80\x3f'

# 解包数据
result = struct.unpack('if', data)
# Python 的 struct 模块默认使用小端格式（least-significant byte first）
# 对于 'i' 格式字符，它表示一个标准的四字节整数（int）,即读取四个字节： \x01\x00\x00\x00 ==> 01 00 00 00 ==> 小端格式下为十六进制数 1
# 对于 'f' 格式字符，它表示一个标准的四字节单精度浮点数（float）,即读取四个字节： \x00\x00\x80\x3f ==> 00111111 10000000 00000000 00000000
# 第一位是符号位 0，表示这是一个正数；接下来的 8 位是指数位 01111111，指数部分需要减去偏移量（对于单精度浮点数，这个偏移量是 127）来获取实际的指数值，即指数位为 127 - 127 = 0。剩下的 23 位是尾数位，而所有的尾数位都是 0， 且由于浮点数的表示中隐含了一个 1（除非指数是特殊值），所以尾数部分表示的是 1.0， 因此这个浮点数为 1.0 × 2^0 = 1.0。
print('result  ---->  ', result)


def parse_mp_file(mp_file_path):
    with open(mp_file_path, 'rb') as file:
        # 读取文件内容
        data = file.read()

        # 解析行数和列数
        rowLen, colLen = struct.unpack('ii', data[:8])
        print('rowLen  ---->  ', rowLen)
        print('colLen  ---->  ', colLen)

        # 初始化一个列表来存储经纬度数据
        # coordinates = []

        # 遍历每一组数据
        for i in range(rowLen * colLen):
            # 计算当前经纬度数据的起始位置
            start = 24 + i * 16
            # 解析经度和纬度
            lon, lat = struct.unpack('dd', data[start:start + 16])
            print('lon, lat ----> ', lon, lat)
            # coordinates.append((lon, lat))

        # print('coordinates  ---->  ', coordinates)


if __name__ == '__main__':
    """
    .mp 数据为二进制流格式，字节顺序定义如下:
    1~4字节，int32，行数，rowLen
    5~8字节，int32，列数，colLen
    9~24字节，保留
    以下数据一共 rowLen * colLen 组，每组16字节
    25~48字节，double * 2，经度、纬度
    25~32字节，double，经度
    33~40字节，double，纬度
    41~56字节，double * 2，经度、纬度
    ...
    ...
    """
    parse_mp_file('assets/fusion.mp')
