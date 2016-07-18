# -*- coding: utf-8 -*-
# coding=utf-8
import json
from django.shortcuts import render, HttpResponse
from scipy.optimize import fsolve
from django.views.decorators.csrf import csrf_exempt
from math import sin, cos
from numpy import *
import math


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


    global ELENGTH  # 字间距的平方

    def f(xyz):
        """
        方程组
        :param xy:
        :return:
        #尤佳佳改！
        #使用闭包
        """
        o1 = float(xyz[1])  # 控制变量1
        o2 = float(xyz[2])  # 控制变量2
        txy = xyz[0]  # 初始迭代值

        def innerf(xy):
            x = float(xy[0])
            y = float(xy[1])
            return [
                x * x / 4900 + y * y / 3136 - 1,
                (x - o1) * (x - o1) + (y - o2) * (y - o2) - ELENGTH,
            ]

        for i in range(50):  # 如果误差值始终大于1？
            c, d = fsolve(innerf, txy)
            e, f = innerf([c, d])  # 得出误差值
            if e > 1 and f > 1:  # 误差值大于1则重新计算
                txy[0] += 1
                txy[1] += 1
            else:
                print innerf([c, d])
                return c, d


    def fontDistance(a, b, n, p):
        """
        计算字体之间的距离
        :param a: 椭圆的长边
        :param b: 椭圆的短边
        :param n: 字数
        :param p: 弧度
        :return: 距离的平方
        """

        ###
        ### 角度的计算好像不对
        ###
        # return ((3.2*(a-b)*p/(360*(n-1))))**2

        return (((2 * math.pi * b + 4 * (a - b)) * p / (360 * (n-1) ))) ** 2


    def hasOne(a, b):
        """
        获取一次函数解
        ##不需要另外求误差的方法
        """
        c, d = f([[100-a, 100-b], a, b])
        return c, d


    ELENGTH = fontDistance(36, 20, 12, 220)  # 测试输入的为偶数
    result = [(0.0, 56.0)]  # 初值
    for i in range(1,7):  # 循环次数为字体数量的一半
        result.append(hasOne(abs(result[-1][0]),abs(result[-1][1])))
        ####

        ####  问题：当循环次数稍大之后，求出的点趋于一个定点！！！

        ####
    result.reverse()  # 原地反转
    z = -1  # 控制变量
    r = []  # 返回的数据承载
    w = []
    for j in result:
        z += 1
        if z % 2 == 0:  # 去除两个字体之间的点
            continue
        r.append([-abs(j[0]), -abs(j[1])])  # y轴左边的点
        w.append([abs(j[0]), -abs(j[1])])  # y轴右边的点
    w.reverse()
    r.extend(w)
    return HttpResponse(json.dumps(r))

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
