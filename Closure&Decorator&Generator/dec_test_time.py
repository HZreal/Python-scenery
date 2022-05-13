import mydecorator_as_module
# 此时已经执行了print('装饰器执行了'), 说明装饰器在导入完成时会立即执行

# 装饰器的执行时机：
         # 当当前模块加载完成后，装饰器会立即执行，对已有函数进行装饰

if __name__ == '__main__':

    mydecorator_as_module.comment()