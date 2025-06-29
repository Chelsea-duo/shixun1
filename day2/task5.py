# 1. 判断回文数
def is_palindrome(n):
    """判断一个数是否为回文数"""
    num_str = str(n)
    return num_str == num_str[::-1]

# 测试回文数函数
print("回文数测试:")
print(f"121 是回文数吗? {is_palindrome(121)}")  # True
print(f"123 是回文数吗? {is_palindrome(123)}")  # False
print(f"12321 是回文数吗? {is_palindrome(12321)}")  # True
print("-" * 50)

# 2. 计算任意数量参数的平均值
def average(*args):
    """计算任意数量参数的平均值"""
    if len(args) == 0:
        return 0  # 避免除以零错误
    return sum(args) / len(args)

# 测试平均值函数
print("平均值计算:")
print(f"(10, 20, 30) 的平均值: {average(10, 20, 30):.2f}")  # 20.00
print(f"(5, 10, 15, 20) 的平均值: {average(5, 10, 15, 20):.2f}")  # 12.50
print(f"单个值 100 的平均值: {average(100):.2f}")  # 100.00
print("-" * 50)

# 3. 返回最长字符串
def find_longest_string(*strings):
    """返回输入字符串中最长的一个"""
    if not strings:  # 检查是否为空
        return None
    return max(strings, key=len)

# 测试最长字符串函数
print("最长字符串查找:")
print(f"在 'apple', 'banana', 'cherry' 中最长的是: {find_longest_string('apple', 'banana', 'cherry')}")
print(f"在 'Python', 'Java', 'C++', 'JavaScript' 中最长的是: {find_longest_string('Python', 'Java', 'C++', 'JavaScript')}")

#4. 导入模块
from rectangle import area, perimeter

# 测试矩形计算
length = 5
width = 3

print(f"矩形面积 (长={length}, 宽={width}): {area(length, width)}")
print(f"矩形周长 (长={length}, 宽={width}): {perimeter(length, width)}")