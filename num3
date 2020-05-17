
# 猜数字小组3 最小次数并写入文件 ：

import random
name = input('请输入你的名字： ')
time = 0  #次数
total =0  # 总轮数
min_count = 0  #最小轮数


while True:
    time +=1
    num = random.randint(1,100)
    count=0  # 此次轮数
    while True:
        ans = int(input('请猜一个 1 - 100 的数字 ：'))
        total +=1
        count +=1
        if ans >  num :
            print('%s, 你猜大了，再试试：' % name)
        elif ans <  num :
            print('%s, 你猜小了，再试试：' % name)
        else:
            print('%s, 你猜对了，一共猜了%d轮' % (name, count))
            break
    if min_count ==0 or min_count < count:
        min_count = count

    print('%s, 你一共玩了%d次，最少%d轮猜出答案,平均%d轮猜出答案”' % (name, time, min_count,total/time))      
    con=input('是否继续游戏？(输入y继续;其它退出)')
    if con != "y"  :   
        print('退出游戏，欢迎下次再来！')
        break
# 文件写入
lst=[0,0,0,0]
lst[0],lst[1],lst[2],lst[3]=name, time, min_count,total/time
result =[]
for i in lst:
    i=str(i)
    result.append(i)
    print(i)
    result.append('\n')
with open('game_one_user.txt','w',encoding='utf8') as f:
    f.writelines(result)


'''
1. 文件的写入的要素为字符串
2. 注意标识编码
'''




