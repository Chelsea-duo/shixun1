import pandas as pd
import numpy as np

# 1. 创建包含指定数据的DataFrame
data = {
    'Student_ID': [101, 102, 103, 104, 105],
    'Name': ['Alice', 'Bob', None, 'David', 'Eva'],
    'Score': [85, 92, 78, np.nan, 88],
    'Grade': ['A', 'A', 'B', 'C', 'B']
}

df = pd.DataFrame(data)

# 保存为CSV文件（不包含索引列）
df.to_csv('students.csv', index=False)
print("students.csv文件已创建\n")

# 2. 读取CSV文件并打印前3行
students_df = pd.read_csv('students.csv')
print("前3行数据：")
print(students_df.head(3))
print("\n")

# 3. 处理缺失值（避免inplace警告的写法）
# 计算Score列的平均分
score_mean = students_df['Score'].mean()

# 创建填充字典
fill_values = {
    'Score': score_mean,
    'Name': 'Unknown'
}

# 一次性填充所有缺失值（推荐写法）
students_df = students_df.fillna(fill_values)

print("处理缺失值后的数据：")
print(students_df)
print("\n")

# 4. 将处理后的DataFrame保存为新CSV文件
students_df.to_csv('students_cleaned.csv', index=False)
print("处理后的数据已保存为students_cleaned.csv")