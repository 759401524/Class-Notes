# 第二章：numpy

## 认识Numpy数组对象


### 导入numpy包


```python
import numpy as np 
```

### 创建数组： 
#### 使用array函数从常规Python列表或元组中创建数组。

创建数组的最简单的办法就是使用array函数。接受一切序列型的对象（包括其他数组），然后产生一个新的含有传入数据的NumPy的数组。


```python
data1 = [5, 7, 9, 20]  # 列表
arr1 = np.array(data1)
arr1
```


```python
data2 = (5, 7, 9, 20)  # 元组
arr2 = np.array(data2)
arr2
```

Python 的元组与列表类似，不同之处在于元组的元素不能修改。
Python 集合（数组）Python 编程语言中有四种集合数据类型： 
+ 列表（List）是一种有序和可更改的集合。允许重复的成员。 
+ 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。 
+ 集合（Set）是一个无序和无索引的集合。没有重复的成员。 
+ 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

嵌套序列（比如一组等长列表组成的列表）将会被转换为一个多维数组


```python
data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]  # 多维数组
arr3 = np.array(data3)
arr3
```

一个 ndarray是具有相同类型和大小的项目的（通常是固定大小的）多维容器。 
每个数组都有一个shape（一个表示各维度大小的元组）和dtype（一个用于说明数组数据类型的对象）


```python
arr3.shape  # 查看数组的形状
```


```python
arr3.dtype  # 查看数据类型
```


```python
data4 = [1.2, 2, 3.45, 5]  # 创建数组
arr4 = np.array(data4)
arr4
```


```python
arr4.dtype  # 数据类型
```

可以在创建时显式指定数据类型


```python
x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)  # 创建int32类型多维数组
print(x)
type(x)
print(x.shape)
x.dtype
```

#### 通过内置函数创建

zeros、ones创建指定长度或形状的全0或全1的数组，函数empty 创建一个数组， 其初始内容是随机的，取决于内存的状态。
要用以上的方法创建数组，需传入一个表示形状的元组即可。arange创建数字组成的数组


```python
np.zeros(8)  # 创建八个为0的一维数组
```


```python
np.zeros((3, 4))  # 创建3x4的为0的一维数组
```


```python
np.ones(4)  # 创建4个为1的一维数组
```


```python
np.ones((4, 6))  # 创建4x6的为1的二维数组
```


```python
np.empty((2, 2, 2))  # 创建2x2x2的多维数组
```


```python
np.arange(10)  # 生成10个组数
```


```python
arr3  # 调用输出
```


```python
arr5 = np.ones_like(arr3)  #  创建全为1的数组，形状为arr3.shape
arr5
```


```python
arr5.dtype  # 数据类型
```


```python
data = [[2, 4, 5], [3, 5, 7]]  # 创建数组
arr = np.array(data)
arr
```

### 属性使用说明
 + .ndim 秩，即数据轴的个数。 
 + .shape 数组的维度。 
 + .size 元素的总个数。
 + .dtype 数据类型。
 + .itemsize 数组中每个元素的字节大小。


```python
arr.ndim  # arr数据轴的个数
```


```python
arr.size  # arr元素的总个数
```


```python
arr.itemsize  # arr数组中每个元素的字节大小
```


```python
arr.dtype  # 数据类型
```


```python
arr1 = np.arange(5)  # 生成数组
arr1
```


```python
arr1.dtype  # 数据类型
```


```python
arr2 = np.arange(5, dtype='float64')  # 生成float64数据类型的数组
arr2
```


```python
arr2.dtype  # 数据类型
```


```python
arr1 = np.arange(6)  # 生成数组
arr1
```

### 数据类型转换

NumPy中常用的数据类型、数组数据类型转换 astype()方法进行转换,调用astype总会创建一个新的数组


```python
arr1.dtype  # 数据类型
```


```python
arr2 = arr1.astype(np.float64)  # 数据类型转换
arr2
```


```python
var = arr2.dtype  # 输出数据类型
print(arr2.dtype)
```


```python
arr3 = arr1.astype('string_')  # 数据类型转换
arr3
```


```python
arr3.dtype  # 输出数据类型
print(arr3.dtype)
```


```python
arr = np.array([2.3, 7.5, 5.6, 9.8])  # 生成数组
arr
```


```python
arr.astype('int32')  # 数据类型转换
```


```python
arr3  # 输出arr3
```


```python
arr3.astype(np.int32)  # 数据类型转换
```


```python
arr = np.array(['2', 'hello'])  # 生成数组
arr
```


```python
# arr.astype('int32')
```


```python
arr1 = np.arange(10)  # 生成数组
arr1.dtype
```


```python
arr2 = np.ones(5)  # 生成5个为0的一维数组
arr2.dtype
```


```python
arr3 = arr1.astype(arr2.dtype)  # 数据类型转换
arr3.dtype
```


```python
arr = np.arange(3)  # 生成数组
arr.dtype
```


```python
arr.astype('float64')  # 数据类型转换
```


```python
arr
```

## 数组变换

重塑、合并、拆分、转置和轴对换

numpy.reshape 函数可以在不改变数据的条件下修改形状


```python
arr = np.arange(9)  # 生成数组
arr
```


```python
arr.reshape((3, 3))  # 改变数组形状变成3x3
```


```python
arr = np.array([[3, 4, 5], [1, 2, 3]])  # 生成数组并改变数组形状
arr.reshape((3, 2))
```


```python
arr = np.arange(12)  # 生成数组并改变数组形状
arr.reshape((3, -1))
# -1：维度自己计算
```


```python
arr = np.arange(10).reshape((5, 2))  # 生成数组并改变数组形状
arr
```

### 多维数组降位一维
numpy.flatten(),numpy.ravel()两者所要实现的功能是一致的（将多维数组降位一维）。 
 > 两者的区别在于返回拷贝（copy）还是返回视图（view），
 + numpy.flatten()返回一份拷贝，对拷贝所做的修改不会影响原始矩阵， 
 + numpy.ravel()返回的是视图，会影响原始矩阵。


```python
arr.ravel()  # 将多维数组转换为一维数组
```


```python
arr  # 多维数组
```


```python
arr.flatten()  # 将多维数组转换为一维数组
```


```python
arr
```


```python
arr1 = np.arange(12).reshape(3, 4)  # 生成数组并改变数组形状
arr1
```


```python
arr2 = np.arange(12, 24).reshape(3, 4)  # 生成数组并改变数组形状
arr2
```

高维数据执行某些操作（如转置）时， 需要指定维度编号，这个编号是从0开始的，然后依次递增1。 
其中，位于纵向的轴（y轴）的编号为0， 位于横向的轴（x轴）的编号为1，以此类推。

数组的连接
> 1.	concatenate 沿着现存的轴连接数据序列
2.	stack 沿着新轴连接数组序列
3.	hstack 水平堆叠序列中的数组(列方向)
4.	vstack 竖直堆叠序列中的数组(行方向)

numpy.concatenate
此函数用于沿指定轴连接相同形状的两个或多个数组。 该函数接受以下参数。
``` python
numpy.concatenate((a1, a2, ...), axis)

```

其中：
+ a1, a2, ...：相同类型的数组序列
+ axis：沿着它连接数组的轴，默认为 0


```python
np.concatenate([arr1, arr2], axis=0)  # 对数组arr1和arr2进行拼接（axis是对多维数组取值）
```


```python
np.concatenate([arr1, arr2], axis=1)  # 对数组arr1和arr2进行拼接（axis是对多维数组取值）

```

numpy.stack 
此函数沿新轴连接数组序列。 此功能添加自 NumPy 版本 1.10.0。 需要提供以下参数。

    numpy.stack(arrays, axis)

其中：

+ arrays：相同形状的数组序列
+ axis：返回数组中的轴，输入数组沿着它来堆叠

numpy.vstack

`numpy.stack` 函数的变体，通过堆叠来生成竖直的单个数组。


```python
np.vstack((arr1, arr2))  # 垂直堆叠数组
```

numpy.hstack 

`numpy.stack` 函数的变体，通过堆叠来生成水平的单个数组。


```python
np.hstack((arr1, arr2))  # 水平堆叠数组
```


```python
arr = np.arange(12).reshape((6, 2))  # 生成数组并改变数组形状
arr
```

数组分割
>1.	`split` 将一个数组分割为多个子数组
2.	`hsplit` 将一个数组水平分割为多个子数组(按列)
3.	`vsplit` 将一个数组竖直分割为多个子数组(按行)

`numpy.split`
该函数沿特定的轴将数组分割为子数组。函数接受三个参数：
    numpy.split(ary, indices_or_sections, axis)

其中：
+ ary：被分割的输入数组
+ indices_or_sections：可以是整数，表明要从输入数组创建的，等大小的子数组的数量。 如果此参数是一维数组，则其元素表明要创建新子数组的点。
+ axis：默认为 0


```python
np.split(arr, [2, 4])  # 将数组拆分为多个子数组。
```


```python
arr
```


```python
np.split(arr, 2, axis=1)  # 按列方向分割，分成2份
```


```python
np.split(arr, 3, axis=0)  # 按行方向分割，分成3份
```


```python
arr = np.arange(12).reshape(3, 4)
arr
```


```python
np.array_split(arr, 3, axis=1)  # 按列方向分割，分成3份
```

翻转操作

1.	transpose 翻转数组的维度
2.	ndarray.T 和self.transpose()相同
3.	rollaxis 向后滚动指定的轴
4.	swapaxes 互换数组的两个轴

numpy.transpose 这个函数翻转给定数组的维度。如果可能的话它会返回一个视图。

函数接受下列参数：
```python
numpy.transpose(arr, axes)
```
其中：

+ arr：要转置的数组
+ axes：整数的列表，对应维度，通常所有维度都会翻转。


```python
arr.transpose((1, 0))  # 0代表原来行维度，1代表列维度 行变成列，列变成行
```

numpy.ndarray.T 该函数属于ndarray类，行为类似于numpy.transpose


```python
arr.T  # 数组转置
```

numpy.swapaxes 该函数交换数组的两个轴。对于 1.10 之前的 NumPy 版本，会返回交换后数组的试图。

这个函数接受下列参数：
    
```python
  numpy.swapaxes(arr, axis1, axis2)
  
```

+ arr：要交换其轴的输入数组
+ axis1：对应第一个轴的整数
+ axis2：对应第二个轴的整数


```python
    arr = np.arange(16).reshape((2, 2, 4))
arr
```


```python
    arr.swapaxes(1, 2)
```

## 随机函数

```python
numpy.random.randint(low,high=None,size=None)
```
生成一个给定形状的离散随机数组(或单个随机数)， 随机数遵循离散均匀分布， 分布范围为[low,high)，若参数high为空，则分布范围为[0,low)。


```python
arr = np.random.randint(100, 200, size=(5, 4))  # 生成100-200之间5x4的随机数组
arr
```

```python
numpy.random.randn(d0,d1,d2,...,dn)
``` 

函数功能描述：生成一个给定形状的随机数组(或单个随机数)， 随机数遵循正态分布(即高斯分布)，分布在中心为0(即平均值为0)，方差为1。 

方差为各个数据与平均数之差的平方的和的平均数


```python
arr = np.random.randn(2, 3, 5)  # 生成2以内的 3x5的随机数组
arr
```

```python
normal(loc,scale,size)
```

产生具有正态分布的数组，loc均值，scale标准差


```python
arr = np.random.normal(4, 5, size=(3, 5))  # 生成3x5的高斯分布的概率密度随机数
arr
```


```python
arr = np.random.randint(100, 200, size=(5, 4))
arr
```

`numpy.random.shuffle(x)` 对X进行重排序，如果X为多维数组，只沿第一条轴洗牌，输出为None。 

`numpy.random.permutation(x)` 与`numpy.random.shuffle(x)`函数功能相同，

两者区别：`peumutation(x)`不会修改X的顺序。


```python
np.random.permutation(arr)  # 返回一个被洗过的数组
```


```python
arr
```


```python
# 当我们设置相同的seed，每次生成的随机数相同。如果不设置seed，则每次会生成不同的随机数
np.random.seed(0)

arr = np.random.randint(100, 200, size=(5, 4))
arr
```


```python
np.random.shuffle(arr)  # 原地洗数组，内容不变，无返回值
```


```python
arr
```

# 索引和切片
ndarray对象的内容可以通过索引或切片来访问和修改，与 Python 中 list 的切片操作一样。

ndarray 数组可以基于 0 - n 的下标进行索引，切片对象可以通过内置的 slice 函数，并设置 start, stop 及 step 参数进行，从原数组中切割出一个新数组。


```python
import numpy as np  # 调用包
```


```python
arr = np.arange(10)  # 生成数组
arr
```

对于一维数组来说，从表面上来看，它使用索引和切片的方式，与Python列表的功能相差不大


```python
arr[3]  # 索引
```


```python
arr[-1]  # 索引
```


```python
arr[2] = 123  # 将 123 赋值给 arr[2]
arr
```


```python
arr
```


```python
arr[3] = 88  # 将 88 赋值给 arr[3]
arr
```

冒号 : 的解释：如果只放置一个参数，如 [2]，将返回与该索引相对应的单个元素。 如果为 [2:]，表示从该索引开始以后的所有项都将被提取。 如果使用了两个参数，如 [2:7]，那么则提取两个索引(不包括停止索引)之间的项。


```python
arr1 = arr[-3:-1]  # 索引
arr1
```


```python
arr1[:] = 77  # 将 77 赋值给 arr1 的所有元素
arr1
```


```python
arr
```


```python
arr1 = arr[1].copy()  # 索引复制
arr1 = 34
arr
```


```python
arr = np.arange(15).reshape(3, 5)  # 生成数组并改变形状
arr
```

对于多维数组来说，索引和切片的使用方式与列表就大不一样了





```python
arr[0]  # 索引
```


```python
arr[2]  # 索引
```


```python
arr
```

如果想获取二维数组的单个元素，则需要通过形如“arr[x，y]”的索引来实现，其中x表示行号，y表示列号。


```python
arr[0][3]  # 索引
```


```python
arr[2, 3]  # 两种方法等价
```


```python
arr = np.arange(12).reshape(2, 2, 3)
arr
```


```python
arr[0]
```


```python
old = arr[0].copy()  # 索引并复制
arr[0] = 12
arr
```


```python
arr[0] = old  # 替换
arr
```


```python
arr
```


```python
arr[1, 1]
```


```python
arr[0, 1, 2]
```


```python
arr = np.arange(6)
arr
```


```python
arr[2:5]  # 索引
```


```python
arr = np.arange(12).reshape(4, 3)  # 生成数组
arr
```


```python
arr[2:]  # 索引切片
```


```python
arr
```

如果用两个花式索引操作数组，则会将第1个作为行索引，第2个作为列索引，以二维数组索引的方式选取其对应位置的元素。



```python
arr[:, 1]  # 切片
```


```python
arr[:, 1:2]  # 切片
```


```python
arr[2:, 1:]  # 切片
```

布尔型索引指的是将一个布尔数组作为数组索引，返回的数据是布尔数组中True对应位置的值。 布尔型数组可与切片，整数（整数序列）一起使用。

通过数组的逻辑运算来作为索引（实际上数组的逻辑运算的结果，也就是一个布尔数组）。假设我们有一个长度为7的字符串数组，然后对这个字符串数组进行逻辑运算，进而把元素的结果（布尔数组）作为索引的条件传递给目标数组


```python
fruits = np.array(
    ['apple', 'banana', 'pear', 'banana', 'pear', 'apple', 'pear'])  # 创建数组
datas = np.random.randint(-1, 1, size=(7, 5))
```


```python
fruits
```


```python
datas
```


```python
fruits == 'pear'  # 判断 fruits 数组中元素是否为 ‘pear’
```


```python
datas[fruits == 'pear']  # 布尔数组中，下标为2,4,6的位置是True，因此将会取出目标数组中第2,4,6行。
```


```python
datas[fruits != 'pear']  # 布尔数组中，下标为0,1,3,5的位置是True，因此将会取出目标数组中第0,1,3,5行。
```


```python
datas[(fruits == 'apple') | (fruits == 'banana')]
```


```python
datas[fruits == 'pear', 2:]
```


```python
datas[fruits == 'pear', 2]
```


```python
datas[datas == 0] = 1  # 将 datas 数组中元素值为 0 的赋值为 1
datas
```


```python
arr = np.arange(12).reshape(4, 3)
arr
```


```python
arr[[1, 3, 2]]  # 获取 arr 数组的第 1, 3, 2 行
```

花式索引指的是利用整数数组进行索引。 如果用两个花式索引操作数组，则会将第1个作为行索引，第2个作为列索引，以二维数组索引的方式选取其对应位置的元素。


```python
arr[[3, 2]][:, [2, 1]]  # 获取 arr 数组的第3, 2行,再取所获得的数组的第2, 1列
```


```python
arr[:, [2, 1]]  # 获取 arr 数组的第2, 1列
```


```python
arr[[3, 2], [2, 1]]  # arr[3,2]  arr[2,1]
```

`np.ix`函数，能把两个一维数组 转换为 一个用于选取方形区域的索引器 

    a[np.ix([1,3],[2,5])] 
returns the array `[[a[1,2] a[1,5]], [a[3,2] a[3,5]]]` 

`np.ix_`函数就是输入两个数组，产生笛卡尔积的映射关系


```python
print(np.ix_([3, 2], [2, 1]))  # 花式索引
```


```python
arr[np.ix_([3, 2], [2, 1])]  # 花式索引
```

数组的运算 数组与标量间的运算（元素级运算） 标量运算会产生一个与数组具有相同行和列的新矩阵，其原始矩阵的每个元素都被相加、相减、相乘或者相除。


```python
a = [1, 2, 3]  
b = []
for i in a:
    b.append(i * 10)  # 每个元素值×10
b
```


```python
arr = np.array([1, 2, 3])  # 每个元素值×10
arr * 10
```


```python
arr * arr  # 对应元素相乘
```


```python
arr - arr  # 对应元素相减
```

通用函数（ufunc）是一种针对ndarray中的数据执行元素级运算的函数，函数返回的是一个新的数组。 我们将ufunc中接收一个数组参数的函数称为一元通用函数，接受两个数组参数的则称为二元通用函数。


```python
arr = np.random.randn(3, 3)  # 生成标准正态分布的随机数
arr
```


```python
np.abs(arr)  # 返回数组中元素的绝对值
```


```python
np.square(arr)  # 计算各元素的平方 exp
```


```python
arr1 = np.random.randint(1, 10, size=(5))  # 生成随机整数
arr1
```


```python
arr2 = np.random.randint(1, 10, size=(5))  # 生成随机整数
arr2
```


```python
np.add(arr1, arr2)  # 给集合添加元素
```


```python
np.minimum(arr1, arr2)  # arr1和arr2对应位置元素进行比较，选取大的那个元素
```


```python
arr = np.random.normal(2, 4, size=(6, ))  # 生成高斯随机分布是随机数，
arr
```


```python
np.modf(arr)  # 返回arr的整数部分和小数部分
```


```python
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
cond = np.array([True, False, False, True])
```

zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象. 使用 list() 转换来输出列表 三元表达式x if condition else y


```python
zipped = zip(arr1, arr2, cond)  # 打包为元组的列表
list(zipped)
```


```python
result = [(x if c else y)
          for x, y, c in zip(arr1, arr2, cond)]  # if条件语句和for循环集合
result
```

NumPy的where()函数是三元表达式x if condition else y的矢量化版本。


```python
result = np.where(cond, arr1, arr2)  # 满足条件输出前者，不满足则输出后者
result
```


```python
arr = np.random.randn(4, 4)  # 生成4X4的标准正态分布随机数
arr
```


```python
new_arr = np.where(arr > 0, 1, -1)  # 满足条件输出前者，不满足则输出后者
new_arr
```


```python
arr = np.random.randint(1, 300, size=(3, 3))  # 生成1-300随机整数
arr
```


```python
new_arr = np.where(arr > 200, 3, np.where(arr > 100, 2,
                                          1))  # 满足条件输出前者，不满足则输出后者
new_arr
```

数组统计运算,数组的统计汇总


```python
arr = np.random.randn(4, 4)
arr
```


```python
arr.sum()  # arr求和
```


```python
arr.mean()  # 求取arr均值
```


```python
arr.std()  # 计算矩阵arr标准差
```


```python
arr
```


```python
arr.mean(axis=1)  # 沿行求取arr均值
```


```python
arr.sum(0)  # 沿列对元素求和
```


```python
arr = np.arange(9).reshape(3, 3)  # 创建数组并改变形状
arr
```


```python
arr.cumsum(0)  # 沿列 arr累加
```


```python
arr.cumprod(1)  # 沿行 arr累乘
```


```python
arr = np.random.randn(20)  # 从标准正态分布中返回多个样本值
arr
```


```python
(arr > 0).sum()  # true转换为1 ，false转换为0 
```


```python
arr = np.array([True, False, False, True])  # 创建数组
arr
```


```python
arr.any()  # any()函数用于判断整个数组中的元素至少有一个满足条件就返回True，否则就返回False。
```


```python
arr.all()  # all()函数用于判断整个数组中的元素的值是否全部满足条件，如果满足条件返回True，否则返回False。
```


```python
arr = np.random.randn(10)  # 从标准正态分布中返回多个样本值
arr
```


```python
arr.sort()  # 对原列表进行从小到大排序
arr
```


```python
arr = np.random.randn(5, 3)  # 从标准正态分布中返回多个样本值
arr
```


```python
arr.sort(1)  # 数组行内进行排序
arr
```


```python
fruits = np.array(
    ['apple', 'banana', 'pear', 'banana', 'pear', 'apple', 'pear'])  # 创建数组
fruits
```


```python
np.unique(fruits)  # 去除其中重复的元素，并按元素由大到小返回一个新的无元素重复的元组或者列表
```


```python
arr = np.array([2, 3, 3, 2, 8, 1])  # 创建数组
arr
```


```python
print(arr.argmin())  # 把 arr 平铺, 输出最小元素的索引
print(arr.argmax())  # 把 arr 平铺, 输出最大元素的索引
```


```python
np.unique(arr)  # 去除其中重复的元素，并按元素由大到小返回一个新的无元素重复的元组或者列表
```


```python
arr = np.array([2, 3, 5, 7])  # 生成数组
arr
```


```python
np.in1d(arr, [2, 7])  # in1d(x,y),x的元素是否在y中，返回布尔型数组
```


```python
arr = np.arange(12).reshape(4, 3)  # 生成数组并改变形状
arr
```


```python
np.savetxt('ch2ex1.csv', arr, fmt='%d', delimiter=',')  # 将 arr 数组保存为整数，以逗号分隔，名为ch2ex1.csv的文件
```


```python
!type ch2ex1.csv  # 打开ch2ex1.csv文件
```


```python
arr = np.loadtxt('ch2ex1.csv', delimiter=',')  # 获取ch2ex1.csv中的数据，以逗号分隔
arr
```


```python
arr1 = np.array([[1, 2, 3], [4, 5, 6]])  # 生成二维数组
arr1
```


```python
arr2 = np.arange(9).reshape(3, 3)  # 生成数组并改变形状
arr2
```


```python
np.dot(arr1, arr2)  # 将数组作为矩阵相乘
```


```python
from numpy.linalg import det  # 调用包
```

计算任何一个数组a的行列式


```python
arr = np.array([[1, 2], [3, 4]])  # 生成二维数组
arr
```


```python
det(arr)  # 计算arr的行列式
```
