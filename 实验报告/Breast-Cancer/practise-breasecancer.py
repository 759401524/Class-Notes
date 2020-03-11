#!/usr/bin/env python
# coding: utf-8
# 1、从本地读入数据，绘制良/恶性乳腺癌肿瘤测试集数据分布，良性肿瘤样本点标记为红色的Ο，恶性肿瘤样本点标记为黑色的×

import pandas as pd
test = pd.read_csv('breast-cancer-test.csv')
print(test.shape)
# print(test.loc[20:23, 'Clump Thickness': 'Cell Size'])

test_0 = test.loc[test['Type'] == 0][['Clump Thickness', 'Cell Size']]
print(test_0.shape)

test_1 = test.loc[test['Type'] == 1][['Clump Thickness', 'Cell Size']]
print(test_1.shape)

import matplotlib.pyplot as plt
from matplotlib import font_manager

font_set = font_manager.FontProperties(fname='c:/Windows/Fonts/simkai.ttf')

plt.scatter(test_0['Clump Thickness'], test_0['Cell Size'], marker='o', c='r')
plt.scatter(test_1['Clump Thickness'], test_1['Cell Size'], marker='x', c='k')
plt.title('良恶性可视化', fontproperties=font_set, fontsize=12)
plt.xlabel('肿瘤厚度', fontproperties=font_set, fontsize=12)
plt.ylabel('细胞大小', fontproperties=font_set, fontsize=12)
plt.show()
# 2、绘制随机参数下的二类分类器（用黄色直线表示），利用numpy中的random函数随机采样直线的截距和系数。

import numpy as np

a = np.random.random([2])
print(a)

b = np.random.random([1])
print(b)

x = np.arange(0, 12)
y = (-a[0]*x-b)/a[1]

plt.plot(x, y, 'y-')
plt.scatter(test_0['Clump Thickness'], test_0['Cell Size'], marker='o', c='r')
plt.scatter(test_1['Clump Thickness'], test_1['Cell Size'], marker='x', c='k')
plt.title('良恶性可视化', fontproperties=font_set, fontsize=12)
plt.xlabel('肿瘤厚度', fontproperties=font_set, fontsize=12)
plt.ylabel('细胞大小', fontproperties=font_set, fontsize=12)
plt.show()

train = pd.read_csv('breast-cancer-train.csv')
print(train.shape)
# 3、（选做）绘制利用10条训练样本得到的二类分类器（用绿色直线表示）。

from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(solver='liblinear')
lr.fit(train.head(10)[['Clump Thickness', 'Cell Size']], train.head(10)['Type'])
print(lr.coef_[0, :])
print(lr.intercept_)

coef = lr.coef_[0, :]
intercept = lr.intercept_
x = np.arange(0, 12)
y = (-coef[0] * x - intercept) / coef[1]

plt.plot(x, y, 'g-')
plt.scatter(test_0['Clump Thickness'], test_0['Cell Size'], marker='o', c='r')
plt.scatter(test_1['Clump Thickness'], test_1['Cell Size'], marker='x', c='k')
plt.title('良恶性可视化', fontproperties=font_set, fontsize=12)
plt.xlabel('肿瘤厚度', fontproperties=font_set, fontsize=12)
plt.ylabel('细胞大小', fontproperties=font_set, fontsize=12)
plt.show()
# 4、（选做）绘制使用所有训练样本得到的二类分类器（用蓝色直线表示）。

lr = LogisticRegression(solver='liblinear')
lr.fit(train[['Clump Thickness', 'Cell Size']], train['Type'])
print(lr.coef_[0, :])
print(lr.intercept_)

coef = lr.coef_[0, :]
intercept = lr.intercept_
x = np.arange(0, 12)
y = (-coef[0] * x - intercept) / coef[1]

plt.plot(x, y, 'b-')
plt.scatter(test_0['Clump Thickness'], test_0['Cell Size'], marker='o', c='r')
plt.scatter(test_1['Clump Thickness'], test_1['Cell Size'], marker='x', c='k')
plt.title('良恶性可视化', fontproperties=font_set, fontsize=12)
plt.xlabel('肿瘤厚度', fontproperties=font_set, fontsize=12)
plt.ylabel('细胞大小', fontproperties=font_set, fontsize=12)
plt.show()
