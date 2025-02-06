from math import sin, cos, pi
from pylab import plot, show, xlabel, legend, ylabel

theta = []
x = []
y = []

for d in range(0,1801):
    aux = d*pi/180
    theta.append(aux)
    x.append((aux**2)*cos(aux))
    y.append((aux**2)*sin(aux))

# Se quiser plotar relação das coordenadas:
#plot(theta,x)
#plot(theta,y)
#xlabel("theta")
#legend(["x","y"])

# Se quiser plotar espiral de Galileu:
plot(x,y)
xlabel("x")
ylabel("y")
show()
