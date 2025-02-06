from math import sin, cos, pi
from pylab import plot, show, xlabel, legend, ylabel
from numpy import exp

theta = []
x = []
y = []
# lindspace[inicio,fim,quantos_pontos_quero] ai posso usar radianos direto.
# Não preciso usar laço for nem append. Uso lindspace que já vai me dar um array e ai qlq operação feita sobre essa variável array vai operar em cada termo da array e modifica-los.
for d in range(0,4321):
    aux = d*pi/180
    theta.append(aux)
    r = exp(cos(aux)-2*cos(4*aux)+(sin(aux/12))**5)
    x.append(r*cos(aux))
    y.append(r*sin(aux))

#Se quiser plotar relação das coordenadas:
#plot(theta,x)
#plot(theta,y)
#xlabel("theta")
#legend(["x","y"])

#Se quiser plotar espiral de Galileu:
plot(x,y)
xlabel("x")
ylabel("y")
show()
