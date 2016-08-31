# -*- coding: utf-8 -*-
# coding=utf-8
import json
from django.shortcuts import render, HttpResponse
# from scipy.optimize import fsolve
from django.views.decorators.csrf import csrf_exempt
import numpy as np

pi = np.pi


def demo2(req):
    """
    绘制圆形印章
    :param req:
    :return:
    """
    return render(req, "demo2.html")


def demo1(req):
    """
    绘制椭圆印章
    :param req:
    :return:
    """
    return render(req, "demo1.html")


@csrf_exempt
def ellipseFont(req):
    """
    计算椭圆上方字体每个字体和旋转角度
    :param req:
    :return:
    """

    # 目前只考虑字数为奇数的排列
    def f(font_num, l_radius):
        result = []
        resulta = []
        zj = 4 * pi / 3 / font_num  # 字体间的角度
        font_radios = 73  # 所有字体所在的椭圆的长边
        brt = pi / 2 + zj  # 左侧从原点正上方的字依次增加zj角度得到下一个字的圆心角
        i = 0
        while i < font_num / 2:  # 求左侧的字体坐标和倾斜度
            x = font_radios * np.cos(brt)  # x * cos(a)
            y = font_radios * np.sin(brt) * 56 / 74  # y * sin(a) 然后进行压缩比
            angle = pi / 2 - brt
            result.append([x, -y, angle])
            brt += zj
            i += 1
        result.reverse()
        resulta.extend(result)  # 整理计算结果
        resulta.append([0, -font_radios * 56 / 74, 0])  # 正上方的那个字
        result.reverse()
        i = 0
        for r in result:  # 利用y轴对称求的右侧字的坐标
            if font_num / 2 < i:
                break
            i += 1
            x, y, angle = -r[0], r[1], -r[2]
            resulta.append([x, y, angle])
        return resulta

    return HttpResponse(json.dumps(f(11, 74)))
    # global ELENGTH  # 字间距的平方

    # def f(xyz):
    #     """
    #     方程组
    #     :param xy:
    #     :return:
    #     #尤佳佳改！
    #     #使用闭包
    #     """
    #     o1 = float(xyz[1])  # 控制变量1
    #     o2 = float(xyz[2])  # 控制变量2
    #     txy = xyz[0]  # 初始迭代值

    #     def innerf(xy):
    #         x = float(xy[0])
    #         y = float(xy[1])
    #         return [
    #             x * x / 4900 + y * y / 3136 - 1,
    #             (x - o1) * (x - o1) + (y - o2) * (y - o2) - ELENGTH,
    #         ]

    #     for i in range(50):  # 如果误差值始终大于1？
    #         c, d = fsolve(innerf, txy)
    #         print fsolve(innerf, txy)
    #         e, f = innerf([c, d])  # 得出误差值
    #         if e > 1 and f > 1:  # 误差值大于1则重新计算
    #             txy[0] += 1
    #             txy[1] += 1
    #         else:
    #             # print innerf([c, d])
    #             return c, d

    # def fontDistance(a, b, n, p):
    #     """
    #     计算字体之间的距离
    #     :param a: 椭圆的长边
    #     :param b: 椭圆的短边
    #     :param n: 字数
    #     :param p: 弧度
    #     :return: 距离的平方
    #     """

    #     ###
    #     # 角度的计算好像不对
    #     ###
    #     # return ((3.2*(a-b)*p/(360*(n-1))))**2

    #     return (((2 * pi * b + 4 * (a - b)) * p / (360 * (n - 1)))) ** 2

    # def hasOne(a, b):
    #     """
    #     获取一次函数解
    #     ##不需要另外求误差的方法
    #     """
    #     c, d = f([[a + 1000, b + 1000], a, b])
    #     return c, d

    # fontNum = 12
    # ELENGTH = fontDistance(45, 20,fontNum, 220)  # 测试输入的为偶数
    # result = [(0.0, -56.0)]  # 初值
    # for i in range(1, fontNum + 1):  # 循环次数为字体数量的一半
    #     result.append(hasOne(result[-1][0], result[-1][1]))
    #     # print result
    #     ####

    #     # 问题：当循环次数稍大之后，求出的点趋于一个定点！！！

    #     ####
    # result.reverse()  # 原地反转
    # z = -1  # 控制变量
    # r = []  # 返回的数据承载
    # w = []
    # for j in result:
    #     z += 1
    #     if z % 2 == 0:  # 去除两个字体之间的点
    #         continue
    #     if fontNum >= 12 and z < 4:
    #         r.append([-abs(j[0]), abs(j[1])])
    #         w.append([abs(j[0]), abs(j[1])])  # y轴右边的点
    #         continue
    #     if fontNum >=10 and z<1:
    #         r.append([-abs(j[0]), abs(j[1])])
    #         w.append([abs(j[0]), abs(j[1])])  # y轴右边的点
    #         continue
    #     # r.append([j[0], j[1]])  # y轴左边的点
    #     r.append([-abs(j[0]), -abs(j[1])])  # y轴左边的点
    #     w.append([abs(j[0]), -abs(j[1])])  # y轴右边的点
    # w.reverse()
    # r.extend(w)
    # return HttpResponse(json.dumps(r))

    #
    # def verify(x, y, o1, o2):
    #     """
    #     用于验证结果准确性的函数
    #     #实验后发现这个函数有问题,需要修改
    #     """
    #     a=x*x/4900+y*y/3136-1
    #     b=(x-o1)*(x-o1)+(y-o2)*(y-o2)-fontDistance(36, 20, 12, 220)
    #     Dtx = abs(abs(x)-abs(o1))
    #     Dty = abs(abs(y)-abs(o2))
    #     print Dty,Dtx
    #     # print Dtx
    #     # print Dty
    #     return (float(abs(a*b))<1.0) & (float(abs(a+b))<2.0) & (float(Dtx)>10) & (float(Dty)>1)
    #
    # def hasOne(result1,result2):
    #     """
    #     计算一次方程的解
    #     算出来结果的正反很奇怪，还要继续做实验测试一下
    #     思路应该是获取算出来结果这些点中精确度最高的一个返回
    #     现在的情况还需要继续测试，搞清楚fsolve函数，
    #     我困死了，睡觉了，志文你白天有空继续研究，晚上我们继续讨论一下。
    #     :return:
    #     """
    #
    #     b, c = f([[55, 55], result1, result2])
    #     print b, c
    #     return b, c
    #     # PRECISION = 1
    #     # klist = linspace(-100, 100, 100)
    #     # blist = linspace(-100, 100, 100)
    #     # # (solved_k, solved_b, a, c) = (-float('Inf'), -float('Inf'), result1, result2)  # Inf 代表无穷大
    #     # result = []
    #     # for k in klist:
    #     #     for b in blist:
    #     #         solved_k, solved_b = f( [[k, b], result1, result2] )
    #     #         if verify(solved_k,solved_b,result1,result2):
    #     #             return (solved_k,solved_b)
    #             # if k > solved_k:
    #                 # (solved_k, solved_b) = f( [[k, b], result1, result2] )
    #             # try:
    #                 # delta_k = min([abs(solved_k - item[0]) for item in result])
    #             # except (IndexError, ValueError):
    #                 # delta_k = 10
    #             # if delta_k > PRECISION:
    #                 # # print '111111111111111111111111111111111111111111111'
    #                 # # print delta_k
    #                 # result.append((int(round(solved_k, 2)), int(round(solved_b, 2))))
    #                 # result = list(result)
    #         # if len(result) >= 2:
    #             # break
    #     # return result
    #
    # # result = []
    # # re = []
    # # words = '智慧应用软件研发工作室王志文'
    # # i = 0
    # # while i < 8:
    #     # if i == 0:
    #         # re.extend(hasOne(0, 56))
    #     # else:
    #         # re.extend(hasOne(re[i-1][0], re[i-1][1]))
    #     # if re[i][1]<0:
    #        # result.extend(re)
    #     # i += 1
    # # result = list(result)
    # # print result
    # i = 0
    # re = [(0,-56)]
    # for i in range(11):
    #     re.append(hasOne(re[-1][0], re[-1][1]))
    # re.reverse()
    # print re
    # result = json.dumps(re)
    # r = []
    # z = -1
    # for j in re:
    #     z += 1
    #     if z % 2 == 0:
    #         continue
    #     r.append([-abs(j[0]), -abs(j[1])])
    # # print r
    # i = 0
    # # r = [[-70,-15],[-53,-34],[-29,-50],[0,-56],[29,-50],[53,-34],[70,-15]]
    # # while i<len(result):
    # #     print words[i]
    # #     result.insert(i+1,[words[i]])
    # #     i += 1
