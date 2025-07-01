import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 读取数据
data = pd.read_csv('D:/myproject_student/shixun1/day4/train (1).csv')

# 计算各等级的生还率
survival_by_class = data.groupby('Pclass')['Survived'].mean() * 100

# 绘制直方图
plt.figure(figsize=(8, 6))
bars = plt.bar(survival_by_class.index, survival_by_class.values, color=['gold', 'silver', 'brown'])

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%', ha='center', va='bottom')

plt.title('Survival Rate by Passenger Class', fontsize=14)
plt.xlabel('Passenger Class', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.xticks([1, 2, 3], labels=['1st Class', '2nd Class', '3rd Class'])
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()