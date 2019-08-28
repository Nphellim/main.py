#!/usr/bin/env python
# coding: utf-8
#encoding=utf-8
from random import *
import json
import requests
from time import time

#procedure that determine the ratio
def MCSimulation(n):
    #number of points to draw
    nPoints = n
    #ro, the value of the ratio
    ro = 0.0
    #list to save and graph points in or out the circle
    in_points = out_points = []
    #ammount of points drawn inside the  circle
    sum_in_sample = 0
    #ammount of points drawn out 
    sum_out_sample = 0
    
    for i in range(nPoints):
        #random pair (x_sample_cord,y_sample_cord) each coordinate goes beetween 0 and 1
        x_sample_cord =  random()
        y_sample_cord =  random()
        #varible to determine if  a point is inside the circle
        d = x_sample_cord**2 + y_sample_cord**2
        if d <= 1:
            sum_in_sample = sum_in_sample + 1
            in_points.append((x_sample_cord,y_sample_cord))
        sum_out_sample = sum_out_sample + 1
        out_points.append((x_sample_cord, y_sample_cord))
    ro = sum_in_sample/float(nPoints)
    return ro

#procedure that calculates
def MCApprox(ro):
    pi_approx = 4.0 * ro
    return pi_approx


def main():
    #res = requests.get('http://www.practice2icc.appspot.com/').json()['value']
    #print MCApprox(res)
    
    print  MCApprox(MCSimulation(5000000))
    
if __name__ == "__main__":
    main()
