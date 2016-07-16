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

    def f(xy):
        """
        方程组
        :param xy:
        :return:
        """
        x = float(xy[0])
        y = float(xy[1])
        o1 = float(xy[2])
        o2 = float(xy[3])

        return [
            x*x/4900+y*y/3136-1,
            (x+o1)*(x+o1)+(y+o2)*(y+o2)-fontDistance(36, 20, 12, 220),
            o1-o1,
            o2-o2
        ]


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


    def hasOne(result1,result2):
        """
        计算一次方程的解
        :return:
        """

        PRECISION = 1
        klist = linspace(-100, 100, 200)
        blist = linspace(-100, 100, 200)
        (solved_k, solved_b, a, c) = (-float('Inf'), -float('Inf'), result1, result2)  # Inf 代表无穷大
        result = []
        for k in klist:
            for b in blist:
                if k > solved_k:
                    (solved_k, solved_b, a, c) = fsolve(f, [k, b, result1, result2])
                    print (solved_k, solved_b, a, c)
                try:
                    delta_k = min([abs(solved_k - item[0]) for item in result])
                except (IndexError, ValueError):
                    delta_k = 10
                if delta_k > PRECISION:
                    # print '111111111111111111111111111111111111111111111'
                    # print delta_k
                    result.append((int(round(solved_k, 2)), int(round(solved_b, 2))))
                    result = list(result)
            if len(result) >= 2:
                break
        return result

    result = []
    re = []
    words = '智慧应用软件研发工作室王志文'
    i = 0
    while i < 8:
        if i == 0:
            re.extend(hasOne(0, 56))
        else:
            re.extend(hasOne(re[i-1][0], re[i-1][1]))
        if re[i][1]<0:
            print re[i][0],re[i][1]
            print re
            result.extend(re)
        i += 1
    # result = list(result)
    # print result
    result.reverse()
    result = json.dumps(result)
    i = 0
    # while i<len(result):
    #     print words[i]
    #     result.insert(i+1,[words[i]])
    #     i += 1
    return HttpResponse(result)
