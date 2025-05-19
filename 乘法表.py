# 控制金字塔的行数
for i in range(1, 6):
    # 打印空格，用于控制金字塔的形状，每一行的空格数随着行数增加而减少
    for j in range(5 - i):
        print(" ", end="")
    # 打印星号，每一行的星号数量是当前行数的两倍减1
    for k in range(2 * i - 1):
        print("*", end="")
    print()