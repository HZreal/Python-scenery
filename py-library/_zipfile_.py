# python 压缩/解压模块 zipfile

# import zipfile
import os.path
from zipfile import ZipFile
from zipfile import Path

# class ZipFile(file, mode="r", compression=ZIP_STORED, allowZip64=True, compresslevel=None)

test_file = '../test_dir/filezip_test.zip'
z1 = ZipFile(test_file)
z2 = ZipFile('../test_dir/temp.zip', mode='r')

# zip_filename = z2.filename   # 文件名(含路径)
# print(zip_filename)

# filelist = z1.filelist  # ZipInfo对象列表
# print('filelist-------------', filelist)
# infolist = z1.infolist()  # 调用的是self.filelist，故依然返回ZipInfo对象列表
# print('infolist-------------', infolist)
# print(filelist == infolist)  # True
# for zipinfo in z1.filelist:
#     print('zipinfo----------', zipinfo)

namelist = z2.namelist()  # zip包的文件名列表
print('namelist-------------', namelist)


# getinfo = z1.getinfo(name='text.txt')   # 参数name为文件名 或者 ZipInfo文件对象
# print('getinfo-------------', getinfo)  # 返回zip包中某个文件名对应的ZipInfo对象

# t = z1.open(name='text.txt', mode='r', pwd=None)  # 参数name为文件名 或者 ZipInfo文件对象
# # t = z1.open(name=z1.filelist[0], mode='r', pwd=None)
# print('open----read-----', t.read())  # 包括readline、readlines、seek等文件方法
# t.close()

# 设置提取已加密文件的默认密码
# z1.setpassword(pwd='gfdhdghf'.encode())

# 读取zip包中某个文件的字节数据
# content = z1.read(name=z1.filelist[0], pwd=None)  # 参数name为文件名 或者 ZipInfo文件对象
# print(content)


# z1.write(filename='../test_dir/text1.txt', arcname='ttt.txt', compress_type=None, compresslevel=None)


# z1.writestr()


# z1.testzip()


# 提取zip包中的某一个文件，参数member为文件名 或 其ZipInfo对象；path指定提取出来的存放路径，不传默认为当前目录下
# path1 = z1.extract(member=z1.filelist[0], path='/Users/hz/Desktop/', pwd=None)
# print(path1)
# 提取zip包中的某些文件，参数members为namelist()或其子列表；path指定提取出来的存放路径，不传默认为当前目录下；
# z1.extractall(path='/Users/hz/Desktop/', members=z1.namelist()[0:2], pwd=None)


# 管理器使用
# ZipFile与ZipFile.open()均支持管理器
# with ZipFile(test_file, 'r') as z:
#     with z.open('text3.txt', 'r') as t3:
#         content = t3.readlines()
#         print(content)


# 处理zip包中的隐藏文件 __MACOSX/ -------mac生成的元数据管理文件
def check_archive_for_bad_filename(file):
    """检查zip文件是否含有非实用文件"""
    zip_file = ZipFile(file, 'r')
    for filename in zip_file.namelist():
        print('zip中filename----------', filename)
        if filename.startswith('__MACOSX/'):
            # 只要发现文件名前缀含有'__MACOSX/'，则检测到非实用文件，返回True
            return True


def remove_bad_filename_from_archive(original_file, temporary_file):
    """移除非实用文件"""
    with ZipFile(original_file, 'r') as original_zip:
        for item in original_zip.namelist():
            if not item.startswith('__MACOSX/'):
                buffer = original_zip.read(item)
                if not os.path.exists(temporary_file):
                    with ZipFile(temporary_file, 'w') as new_zip:
                        new_zip.writestr(item, buffer)
                else:
                    with ZipFile(temporary_file, 'a') as new_zip:
                        new_zip.writestr(item, buffer)


def run():
    archive_filename = '../test_dir/filezip_test.zip'
    temp_filename = '../test_dir/temp.zip'
    result = check_archive_for_bad_filename(archive_filename)
    if result:
        print('Removing MACOSX file from archive.')
        remove_bad_filename_from_archive(archive_filename, temp_filename)
    else:
        print('No MACOSX file in archive.')


# zipfile.Path()
path1 = Path(root='../test_dir/temp.zip', at='')
path2 = Path(root=z1, at='')
name = path1.name
print(name)
is_dir = path1.is_dir()
is_file = path1.is_file()


# path1.open()    # 调用ZipFile.open()

# iterdir = path1.iterdir()
# for item in iterdir:
#     print('dir or file -------', item)    # Path Object
#     p = path1.joinpath(item.name)         # 拼路径
#     for i in p.iterdir():
#         print(i)             # Path Object

def list_all_file(path: Path):
    """递归显示目录树"""
    print('list this directory --------')
    iterator = path.iterdir()
    if iterator is None:
        print('this directory is None')
    for item in iterator:
        if item.is_dir():
            print('this directory name----------', item.name)
            p = path.joinpath(item.name)
            list_all_file(p)
        else:
            print('this file name------------', item.name)
            continue


# ZipInfo 对象

zipinfo = z2.filelist[1]
print(zipinfo)             # ZipInfo 对象
print('filename--------', zipinfo.filename)
print('is_dir--------', zipinfo.is_dir())
print('date_time--------', zipinfo.date_time)
print('compress_type--------', zipinfo.compress_type)
print('compress_size--------', zipinfo.compress_size)
print('create_system--------', zipinfo.create_system)
print('create_version--------', zipinfo.create_version)
print('internal_attr--------', zipinfo.internal_attr)
print('external_attr--------', zipinfo.external_attr)
print('header_offset--------', zipinfo.header_offset)
print('CRC-32--------', zipinfo.CRC)
print('compress_size--------', zipinfo.compress_size)
print('file_size--------', zipinfo.file_size)


z1.close()
z2.close()


# --------------------------------------------------------------------------------
# zipfile 模块提供了简单的命令行接口用于与 ZIP 归档的交互
# 如果你想要创建一个新的 ZIP 归档，请在 -c 选项后指定其名称然后列出应当被包含的文件名:
# $ python -m zipfile -c monty.zip spam.txt eggs.txt
# 传入一个目录也是可接受的:
# $ python -m zipfile -c monty.zip life-of-brian_1979/
# 如果你想要将一个 ZIP 归档提取到指定的目录，请使用 -e 选项:
# $ python -m zipfile -e monty.zip target-dir/
# 要获取一个 ZIP 归档中的文件列表，请使用 -l 选项:
# $ python -m zipfile -l monty.zip

# 命令行选项
# -l <zipfile>
# --list <zipfile>
# 列出一个 zipfile 中的文件名。
#
# -c <zipfile> <source1> ... <sourceN>
# --create <zipfile> <source1> ... <sourceN>
# 基于源文件创建 zipfile。
#
# -e <zipfile> <output_dir>
# --extract <zipfile> <output_dir>
# 将 zipfile 提取到目标目录中。
#
# -t <zipfile>
# --test <zipfile>
# 检测 zipfile 是否有效。


if __name__ == '__main__':
    print('main--------------')
    # run()
    # list_all_file(path1)
