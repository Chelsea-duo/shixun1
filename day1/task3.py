# 1. 使用列表推导式存储1-100的整数，输出所有偶数
numbers = [x for x in range(1, 101)]  # 生成1-100的整数列表
even_numbers = [num for num in numbers if num % 2 == 0]  # 筛选偶数
print("1-100之间的所有偶数：")
print(even_numbers)
print("-" * 50)

# 2. 删除列表中的重复元素并保持顺序不变
original_list = [3, 5, 2, 5, 7, 3, 8, 2, 9, 1, 5]
print(f"原始列表: {original_list}")

# 使用字典保持顺序删除重复元素（Python 3.7+ 字典保持插入顺序）
unique_list = list(dict.fromkeys(original_list))
print(f"删除重复元素后的列表: {unique_list}")
print("-" * 50)

# 3. 合并两个列表为字典
keys = ["a", "b", "c"]
values = [1, 2, 3]

# 使用zip函数合并两个列表
merged_dict = dict(zip(keys, values))
print(f"合并后的字典: {merged_dict}")
print("-" * 50)

# 4. 元组存储学生信息并解包
# 定义学生信息元组
student_info = ("张三", 18, 92.5)

# 解包元组
name, age, score = student_info

print(f"学生姓名: {name}")
print(f"学生年龄: {age}")
print(f"学生成绩: {score}")