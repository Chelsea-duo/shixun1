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


# 3. 使用Windows自然排序算法对文件进行排序
def natural_sort_key(s):
    """
    生成用于自然排序的键值
    将文件名中的数字部分转换为整数，非数字部分保留为字符串
    """
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(r'(\d+)', s)]


# 按Windows资源管理器的排序方式排序
image_files.sort(key=lambda x: natural_sort_key(os.path.basename(x)))

# 4. 检查数量是否匹配
if len(names) != len(image_files):
    print(f"警告: 姓名数量({len(names)})与图片数量({len(image_files)})不匹配!")
    # 取最小数量继续操作
    min_count = min(len(names), len(image_files))
    names = names[:min_count]
    image_files = image_files[:min_count]

# 5. 重命名图片
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