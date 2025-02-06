#Convesor coordenadas polares para cartesianas precisão 2 casas.
r=float(input("Enter r:"))
d=float(input("Enter theta in degrees:"))

from math import sin,cos,pi

theta=d*pi/180
x=round(r*cos(theta), 2)
y=round(r*sin(theta), 2)

print("x =",x, "and y =",y)