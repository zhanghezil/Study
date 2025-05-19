# 定义变量名
age = 18
name = '竹竹'
height = 1.75

print('我的名字是：%s ，今年 %d 岁，身高 %f m' % (name, age, height))
# 小数默认显示6位，如果想要指定小数展示位数，需要在后面加一个小数点，然后在小数点后面指定小数位数
print('我的名字是：%s ，今年 %d 岁，身高 %.2f m' % (name, age, height))  # 两位小数
# %s可以占位任何类型的数据
print('我的名字是：%s ，今年 %s 岁，身高 %s m' % (name, age, height))  # 三位小数
stu_num = 1

print('我的学号是 %06d' % stu_num)
print('我的学号是 %6s' % stu_num)

num = 90
# 如果在格式化显示百分号，需要输入两个百分号
print('考试及格率 %d%%' % num)
