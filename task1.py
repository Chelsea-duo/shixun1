# 1. 判断变量 x = 10, y = "10", z = True 的数据类型并输出。
# 2. 接收用户输入的半径，输出圆的面积，π定义为3.14。
# 3. 将字符串 "3.14" 转换为浮点数，再转换为整数，观察结果差异。

# 1. 判断变量数据类型
x = 10
y = "10"
z = True
print(f"x 的数据类型是：{type(x)}")  # <class 'int'>
print(f"y 的数据类型是：{type(y)}")  # <class 'str'>
print(f"z 的数据类型是：{type(z)}")  # <class 'bool'>

# 2. 计算圆面积
π = 3.14
radius = float(input("请输入圆的半径："))
area = π * (radius ** 2)
print(f"半径为 {radius} 的圆面积为：{area:.2f}")

# 3. 类型转换观察
str_value = "3.14"
float_value = float(str_value)  # 字符串转浮点数
int_value = int(float_value)    # 浮点数转整数

print(f"\n原始字符串值：{str_value} (类型: {type(str_value)})")
print(f"转换为浮点数：{float_value} (类型: {type(float_value)})")
print(f"转换为整数：{int_value} (类型: {type(int_value)})")