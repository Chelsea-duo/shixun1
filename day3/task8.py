import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 设置图形大小
plt.figure(figsize=(8, 6))

# 生成x值范围（-5到5之间，包含100个点）
x = np.linspace(-5, 5, 100)

# 计算y = x^3
y = x ** 3

# 绘制曲线
plt.plot(x, y, label='y = x³', color='blue', linewidth=2)

# 添加标题和标签
plt.title('x^3的图像', fontsize=14)
plt.xlabel('x', fontsize=12)
plt.ylabel('y', fontsize=12)

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图例
plt.legend(fontsize=12)

# 设置坐标轴范围
plt.xlim(-5, 5)
plt.ylim(-125, 125)

# 显示图形
plt.show()



# 生成年份数组（2000-2020）
year = np.arange(2000, 2021).astype(np.str_)

# 随机生成月份和日期
month = np.random.randint(1, 13, size=20).astype(np.str_)
day = np.random.randint(1, 31, size=20).astype(np.str_)

# 组合年月日形成日期字符串
date = np.array([])
for i in range(20):
    a = np.array([year[i], month[i], day[i]])
    b = '/'.join(a)  # 组合年月日
    date = np.append(date, b)

# 随机生成销量数据
sales = np.random.randint(500, 2000, size=len(date))

# 绘制图形
plt.figure(figsize=(10, 6))  # 设置图形大小

# 绘制折线图
plt.plot(date, sales, marker='o', linestyle='-', color='blue')

# 设置x轴刻度（每隔2个日期显示一个）
plt.xticks(range(0, len(date), 2),
           [f'日期:{i}' for i in date][::2],
           rotation=45,
           color='red')

# 添加标题和标签
plt.title('2000-2020年随机销量数据', fontsize=14)
plt.xlabel('日期', fontsize=12)
plt.ylabel('销量', fontsize=12)

# 显示网格
plt.grid(True, linestyle='--', alpha=0.6)

# 自动调整布局
plt.tight_layout()

# 显示图形
plt.show()