import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.font_manager import FontProperties
# ===== 1. 自定义字体配置 =====
font_path = 'D:/myproject_student/shixun1/day4/simhei.ttf'
font_prop = FontProperties(fname=font_path)


df = pd.read_csv('D:/myproject_student/shixun1/day4/train (1).csv')

# 1. 处理缺失值
df['Age'].fillna(df['Age'].median(), inplace=True)

# 2. 创建年龄分段
bins = [0, 12, 30, 50, 100]
labels = ['儿童(<12)', '青年(12-30)', '中年(30-50)', '老年(50+)']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

# 3. 按性别分析生还率
gender_survival = df.groupby('Sex')['Survived'].mean() * 100

# 4. 按性别和年龄分组分析
grouped = df.groupby(['Sex', 'AgeGroup'])['Survived'].mean().reset_index()


# 全局字体设置
plt.rcParams['font.family'] = font_prop.get_name()
plt.rcParams['axes.unicode_minus'] = False
# 设置绘图风格
#sns.set_style('whitegrid')
plt.figure(figsize=(14, 10))

# 5. 绘制性别生还率对比图
plt.subplot(2, 2, 1)
gender_survival.plot(kind='bar', color=['hotpink', 'dodgerblue'])
plt.title('不同性别生还率对比', fontsize=14)
plt.ylabel('生还率 (%)')
plt.ylim(0, 100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 添加数据标签
for i, v in enumerate(gender_survival):
    plt.text(i, v + 3, f'{v:.1f}%', ha='center', fontsize=12)

# 6. 绘制性别+年龄组生还率
plt.subplot(2, 2, 2)
sns.barplot(x='AgeGroup', y='Survived', hue='Sex', data=grouped,
           palette={'female': 'hotpink', 'male': 'dodgerblue'})
plt.title('性别与年龄组生还率', fontsize=14)
plt.ylabel('生还率')
plt.xlabel('年龄组')
plt.ylim(0, 1)
plt.legend(title='性别')

# 7. 绘制年龄分布直方图
plt.subplot(2, 2, 3)
sns.histplot(data=df, x='Age', hue='Survived', bins=20,
            palette={0: 'gray', 1: 'green'}, kde=True)
plt.title('年龄分布与生还情况', fontsize=14)
plt.xlabel('年龄')
plt.ylabel('人数')
plt.legend(['遇难', '生还'])

# 8. 绘制年龄与生还率关系图
plt.subplot(2, 2, 4)
sns.lineplot(data=df, x='Age', y='Survived', ci=None)
plt.title('年龄与生还率关系', fontsize=14)
plt.ylabel('生还率')
plt.xlabel('年龄')
plt.ylim(0, 1)
plt.axvline(18, color='red', linestyle='--', alpha=0.5)
plt.text(19, 0.8, '儿童/成人分界', color='red')

plt.tight_layout()
plt.savefig('titanic_survival_analysis.png', dpi=300)
plt.show()

# 9. 关键数据输出
print("\n=== 关键统计数据 ===")
print(f"整体生还率: {df['Survived'].mean()*100:.1f}%")
print(f"女性生还率: {gender_survival['female']:.1f}%")
print(f"男性生还率: {gender_survival['male']:.1f}%")
print("\n各年龄组生还率:")
print(grouped.pivot(index='AgeGroup', columns='Sex', values='Survived'))