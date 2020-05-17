'''
Guess Number 4 the best score

Note:
1. f.readline() 读取第一行;f.readlines()读取所有行
2. 字典复习
   1) dict() and turple() can separately creat new ()
   2) disorder
   3) for is also can be used
   4) dic.get[key] is right only the dic has this key value
   5) 
'''
  
import random    

f=open("game_one_user.txt")  # 打开文件
data=f.read()  #读取内容，注意readlines整体作为一个字符
#print(type(data),data)  #判断类型
f.close  #关闭文件
#print(data)
A=data.split(" ")  #生成列表
if A[-1] == 0:
    print("您还没有游戏记录")
else:
    A.append(A[-1])
    #print(A)
    A[-2]=int(A[1])*int(A[-1])
    #print(A)
    
    # 生成字典
    num_dict=dict()   # or num_dict={}
    name=A[0] 
    #print(name,type(name))
    game_times = int(A[1])
    min_times = int(A[2])
    total_times = A[3]
    ave_times = A[4]


    num_dict["name"]=name
    num_dict["game_times"]=game_times
    num_dict["min_times"]=min_times
    num_dict["total_times"]=total_times
    num_dict["ave_times"]=ave_times
    print(num_dict)
    

# 开始游戏
name = input('请输入你的名字： ')
time = 0  #次数
total =0  # 总轮数
min_count = 0  #最小轮数

while True:
    time +=1
    num = random.randint(1,10)
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
    if min_count ==1 or count < min_count:
        min_count = count


    print('%s, 你一共玩了%d次，最少%d轮猜出答案,平均%d轮猜出答案' % (name, time, min_count,total/time))      
    con=input('是否继续游戏？(输入y继续;其它退出)')
    if con != "y"  :   
        print('退出游戏，欢迎下次再来！')
        break
# 文件写入
result ='%s %d %d %d' % (name, time, min_count,total/time)
print(result)
f=open('game_one_user.txt','w',encoding='utf8')
f.write(result)
f.close()

'''
1. 文件的写入的要素为字符串
2. 注意标识编码
'''

'''
其他想法，可否通过验证用户名是否存在进行过往记录展示
name_input=str(input('input your name:'))
print(name_input, type(name_input))
name_record = name_input+".txt"
while True:
    f=open(name_record)
    data=f.readline(4)
    f.close
    print(data)
    break
 ''' 









