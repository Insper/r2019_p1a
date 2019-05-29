#! /usr/bin/env python
# -*- coding:utf-8 -*-

import rospy

import numpy as np

from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

import math


angulo = 0

def scaneou(dado):
    print("Faixa valida de leituras: ", dado.range_min , " - ", dado.range_max )
    print("Leituras:")
    print(np.array(dado.ranges).round(decimals=2))

    global angulo

    menor = 1000.0
    rg = dado.ranges
    angulo = 1000

    for i in range(len(rg)):
        if dado.range_min < rg[i] < dado.range_max:
            if rg[i] < menor:
                menor = rg[i]
                angulo = i

    print("Menor distancia ", menor)
    print("Menor angulo ", angulo)



    


if __name__=="__main__":

    rospy.init_node("le_scan")

    velocidade_saida = rospy.Publisher("/cmd_vel", Twist, queue_size = 3 )
    recebe_scan = rospy.Subscriber("/scan", LaserScan, scaneou)

    parado = Twist(Vector3(0.0, 0, 0), Vector3(0, 0, 0))
    gira = Twist(Vector3(0.0, 0, 0), Vector3(0, 0, math.radians(15)))

    tole = 5



    while not rospy.is_shutdown():
        print("Oeee")
        if angulo > (360 - tole) or angulo < (0 + tole):
            velocidade_saida.publish(parado)
        else:
            velocidade_saida.publish(gira)

        rospy.sleep(0.1)


