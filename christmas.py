import turtle as t
import random
import math
import time
def flower_sky():
    # 石蕊红
    t.pencolor("#f0c9cf")
    pos=(random.randint(-800,800),random.randint(0,400))
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor("#f0c9cf")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def flower_ground():
    # 姜红
    t.pencolor("#eeb8c3")
    pos=(random.randint(-800,800),random.randint(-300,0))
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor("#eeb8c3")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def snow():
    # 月白
    t.pencolor("#eef7f2")
    pos = (random.randint(-800, 800), random.randint(0, 400))
    t.penup()
    t.goto(pos)
    t.pendown()
    t.fillcolor("#eef7f2")
    t.begin_fill()
    t.circle(2)
    t.end_fill()

def tree(degree,len):
    t.seth(degree)
    # 玫瑰灰
    t.pencolor("#4b2e2b")
    t.pd()
    t.fd(len)
    if len>0:
        a=t.pos()
        tree(degree + 18, len - 10)
        t.goto(a)
        tree(degree - 18, len - 10)
    else:
        # 牡丹粉红
        t.pencolor(238,162,164)
        t.circle(2)
        # 月白
        t.pencolor("#eef7f2")
        t.circle(3)
        t.penup()

# 初始化
t.screensize(1000,1000)
t.colormode(255)

t.bgcolor("#989292")
t.speed(0)
t.penup()
t.goto(0,-300)
# time.sleep(10)

tree(90,100)
for i in range(100):
    flower_ground()
for i in range(200):
    flower_sky()
    snow()
t.penup()
t.goto(0,350)
t.pendown()
t.write("新年快乐",align="center",font=("youyuan",100,"normal"))
t.mainloop()
#
# from turtle import *
# from random import *
# from math import *
#
# def tree(n, l):
#     pd() # 下笔
#     # 阴影效果
#     t = cos(radians(heading() + 45)) / 8 + 0.25
#     pencolor(t, t, t)
#     pensize(n / 3)
#     forward(l) # 画树枝
#
#
#     if n > 0:
#         b = random() * 15 + 10 # 右分支偏转角度
#         c = random() * 15 + 10 # 左分支偏转角度
#         d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
#         # 右转一定角度，画右分支
#         right(b)
#         tree(n - 1, d)
#         # 左转一定角度，画左分支
#         left(b + c)
#         tree(n - 1, d)
#
#         # 转回来
#         right(c)
#     else:
#         # 画叶子
#         right(90)
#         n = cos(radians(heading() - 45)) / 4 + 0.5
#         pencolor(n, n*0.8, n*0.8)
#         circle(3)
#         left(90)
#
#         # 添加0.3倍的飘落叶子
#         if(random() > 0.7):
#             pu()
#             # 飘落
#             t = heading()
#             an = -40 + random()*40
#             setheading(an)
#             dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
#             forward(dis)
#             setheading(t)
#
#
#             # 画叶子
#             pd()
#             right(90)
#             n = cos(radians(heading() - 45)) / 4 + 0.5
#             pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
#             circle(2)
#             left(90)
#             pu()
#
#             #返回
#             t = heading()
#             setheading(an)
#             backward(dis)
#             setheading(t)
#
#     pu()
#     backward(l)# 退回
#
# bgcolor(0.5, 0.5, 0.5) # 背景色
# ht() # 隐藏turtle
# speed(0) # 速度，1-10渐进，0最快
# tracer(0, 0)
# pu() # 抬笔
# backward(100)
# left(90) # 左转90度
# pu() # 抬笔
# backward(300) # 后退300
# # tree(12, 100) # 递归7层
# done()