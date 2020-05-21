'''
Guess Number 6


Note：
1. 安装是在终端
'''
import random #引入random模块
import requests #引入requests模块

# 一次游戏是一个函数，返回值times代表用户一次游戏猜的轮数
def one_game():
    url = 'https://python666.cn/cls/number/guess/'
    req=requests.get(url)
    num=int(req.text)  #req.text返回的请求字符

    times = 0
    
    while True:
        input_num = int(input('请猜一个 1 - 100 的数字：'))
        times += 1

        if num == input_num:
            print('猜对了', '，你一共猜了%d轮' % times)
            return times  # 注意函数的返回值
        elif num > input_num:
            print('猜小了，再试试')
        else:
            print('猜大了，再试试')
            
# 用户的很多次游戏，输入的参数分别是用户的姓名、总游戏次数，最快猜出的轮数，猜过的总轮数
def all_game(name,game_times,min_times,total_times):
    if game_times > 0:
        avg_times = total_times/game_times
    else:
        avg_times = 0
    
    print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案，开始游戏！' % (
        name, game_times, min_times, avg_times
    ))

    while True:
        times = one_game() #用户进行一次游戏，调用一次函数，返回这次函数的轮数
        
        #第一次玩，或轮数比最快猜出的轮数小，更新最快猜出的轮数。
        if game_times == 0 or times < min_times:
            min_times = times
        total_times += times  #总游戏的轮数增加
        game_times +=1  #游戏次数增加

        avg_times = total_times/ game_times #计算平均轮数

        #输出成绩信息，保留两位小数
        print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案' % (
            name, game_times, min_times, avg_times
        ))

        more_game = input('是否继续游戏？(输入y继续，其他退出)')
        if more_game != 'y':
            print('退出游戏，欢迎下次再来！')
            return game_times, min_times, total_times
            # 返回用户最新的总游戏次数，最快猜出的轮数和猜过的总轮数

def main():
    name = input('输入你的名字:')

    f=open('game_many_user.txt',encoding='utf8')
    lines = f.readlines()
    f.close()

    scores={}
    for l in lines:
        s=l.split()
        scores[s[0]]=s[1:]

    score = scores.get(name)
    if score is None:
        score=[0,0,0]

    #调用函数，所有猜数字的逻辑都在函数中，返回值是一个元组，里面是用户的最新的成绩数据
    score_new = all_game(name,int(score[0]),int(score[1]),int(score[2]))

    #更新scores中的成绩，加str转成字符串，为格式化做准备
    scores[name] =[str(score_new[0]), str(score_new[1]), str(score_new[2])]

    result = '' #初始化空字符串，储存数据
    for n in scores:
        line = n+ ' '+ ' '.join(socres[n])+'\n'
        result +=line

    print = open('game_many_user.txt','w',encoding='utf8')
    f.write(result)
    f.close

main()

    
        


        
        


   
