#Convesor coordenadas cartesianas para polares precisão 2 casas.

x=round(float(input("Enter x:")), 2)
y=round(float(input("Enter y:")), 2)

from math import acos,asin,pi

r = round((x**2 + y**2)**(1/2), 2)

aux1 = round((acos(x/r))/pi, 2)

if x>=0 and y>=0:
    theta = aux1
elif x>=0 and y<0:
    theta = 2 - aux1
elif x<0 and y>=0:
    theta = aux1
else:
    theta = 0.5 + aux1

print("Theta=",theta,"*pi", "and r=",r)
