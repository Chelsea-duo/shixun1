import pandas as pd
import os

# 设置文件路径
base_path = r'D:\myproject_student\shixun1\day3'
files = [
    '2015年国内主要城市年度数据.csv',
    '2016年国内主要城市年度数据.csv',
    '2017年国内主要城市年度数据.csv'
]

# 1. 读取并标准化所有数据
dfs = []
for file in files:
    file_path = os.path.join(base_path, file)

    # 读取CSV文件，处理BOM头和空格问题
    df = pd.read_csv(file_path, encoding='utf-8-sig')

    # 标准化列名：去除空格和不可见字符
    df.columns = df.columns.str.strip().str.replace('\u200b', '')

    # 确保所有数值列为float类型
    numeric_cols = [
        '国内生产总值', '第一产业增加值', '第二产业增加值', '第三产业增加值',
        '社会商品零售总额', '货物进出口总额', '年末总人口', '在岗职工平均工资',
        '普通高等学校在校学生数', '医院、卫生院数', '房地产开发投资额'
    ]

    for col in numeric_cols:
        if col in df.columns:
            # 处理可能存在的空字符串和特殊字符
            df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

    dfs.append(df)

# 2. 纵向连接所有DataFrame
merged_df = pd.concat(dfs, ignore_index=True)

# 3. 按照年份聚合并求每年的国内生产总值总和
yearly_gdp = merged_df.groupby('年份')['国内生产总值'].sum().reset_index()

# 4. 处理缺省值，填充为0
# 识别所有数值列
numeric_cols = merged_df.select_dtypes(include=['number']).columns
# 填充数值列的缺失值为0
merged_df[numeric_cols] = merged_df[numeric_cols].fillna(0)

# 5. 输出结果
print("=" * 50)
print("合并后的数据前5行：")
print(merged_df.head())
print("\n数据形状：", merged_df.shape)
print("\n列名：", merged_df.columns.tolist())

print("\n" + "=" * 50)
print("每年的国内生产总值总和：")
print(yearly_gdp)

print("\n" + "=" * 50)
print("缺省值处理后的数据统计信息：")
print(merged_df.describe())

# 可选：保存合并后的数据到新文件
output_path = os.path.join(base_path, '2015-2017_合并数据.csv')
merged_df.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n合并数据已保存至: {output_path}")