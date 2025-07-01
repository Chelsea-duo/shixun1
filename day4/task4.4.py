import pandas as pd
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('D:/myproject_student/shixun1/day4/train (1).csv')

# 处理缺失值（用中位数填充）
data['Age'].fillna(data['Age'].median(), inplace=True)

# 划分10岁区间（0-10, 10-20, ..., 70-80）
bins = list(range(0, 81, 10))  # [0, 10, 20, ..., 80]
labels = [f'{i}-{i+10}' for i in range(0, 70, 10)] + ['70+']  # 最后一个区间改为"70+"

data['AgeGroup'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)
survival_by_age = data.groupby('AgeGroup')['Survived'].mean() * 100
plt.figure(figsize=(12, 6))
bars = plt.bar(survival_by_age.index, survival_by_age.values, color=plt.cm.viridis_r(range(len(survival_by_age))))

# 添加数值标签
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%', ha='center', va='bottom')

plt.title('Survival Rate by Age Group (10-year intervals)', fontsize=14)
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Survival Rate (%)', fontsize=12)
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.show()