# 浅拷贝：只会对可变类型的第一层进行拷贝，不会对子对象进行拷贝，拷贝成功会开批一个新的内存空间储存拷贝的这个对象
# 对不可变类型的浅拷贝，其实是拷贝了原数据的一个引用，不会开辟新的内存空间

# 深拷贝： 只要发现对象有可变类型，那么就对该对象到最后一个可变类型的每一层对象进行拷贝，拷贝成功会开辟新的内存空间

# 不管是给对象进行深拷贝还是浅拷贝，只要拷贝成功就会开辟新的内存空间存储拷贝的对象。
# 浅拷贝和深拷贝都是针对可变类型的拷贝

# 浅拷贝和深拷贝的区别是:
# 浅拷贝最多拷贝对象的一层，深拷贝可能拷贝对象的多层

# 不可变类型(不允许在原内存地址处修改)：数字，字符串，元组
# 可变类型(允许在原内存地址处修改)：列表，字典，集合

import copy


# 浅拷贝
# 对于不可变数据类型：
num1 = 1
num2 = copy.copy(num1)
print('num1内存地址：', id(num1))
print('num2内存地址：', id(num2))                # 地址相同

tuple1 = (4, 5, 8)
tuple2 = copy.copy(tuple1)
print('tuple1内存地址：', id(tuple1))
print('tuple2内存地址：', id(tuple2))           # 地址相同，说明没有开辟新的内存空间
# 结论：
# 对于不可变类型的浅拷贝，其实是拷贝了原数据的一个引用，两个变量指向同一个内存地址


# 对于可变数据类型
list1 = [1, 3, 5, [2, 8]]
list2 = copy.copy(list1)
print('list1内存地址：', id(list1))
print('list2内存地址：', id(list2))     # 地址不同
list1.append(9)
print(list1, list2)      # list1被修改，list2依然不变

print('list1[3]内存地址：', id(list1[3]))
print('list2[3]内存地址：', id(list2[3]))     # 地址相同，说明不会拷贝其子元素
list1[3].append(7)
print(list1, list2)         # 修改list1的子元素时，list2的子元素也被修改

# 结论：
# 只会对可变类型的第一层进行拷贝，不会对子对象进行拷贝





# 深拷贝
# 对于不可变类型
num3 = 1
num4 = copy.deepcopy(num3)
print('num3:', id(num3), 'num4:', id(num4))              # 地址相同

str1 = 'hello'
str2 = copy.deepcopy(str1)
print('str1:', id(str1), 'str2:', id(str2))              # 地址相同

tuple3 = (1, )
tuple4 = copy.deepcopy(tuple3)
print('tuple3:', id(tuple3), 'tuple4:', id(tuple4))        # 地址相同

tuple5 = (4, 2, [7, 5])
tuple6 = copy.deepcopy(tuple5)
print('tuple5:', id(tuple5), 'tuple6:', id(tuple6))        # 地址不同
print('tuple5[1]:', id(tuple5[1]), 'tuple6[1]:', id(tuple6[1]))        # 地址相同,对不可变子对象不拷贝
print('tuple5[2]:', id(tuple5[2]), 'tuple6[2]:', id(tuple6[2]))        # 地址不同，只要有可变类型子对象就拷贝
tuple5[2].append(2)
print(tuple5, tuple6)

# 结论：
# 如果发现元组里面有可变类型，会对元组以及可变子对象进行拷贝，拷贝后会产生新的内存空间
# 不可变类型不会对其拷贝，因为不可变类型不允许在原地址处修改，拷贝没有意义，因为每次修改数据内存地址会改变


# 对于可变类型：
list3 = [2, 5, [1, 9]]
list4 = copy.deepcopy(list3)
print('list3:', id(list3), 'list4:', id(list4))        # 地址不同
print('list3[1]:', id(list3[1]), 'list4[1]:', id(list4[1]))        # 地址相同
print('list3[2]:', id(list3[2]), 'list4[2]:', id(list4[2]))        # 地址不同
# 只拷贝可变类型
























