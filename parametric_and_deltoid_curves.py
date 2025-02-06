#Curva de deltoide

import matplotlib.pyplot as plt
from math import cos, sin, pi

x = []
y = []
theta = []

for d in range(0,360):
    aux = d*pi/180
    theta.append(aux)
    x.append(2*cos(aux)+cos(2*aux))
    y.append(2*sin(aux)-sin(2*aux))

def plot_parametric():
    plt.xlabel("theta")
    plt.plot(theta,x, label="x")
    plt.plot(theta,y, label="y")
    plt.legend()
    plt.show()

def plot_deltoid_curve():
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x,y)
    plt.show()

k = input("What plot do you want: parametric or deltoid? ")
if k == "parametric":
    plot_parametric()
else:
    plot_deltoid_curve()
