score = int(input("请输入："))
if score >=90:
    print('优')
if score<90 and score>=80:
    print('良')
if score<80 and score>=70:
    print('中')
if score<70 and score>=60:
    print('及格')
if score<60:
    print('不及格')