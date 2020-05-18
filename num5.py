
'''
Guess Number5 many users

字典的用法还是不熟练
'''

import random #引入模块

name = str(input('Input your name：'))  

# 读取文件
f=open('game_many_user.txt','r',encoding='utf8')  # 由于姓名可能为中文，存在编码问题，所以要加上参数 encoding
lst_B = f.readlines()
f.close

dic_B={}
for A in lst_B:
    data = A.strip().split()  #处理换行符及空格的问题
    #print(data[0],data[1:],data)   
    dic_B[data[0]]=data[1:]  #生成字典
    #print(dic_B)

#这个判断很重要，涉及到更新
score = dic_B.get(name)
if score == None:
    score = [0,0,0]

game_times = int(score[0]) # 总游戏次数
min_times = int(score[1]) # 最快猜出的轮数
total_times = int(score[2]) # 猜过的总轮数

##补充-crossin
if game_times>0:
    ave_times = total_times / game_times
else:
    ave_times = 0

print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏！' % (
    name, game_times, min_times, ave_times
))



while True:
    game_times +=1
    num = random.randint(1,100)
    time=0  # 此次轮数
    while True:
        ans = int(input('请猜一个 1 - 100 的数字 ：'))
        total_times +=1
        time +=1
        if ans >  num :
            print('%s, 你猜大了，再试试：' % name)
        elif ans <  num :
            print('%s, 你猜小了，再试试：' % name)
        else:
            print('%s, 你猜对了，一共猜了%d轮' % (name, time))
            break
        
    if min_times ==0 or time < min_times:
        min_times = time
        
    ave_times = total_times/game_times

    print('%s, 你一共玩了%d次，最少%d轮猜出答案,平均%d轮猜出答案' % (name, game_times,min_times,ave_times))      
    con=input('是否继续游戏？(输入y继续;其它退出)')
    if con != "y"  :   
        print('退出游戏，欢迎下次再来！')
        break

dic_B[name]=[str(game_times),str(min_times),str(ave_times)]
print(dic_B)

result = ''
for n in dic_B:
    A = n+' '+' '.join(dic_B[n]) + '\n'
    result +=A
    print(result)
f=open('game_many_user.txt', 'w', encoding='utf8')
f.write(result)
f.close()





    
