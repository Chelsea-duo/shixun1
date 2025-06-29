# 大数据实训日志
*2025.6.29*
## 编程基础强化
今天系统学习了函数设计与参数传递机制，深入理解了"一个文件只能有一个主函数"的工程化编程规范。通过实际案例，我掌握了如何设计高内聚、低耦合的函数模块，这对构建可维护的大型项目至关重要。特别是在处理数据归一化时，学会了添加除数非零检查和数值范围限制，有效避免了程序运行时错误和内存溢出问题。
[python基础](https://www.notion.so/python-21e29eaba1c3800a821aff11badae198)
## 实用技能提升
Windows自然排序算法的学习解决了我在文件处理中长期遇到的排序混乱问题。通过开发文件批量重命名脚本，将理论转化为实践，成功实现了文档名称与文件系统的自动化匹配。由于图片的原命名中包含0，所以Windows自然排序算法的处理结果还存在一些问题，最后运用了一个特殊的sort算法，将数字按自然排序，但带前导零的数字排在相同值的数字之前解决了问题。这个过程中，我深刻体会到算法选择对实际应用效果的决定性影响。
```
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
```
## 技术文档规范化
Markdown笔记方法的系统学习让我的技术文档编写能力显著提升。掌握了代码块、表格、数学公式等专业排版技巧，使学习笔记和项目文档更加清晰易读。这种结构化记录方式大大提高了知识复盘和团队协作的效率。
[markdown语法](https://www.notion.so/markdown-21f29eaba1c380738a66c2455fd34e48)

## 数据分析核心工具
NumPy和Pandas库的深入学习是今日重点。通过创建多维数组、属性分析、索引切片和广播运算等练习，我掌握了向量化计算的核心思想。特别是在处理矩阵运算时，认识到广播机制如何优雅地解决维度不匹配问题，这将成为未来大数据处理的重要利器。

## 标准库应用实践
系统梳理了常用内置模块：
- math模块提供了高精度数学计算能力
- random模块满足各种随机化需求
- time/datetime模块解决了时间处理难题

通过对比实验，我发现datetime在时间戳转换和格式化输出上具有明显优势，这对日志分析和时间序列处理尤为重要。

# 学习心得
今天的实训将编程基础、算法思想和工程实践紧密结合。最大的收获是建立了防御性编程思维，在编写每个函数时都会考虑参数校验和异常处理。同时，通过文件重命名项目，我体会到自动化脚本对工作效率的倍增效应。在后续学习中，我将重点强化NumPy和Pandas的高阶应用，为即将开展的大数据分析项目打下坚实基础。
