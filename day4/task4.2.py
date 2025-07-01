import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 设置文件路径
file_path = r'D:\myproject_student\shixun1\day3\2015-2017_合并数据.csv'

# 读取数据
df = pd.read_csv(file_path, encoding='utf-8-sig')

# 1. 绘制2015-2017年各个城市的国内生产总值直方图
plt.figure(figsize=(18, 10))

# 获取所有城市列表
cities = df['地区'].unique()
years = [2015, 2016, 2017]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']  # 蓝、橙、绿

# 设置条形宽度和位置
bar_width = 0.25
x = np.arange(len(cities))

# 绘制每个年份的条形图
for i, year in enumerate(years):
    year_data = df[df['年份'] == year].sort_values(by='地区')['国内生产总值']
    plt.bar(x + i * bar_width, year_data, width=bar_width,
            color=colors[i], label=f'{year}年')

# 设置图表标题和标签
plt.title('2015-2017年各城市国内生产总值对比', fontsize=16)
plt.xlabel('城市', fontsize=14)
plt.ylabel('国内生产总值 (亿元)', fontsize=14)
plt.xticks(x + bar_width, cities, rotation=45, ha='right', fontsize=10)
plt.legend(fontsize=12)

# 添加网格线
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 调整布局
plt.tight_layout()
plt.savefig(os.path.join(r'D:\myproject_student\shixun1\day3', '各城市GDP对比直方图.png'))
plt.show()

# 2. 绘制2015年各个城市的国内生产总值饼状图
plt.figure(figsize=(14, 14))

# 获取2015年数据并按GDP排序
df_2015 = df[df['年份'] == 2015].sort_values('国内生产总值', ascending=False)

# 计算前10大城市的GDP占比
top_10 = df_2015.head(10)
other_gdp = df_2015['国内生产总值'][10:].sum()
other_row = pd.DataFrame([['其他城市', 2015, other_gdp] + [0]*10], columns=df_2015.columns)
pie_data = pd.concat([top_10, other_row])

# 设置颜色
colors = plt.cm.tab20c(np.linspace(0, 1, len(pie_data)))

# 绘制饼图
plt.pie(pie_data['国内生产总值'],
        labels=pie_data['地区'],
        autopct='%1.1f%%',
        startangle=90,
        colors=colors,
        textprops={'fontsize': 10},
        pctdistance=0.85)

# 添加标题
plt.title('2015年各城市国内生产总值占比', fontsize=16)

# 添加中心空白圆环，使成甜甜圈图效果
centre_circle = plt.Circle((0,0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# 添加图例
plt.legend(pie_data['地区'], loc="best", bbox_to_anchor=(1, 0.5), fontsize=10)

# 确保饼图为正圆
plt.axis('equal')

# 保存并显示
plt.tight_layout()
plt.savefig(os.path.join(r'D:\myproject_student\shixun1\day3', '2015年各城市GDP占比饼图.png'))
plt.show()