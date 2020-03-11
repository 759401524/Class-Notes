```python
import numpy as np
# 1、创建从0到9的一维数组
a = np.arange(10)
print(a)

# 2、创建一个3×3的二维数组，值域为0到8
a = np.arange(9).reshape(3, 3)
print(a)

# 3、将一维数组np.arange(10)转换为2行的二维数组
a = np.arange(10)
b = a.reshape(2, -1)
print(b)

# 4、将数组a = np.arange(10).reshape(2,-1)和数组b = np.repeat(1, 10).reshape(2,-1)垂直堆叠
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.vstack((a, b))
print(c)

# 5、将数组a = np.arange(10).reshape(2,-1)和数组b = np.repeat(1, 10).reshape(2,-1)水平堆叠
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
c = np.hstack((a, b))
print(c)

# 6、找到二维数组np.arange(9).reshape(3,3)每一行中的最大值
a = np.arange(9).reshape(3, 3)
b = np.max(a, axis=1)
print(b)
```