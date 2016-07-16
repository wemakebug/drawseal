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

    def f(xyz):
        """
        方程组
        :param xy:
        :return:
        #尤佳佳改！
        #使用闭包
        """
        o1 = float(xyz[1])
        o2 = float(xyz[2])
        txy = xyz[0]
        def innerf(xy):
            x = float(xy[0])
            y = float(xy[1])
            return [
                x*x/4900+y*y/3136-1,
                (x+o1)*(x+o1)+(y+o2)*(y+o2)-fontDistance(36, 20, 12, 220),
            ]
        return fsolve(innerf,txy)


    def fontDistance(a, b, n, p):
        """
        计算字体之间的距离
        :param a: 椭圆的长边
        :param b: 椭圆的短边
        :param n: 字数
        :param p: 弧度
        :return: 距离的平方
        """
        return round(((2*math.pi*b+4*(a-b)*p/360)/(n-1))**2, 2)

    def verify(x, y, o1, o2):
        """
        用于验证结果准确性的函数
        #实验后发现这个函数有问题,需要修改
        """
        a=x*x/4900+y*y/3136-1
        b=(x+o1)*(x+o1)+(y+o2)*(y+o2)-fontDistance(36, 20, 12, 220)
        print float(abs(a*b))
        print float(abs(a+b))
        return (float(abs(a*b))<1.0) & (float(abs(a+b))<2.0)

    def hasOne(result1,result2):
        """
        计算一次方程的解
        算出来结果的正反很奇怪，还要继续做实验测试一下
        思路应该是获取算出来结果这些点中精确度最高的一个返回
        现在的情况还需要继续测试，搞清楚fsolve函数，
        我困死了，睡觉了，志文你白天有空继续研究，晚上我们继续讨论一下。
        :return:
        """

        PRECISION = 1
        klist = linspace(-100, 100, 100)
        blist = linspace(-100, 100, 100)
        # (solved_k, solved_b, a, c) = (-float('Inf'), -float('Inf'), result1, result2)  # Inf 代表无穷大
        result = []
        for k in klist:
            for b in blist:
                solved_k, solved_b = f( [[k, b], result1, result2] )
                if verify(solved_k,solved_b,result1,result2):
                    return (solved_k,solved_b)
                # if k > solved_k:
                    # (solved_k, solved_b) = f( [[k, b], result1, result2] )
                # try:
                    # delta_k = min([abs(solved_k - item[0]) for item in result])
                # except (IndexError, ValueError):
                    # delta_k = 10
                # if delta_k > PRECISION:
                    # # print '111111111111111111111111111111111111111111111'
                    # # print delta_k
                    # result.append((int(round(solved_k, 2)), int(round(solved_b, 2))))
                    # result = list(result)
            # if len(result) >= 2:
                # break
        # return result

    # result = []
    # re = []
    # words = '智慧应用软件研发工作室王志文'
    # i = 0
    # while i < 8:
        # if i == 0:
            # re.extend(hasOne(0, 56))
        # else:
            # re.extend(hasOne(re[i-1][0], re[i-1][1]))
        # if re[i][1]<0:
           # result.extend(re)
        # i += 1
    # result = list(result)
    # print result
    i = 0
    re = []
    while i < 4:
        if i == 0:
            re.append(hasOne(0, 56))
        else:
            re.append(hasOne(re[-1][0], re[-1][1]))
        i += 1
    re.reverse()
    result = json.dumps(re)
    print result
    i = 0
    # while i<len(result):
    #     print words[i]
    #     result.insert(i+1,[words[i]])
    #     i += 1
    return HttpResponse(result)
