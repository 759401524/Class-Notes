# -*- coding: utf-8 -*-
# @Time : 2019-12-11 15:36
# @Author : dml19
# 假设一个班有50个学生，随机产生50个1-100之间的整数分别作为50个学生的考试成绩分数。
# （1）	将所有的成绩打印显示出来。
# （2）	计算所有为素数的分数的总和并打印显示出来。
# （3）	90分以上（含90分）等级为优秀，80分以上（含80分）而且低于90分等级为良好，
# 70分以上（含70分）而且低于80分等级为中等，60分以上（含60分）而且低于70分等级为及格，
# 低于60分等级为不及格，统计这些随机产生的分数中五个等级的人数并打印显示出来。
import random

randnum = [random.randint(1, 100) for i in range(50)]

# 将所有的成绩打印显示出来。
print('所有的分数为：', end='')
for i in randnum:
	print(i, end=" ")
print()

# 计算所有为素数的分数的总和并打印显示出来。
sum1 = 0
for i in randnum:
	for j in range(2, int(i ** 0.5)):
		if i % j == 0:
			break
	else:
		sum1 += i
print('素数的和为{}'.format(sum1))

# 统计这些随机产生的分数中五个等级的人数并打印显示出来
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
for i in randnum:
	if i < 60:
		count1 += 1
	elif i < 70:
		count2 += 1
	elif i < 80:
		count3 += 1
	elif i < 90:
		count4 += 1
	else:
		count5 += 1
print('优秀的有{}人，良好的有{}人，中等的有{}人，及格的有{}人，不及格的有{}人'.format(count5, count4, count3, count2, count1))
