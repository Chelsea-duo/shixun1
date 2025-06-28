# 1. 输出1到100之间的所有素数
print("1到100之间的所有素数：")
for num in range(2, 101):  # 2是最小的素数
    is_prime = True
    # 检查是否能被2到num-1之间的数整除
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=' ')  # 输出素数，用空格分隔
print("\n" + "-"*50)  # 分隔线

# 2. 计算斐波那契数列的前20项
print("斐波那契数列前20项：")
fibonacci = [0, 1]  # 初始化前两项

# 生成剩余的18项
for i in range(2, 20):
    next_num = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(next_num)

# 打印结果，每行5个数字
for i in range(0, 20, 5):
    print(' '.join(f"{num:>5}" for num in fibonacci[i:i+5]))
print("-"*50)  # 分隔线

# 3. 使用while循环计算符合条件的数的和
total = 0
num = 1
while num <= 10000:
    # 检查条件：能被3整除 或 (能被5整除且不能被15整除)
    if (num % 3 == 0) or (num % 5 == 0 and num % 15 != 0):
        total += num
    num += 1

print(f"1-10000之间符合条件的数的和为：{total}")