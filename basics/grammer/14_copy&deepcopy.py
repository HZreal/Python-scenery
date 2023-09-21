# 浅拷贝：
# 只会对可变类型的第一层进行拷贝，不会对子对象进行拷贝，拷贝成功会开批一个新的内存空间储存拷贝的这个对象
# 对不可变类型的浅拷贝，其实是拷贝了原数据的一个引用，不会开辟新的内存空间

# 深拷贝：
# 对不可变类型的深拷贝，同样是拷贝了原数据的一个引用，不会开辟新的内存空间
# 但只要发现对象有可变类型，那么就对该对象到最后一个可变类型的每一层对象进行拷贝，拷贝成功会开辟新的内存空间。如元祖套了个列表，子对象列表会被拷贝

# ps: 拷贝成功指的是分配一个新的内存空间存储拷贝的对象，拷贝失败通常说是拷贝的是原对象的一个引用


# 不管是深拷贝还是浅拷贝，都是针对可变类型的拷贝，只要拷贝成功就会开辟新的内存空间存储拷贝的对象。
# 对不可变类型拷贝的只是原对象的一个引用。
# 浅拷贝最多拷贝对象的一层，深拷贝可能拷贝对象的多层


# 不可变类型(不允许在原内存地址处修改)：数字，字符串，元组
# 可变类型(允许在原内存地址处修改)：列表，字典，集合

import copy


# 浅拷贝
# 对于不可变数据类型：
num1 = 10
num2 = copy.copy(num1)
print('num1内存地址：', id(num1))
print('num2内存地址：', id(num2))         # 地址相同，没有开辟新的内存空间，拷贝的是引用，指向的还是原地址空间

tuple1 = (4, 5, 8)
tuple2 = copy.copy(tuple1)
print('tuple1内存地址：', id(tuple1))
print('tuple2内存地址：', id(tuple2))      # 地址相同，没有开辟新的内存空间，拷贝的是引用，指向的还是原地址空间

# 结论：对于不可变类型的浅拷贝，其实是拷贝了原数据的一个引用，两个变量指向同一个内存地址


# 对于可变数据类型
list1 = [1, 3, 5, [2, 8]]
list2 = copy.copy(list1)
print('list1内存地址：', id(list1))
print('list2内存地址：', id(list2))           # 地址不同，拷贝后，开辟新内存地址进行存储
list1.append(9)
print(list1, list2)                         # list1被修改，list2依然不变，

print('list1[3]内存地址：', id(list1[3]))
print('list2[3]内存地址：', id(list2[3]))     # 地址相同，说明不会拷贝其子元素
list1[3].append(7)
print(list1, list2)                         # 修改list1的子元素时，list2的子元素也被修改

# 结论：
# 只会对可变类型的第一层进行拷贝，拷贝后的对象与原对象相互独立；但不会对子对象进行拷贝，子对象共享，其中一个子对象被修改，另一个子对象也同样改变


# 深拷贝
# 对于不可变类型的深拷贝，拷贝的还是引用
num3 = 12
num4 = copy.deepcopy(num3)
print('num3:', id(num3), 'num4:', id(num4))  # 地址相同

str1 = 'hello'
str2 = copy.deepcopy(str1)
print('str1:', id(str1), 'str2:', id(str2))  # 地址相同

tuple3 = (1, )
tuple4 = copy.deepcopy(tuple3)
print('tuple3:', id(tuple3), 'tuple4:', id(tuple4))  # 地址相同


# 不可变类型内部有可变类型(元祖内部含列表等)
tuple5 = (4, 2, [7, 5])
tuple6 = copy.deepcopy(tuple5)
print('tuple5:', id(tuple5), 'tuple6:', id(tuple6))  # 地址不同，注意：元祖及其子对象列表均被拷贝，开辟新空间
print('tuple5[1]:', id(tuple5[1]), 'tuple6[1]:', id(tuple6[1]))  # 地址相同,对不可变子对象不拷贝
print('tuple5[2]:', id(tuple5[2]), 'tuple6[2]:', id(tuple6[2]))  # 地址不同，只要有可变类型子对象就拷贝
tuple5[2].append(3)
print(tuple5, tuple6)                       # 由于可变子对象列表被拷贝，于是两者修改互不影响

tuple7 = (4, 2, {7, 5})
tuple8 = copy.deepcopy(tuple7)
print('tuple7:', id(tuple7), 'tuple8:', id(tuple8))      # 地址不同
print('tuple7[1]:', id(tuple7[1]), 'tuple8[1]:', id(tuple8[1]))   # 地址相同
print('tuple7[2]:', id(tuple7[2]), 'tuple8[2]:', id(tuple8[2]))   # 地址不同
tuple7[2].add(3)
print(tuple7, tuple8)              # 修改其一，另一不会随之改变

# 结论：
# 如果发现元组里面有可变类型，会对元组以及可变子对象进行拷贝，拷贝后会产生新的内存空间；对不可变子对象不拷贝。
# 不可变类型不会对其拷贝，因为不可变类型不允许在原地址处修改，拷贝没有意义，因为每次修改数据内存地址会改变


# 对于可变类型的深拷贝：        递归拷贝可变类型
list3 = [2, 5, [1, 9]]
list4 = copy.deepcopy(list3)
print('list3:', id(list3), 'list4:', id(list4))  # 地址不同
print('list3[1]:', id(list3[1]), 'list4[1]:', id(list4[1]))  # 子对象为不可变类型，不会拷贝或者说拷贝的是引用，地址相同
print('list3[2]:', id(list3[2]), 'list4[2]:', id(list4[2]))  # 子对象为可变类型，地址不同


##################################################################################################

# 列表的切片属于浅拷贝，只拷贝第一层，即第一层拷贝成功开辟新地址存储，与原对象无关，但内部可变对象不会拷贝，依然共享
lis1 = [1, 2, 4]
lis2 = [1, 2, [9, 5]]
_lis1 = lis1[:]
_lis2 = lis2[:]
lis1.append(7777)
lis2[2].append(8888)
print(lis1, _lis1)              # 修改其一，另一不变
print(lis2, _lis2)              # 修改其一内部可变对象，另一随之改变


# 列表的copy方法     -----------浅拷贝  shallow copy
list5 = [1, 'q']
list6 = list5.copy()
print('list5:', id(list5), 'list6:', id(list6))          # 拷贝成功，两者地址不同
list5.append(3)
print(list5, list6)


list7 = [1, 'q', (5, ), [3, 4]]
list8 = list7.copy()
print('list7:', id(list7), 'list8:', id(list8))          # 拷贝成功，两者地址不同
print('list7[2]:', id(list7[2]), 'list8[2]:', id(list8[2]))          # 两者地址相同，因为是浅拷贝，不会考虑子对象，当然即使是深拷贝地址也相同，因为这里是不可变类型
print('list7[3]:', id(list7[3]), 'list8[3]:', id(list8[3]))          # 两者地址相同。因为是浅拷贝，不会考虑子对象，即使这里为可变类型，不拷贝即共享地址空间
list7[3].append(111)
print(list7, list8)            # 修改其一，另一随之改变


# 字典的copy方法        -----------浅拷贝  shallow copy
dic1 = {'a': 1, '2': 2}
dic2 = dic1.copy()
print('dic1:', id(dic1), 'dic2:', id(dic2))            # 拷贝成功，两者地址不同
dic1['b'] = 3
print(dic1, dic2)                  # 修改其一，另一不会随之改变


dic3 = {'a': 1, '2': 2, 't': (1, ), 'l': [1, 'e']}
dic4 = dic3.copy()
print('dic3:', id(dic3), 'dic4:', id(dic4))            # 拷贝成功，两者地址不同
print('dic3["t"]:', id(dic3['t']), 'dic4["t"]:', id(dic4['t']))         # 地址相同，因为是浅拷贝
print('dic3["l"]:', id(dic3['l']), 'dic4["l"]:', id(dic4['l']))         # 地址相同，因为是浅拷贝
# dic3['t'] = (3, 222, )
# print(dic3, dic4)                  # 修改对象，另一对象不会随之改变
dic3['l'][0] = 5555
dic3['l'].append(8888)
print(dic3, dic4)                   # 修改其子对象，另一子对象随之改变

# 总结：
# 字典/列表的copy方法为浅拷贝，不会考虑子对象的拷贝，当前对象(字典/列表)为可变类型，于是拷贝成功，开辟新地址存储。于是这两个对象独立不影响，修改其一元素，另一不会随之改变
# 若其子对象中有可变类型，则此可变子对象不会拷贝，或者说拷贝的是其引用，又或者说此可变子对象被两个对象共享地址，于是修改这个可变子对象的元素，另一个随之改变


##################################################################################################

# 引用变量
a = [1, {'age': 10}]         # a为此列表的一个引用变量
b = a                        # b也为此列表的另一个引用变量，可以说a、b是两个指针
print(id(a), id(b))          # a、b两个变量均指向列表所在地址，故相同
# 对a、对b的修改都是操作原数据
a[1]['age'] = 12
# b[1]['age'] = 12

print(a, b, a == b)






