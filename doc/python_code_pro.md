# Python代码小优化

有必要进行一定的代码优化来提高 Python 程序的执行效率

1. 尽量使用内置函数，效率高

2. 拼接字符串，建议用 %  format  而不是 + (内存会先创建一个新字符串，然后将两个旧字符串拼接，再复制到新字符串。)

3. 生成器，非常棒的特性。大大节省内存空间。

4. 死循环  虽然使用While True和while 1都能实现死循环，但是while 1是单步运算，所以效率会高一点。

5. bisect 模块是内置模块，它实现了一个算法用于插入元素到有序列表。在一些情况下，这比反复排序列表或构造一个大的列表再排序的效率更高。

6. 尽量使用局部变量，定义在全局范围内的代码运行速度会比定义在函数中的慢不少。

7. 避免模块和函数属性访问。每次使用.（属性访问操作符时）会触发特定的方法，如__getattribute__()和__getattr__()，这些方法会进行字典操作，因此会带来额外的时间开销。

   ```python
   import math
   math.sqrt(4)   #  math.操作取函数sqrt，触发了一些特定方法，带来开销
   from math import sqrt
   sqrt(4)        # 更快
   
   def computeSqrt(size: int):
       result = []
       sqrt = math.sqrt  # 若频繁访问math.sqrt，可将其设置成局部变量，局部变量的查找会比全局变量更快。
       for i in range(size):
           result.append(sqrt(i))  # 避免math.sqrt的使用
       return result
   ```

8. 避免`.`的原则也适用于类内属性，访问`self._value`的速度会比访问一个局部变量更慢一些。通过将需要频繁访问的类内属性赋值给一个局部变量，可以提升代码运行速度。

   ```python
   user_id = user_obj.id
   func1(user_id)      # 多处使用user对象的id值，可以用局部变量存起来
   func2(user_id)
   ...
   ```

9. **避免不必要的抽象**。任何时候当你使用额外的处理层（比如装饰器、属性访问、描述器）去包装代码时，都会让代码变慢。

10. **避免数据复制**。
    1. **避免无意义的数据复制**
    2. 对 Python 的数据共享机制过于偏执，并没有很好地理解或信任 Python 的内存模型，滥用 `copy.deepcopy()`之类的函数。通常在这些代码中是可以去掉复制操作的。
    3. **交换值时不使用中间变量**
    4. **字符串拼接用join而不是+** 当使用`a + b`拼接字符串时，由于 Python 中字符串是不可变对象，其会申请一块内存空间，将`a`和`b`分别复制到该新申请的内存空间中。因此，如果要拼接 n 个字符串，会产生 n-1 个中间结果，每产生一个中间结果都需要申请和复制一次内存，严重影响运行效率。而使用`join()`拼接字符串时，会首先计算出需要申请的总的内存空间，然后一次性地申请所需内存，并将每个字符串元素复制到该内存中去。
11. **利用if条件的短路特性**

`if` 条件的短路特性是指对`if a and b`这样的语句， 当`a`为`False`时将直接返回，不再计算`b`；

对于`if a or b`这样的语句，当`a`为`True`时将直接返回，不再计算`b`。

为了节约运行时间，对于`or`语句，应该将值为`True`可能性比较高的变量写在`or`前，而`and`应该推后。

12. **循环优化**

    1. **用for循环代替while循环**  `for`循环比`while`循环快不少

    2. 可以用隐式`for`循环来替代显式`for`循环

       ```py
       for i in range(size):  
               sum_ += i
       可改为如下：
       sum(range(size))  # 隐式 for 循环代替显式 for 循环
       ```

    3. **减少内层for循环的计算**

13. **使用numba.jit**

    `numba`可以将 Python 函数 JIT 编译为机器码执行，大大提高代码运行速度。关于`numba`的更多信息见下面的主页：http://numba.pydata.org/numba.pydata.org

14.  **选择合适的数据结构**

    Python 内置的数据结构如`str`, `tuple`, `list`, `set`, `dict`底层都是 C 实现的，速度非常快，自己实现新的数据结构想在性能上达到内置的速度几乎是不可能的。

    1. `list`类似于 C++ 中的`std::vector`，是一种动态数组。其会预分配一定内存空间，当预分配的内存空间用完，又继续向其中添加元素时，会申请一块更大的内存空间，然后将原有的所有元素都复制过去，之后销毁之前的内存空间，再插入新元素。
    2. 如果有频繁的新增、删除操作，新增、删除的元素数量又很多时，list的效率不高。此时，应该考虑使用`collections.deque`。`collections.deque`是双端队列，同时具备栈和队列的特性，能够在两端进行 O(1) 复杂度的插入和删除操作。

    2. `list`的查找操作也非常耗时。当需要在`list`频繁查找某些元素，或频繁有序访问这些元素时，可以使用`bisect`维护`list`对象有序并在其中进行二分查找，提升查找的效率。
    3. 一个常见需求是查找极小值或极大值，此时可以使用`heapq`模块将`list`转化为一个堆，使得获取最小值的时间复杂度是 O(1)。