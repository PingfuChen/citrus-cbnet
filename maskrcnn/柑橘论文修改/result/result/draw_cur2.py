import os
import matplotlib.pyplot as plt
import random
acc1,acc2,acc3 = [],[],[]
acc = [acc1,acc2,acc3]
loss1,loss2,loss3 = [],[],[]
loss = [loss1,loss2,loss3]
txt = ['vgg.txt','vgg-c.txt','resnet.txt']
for i in range(3):     #循环读取3个文本数据
    with open(txt[i]) as f:      #打开文本文件
        for line in f.readlines():   #按每行循环读取
            t1,t2,t3 = line.split(',')    #字符串切片，t2为loss.t3为acc
            tmp_acc = float(t2.split(':')[-1])   #从后往前读取数值
            tmp_loss = float(t3.split(':')[-1])
            acc[i].append(tmp_acc)  #在列表末尾添加新的对象
            loss[i].append(tmp_loss)
        

x = [i for i in range(len(loss1))]
for i in range(3):
    plt.plot(x,acc[i],label=txt[i].replace('.txt','_acc'))

for i in range(3):
    plt.plot(x,loss[i],label=txt[i].replace('.txt','_loss'))

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.xlabel('Epoach/次')
plt.ylabel('Train loss')

plt.legend()   #给图像加上图例
plt.show()     #展示图片


