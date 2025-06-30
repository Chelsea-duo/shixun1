import pandas as pd

# 读取CSV文件
file_path = r'C:\Users\朵\OneDrive\桌面\exercise_data\drinks.csv'
df = pd.read_csv(file_path)

# 1. 哪个大陆平均消耗的啤酒更多？
beer_by_continent = df.groupby('continent')['beer_servings'].mean()
max_continent = beer_by_continent.idxmax()
print(f"1. 平均啤酒消耗最多的大陆: {max_continent} ({beer_by_continent[max_continent]:.1f} 份)\n")

# 2. 每个大陆的红酒消耗描述性统计
wine_stats = df.groupby('continent')['wine_servings'].describe()
print("2. 每个大陆红酒消耗的描述性统计:")
print(wine_stats, "\n")

# 3. 每个大陆每种酒类别的消耗平均值
drink_types = ['beer_servings', 'spirit_servings', 'wine_servings']
avg_drinks = df.groupby('continent')[drink_types].mean()
print("3. 每个大陆每种酒类别的平均消耗:")
print(avg_drinks, "\n")

# 4. 每个大陆每种酒类别的消耗中位数
median_drinks = df.groupby('continent')[drink_types].median()
print("4. 每个大陆每种酒类别的消耗中位数:")
print(median_drinks)