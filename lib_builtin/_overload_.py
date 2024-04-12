# -*- coding:utf-8 -*-
"""
 @author: huang
 @date: 2024-04-12
 @File: _overload_.py
 @Description: 
"""
from typing import overload, Optional, Union


class A:
    def __init__(self):
        pass

    @overload
    def write(self, value: str):
        ...

    @overload
    def write(self, value: int):
        ...

    def write(self, value: Optional[Union[str, int]]):
        print(value)


if __name__ == '__main__':
    a = A()
    a.write('hello world')
    a.write(123)
