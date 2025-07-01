import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# 国家列表
countries = ['挪威', '德国', '中国', '美国', '瑞典']

# 奖牌个数
gold_medal = np.array([16, 12, 9, 8, 8])  # 金牌
silver_medal = np.array([8, 10, 4, 10, 5])  # 银牌
bronze_medal = np.array([13, 5, 2, 7, 5])  # 铜牌

# 设置X轴位置
x = np.arange(len(countries))

# 创建图形
plt.figure(figsize=(10, 6))

# 绘制条形图
plt.bar(x - 0.2, gold_medal, width=0.2, color='gold', label='金牌')
plt.bar(x, silver_medal, width=0.2, color='silver', label='银牌')
plt.bar(x + 0.2, bronze_medal, width=0.2, color='saddlebrown', label='铜牌')

# 设置X轴标签
plt.xticks(x, countries, fontsize=12)
plt.xlabel('国家', fontsize=12)
plt.ylabel('奖牌数量', fontsize=12)
plt.title('各国金银铜牌数量对比', fontsize=15)

# 添加图例
plt.legend(fontsize=10)

# 添加数据标签
for i in range(len(countries)):
    # 金牌标签
    plt.text(x[i] - 0.2, gold_medal[i], str(gold_medal[i]),
             va='bottom', ha='center', fontsize=10, fontweight='bold')

    # 银牌标签
    plt.text(x[i], silver_medal[i], str(silver_medal[i]),
             va='bottom', ha='center', fontsize=10, fontweight='bold')

    # 铜牌标签
    plt.text(x[i] + 0.2, bronze_medal[i], str(bronze_medal[i]),
             va='bottom', ha='center', fontsize=10, fontweight='bold')

# 调整布局
plt.tight_layout()

# 显示图形
plt.show()