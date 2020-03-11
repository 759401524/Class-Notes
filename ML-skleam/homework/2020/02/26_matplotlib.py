# coding:utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

# matplotlib默认不支持中文字符，设置中文字体，参数的值为系统字体路径
my_font = font_manager.FontProperties(fname=r"c:\windows\fonts\simsun.ttc")

# 需要绘制的数据
x = ['1.30', '1.31', '2.1', '2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', ]
y_confirm = [9720, 11821, 14411, 17238, 20471, 24363, 28060, 31211, 34598, 37251]
y_doubt = [15238, 17988, 19544, 21558, 23214, 23260, 24702, 26359, 27657, 28942]

# 绘制第一条折线
plt.plot(x, y_confirm, label="确诊数", color="red", marker="o")

# 绘制第二条折线
plt.plot(x, y_doubt,
         label="疑似数",  # 图例显示内容
         color="orange",  # 线条颜色
         marker='o',
         linestyle="--")  # 线条样式
# 设置x轴刻度，rotation为旋转度数
plt.xticks(x[::], rotation=45)

# 设置图例，prop为设置字体，fontsize为设置字体大小
plt.legend(prop=my_font, fontsize=12)

# 绘制网格，alpha,明度
plt.grid(alpha=0.5)

# 添加描述信息，fontproperties为设置字体，fontsize为设置字体大小
plt.xlabel("日期", fontproperties=my_font, fontsize=12)
plt.ylabel("人数（人）", fontproperties=my_font, fontsize=12)
plt.title("全国累计确诊/疑似数", fontproperties=my_font, fontsize=18)

# 显示图形
plt.show()
