import os
import glob
import re

# 文件路径
txt_path = r"C:\Users\朵\OneDrive\桌面\新建文本文档.txt"
image_folder = r"C:\Users\朵\OneDrive\桌面\新建文件夹"

# 1. 读取文本文件中的姓名列表
with open(txt_path, 'r', encoding='utf-8') as file:
    names = [line.strip() for line in file.readlines() if line.strip()]

# 2. 获取文件夹中的所有图片文件
image_files = glob.glob(os.path.join(image_folder, '*.*'))


# 3. 实现特殊排序规则：数字按自然排序，但带前导零的数字排在相同值的数字之前
def natural_sort_key(s):
    """
    实现特殊排序规则：
    - 数字按数值大小排序（自然排序）
    - 带前导零的数字排在相同值的数字之前
    - 非数字部分按字母顺序排序（不区分大小写）
    """
    # 分割字符串为数字和非数字部分
    parts = re.split(r'(\d+)', s)

    # 处理每个部分
    key_parts = []
    for part in parts:
        if part.isdigit():
            # 数字部分：计算数值和是否有前导零
            num_val = int(part)
            has_leading_zero = len(part) > 1 and part.startswith('0')

            # 创建排序键：(数值, 是否有前导零, 原始字符串)
            key_parts.append((num_val, 0 if has_leading_zero else 1, part))
        else:
            # 非数字部分：按小写字母排序
            key_parts.append(part.lower())

    return key_parts


# 4. 按特殊规则排序
image_files.sort(key=lambda x: natural_sort_key(os.path.basename(x)))

# 5. 检查数量是否匹配
if len(names) != len(image_files):
    print(f"警告: 姓名数量({len(names)})与图片数量({len(image_files)})不匹配!")
    min_count = min(len(names), len(image_files))
    names = names[:min_count]
    image_files = image_files[:min_count]

# 6. 重命名图片
for i, (name, old_path) in enumerate(zip(names, image_files)):
    # 获取文件扩展名
    ext = os.path.splitext(old_path)[1]

    # 创建新文件名
    new_filename = f"{name}{ext}"
    new_path = os.path.join(image_folder, new_filename)

    # 重命名文件
    os.rename(old_path, new_path)
    print(f"重命名 {i + 1}/{len(image_files)}: {os.path.basename(old_path)} -> {new_filename}")

print("\n操作完成! 所有图片已按姓名重命名。")
print(f"已重命名 {len(image_files)} 张图片")