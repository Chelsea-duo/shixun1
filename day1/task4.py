# 1. 给定字符串 s1 的操作
s1 = "Python is a powerful programming language"

# (1) 提取单词 "language"
words = s1.split()  # 以空格分隔单词
last_word = words[-1]  # 获取最后一个单词
print(f"(1) 最后一个单词是: {last_word}")

# (2) 连接 s1 和 s2 并重复输出 3 次
s2 = " Let's learn together"
combined = s1 + s2
print("(2) 连接并重复3次:")
print(combined * 3)

# (3) 输出所有以 p 或 P 开头的单词
p_words = [word for word in words if word.lower().startswith('p')]
print(f"(3) 以p或P开头的单词: {p_words}")

print("\n" + "="*50 + "\n")  # 分隔线

# 2. 对字符串 s3 的操作
s3 = " Hello, World! This is a test string. "

# (1) 去除字符串前后的空格
trimmed = s3.strip()
print(f"(1) 去除前后空格: '{trimmed}'")

# (2) 将所有字符转换为大写
uppercase = s3.upper()
print(f"(2) 转换为大写: '{uppercase}'")

# (3) 查找子串 "test" 的起始下标
test_index = s3.find("test")
print(f"(3) 'test'子串起始下标: {test_index}")

# (4) 将 "test" 替换为 "practice"
replaced = s3.replace("test", "practice")
print(f"(4) 替换后: '{replaced}'")

# (5) 以空格分割字符串并用 "-" 连接
split_words = s3.split()  # 以空格分割
joined = "-".join(split_words)  # 用连字符连接
print(f"(5) 分割并连接: '{joined}'")