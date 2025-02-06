# Calculando a média móvel dos dados.

from numpy import loadtxt
from pylab import plot, show, xlabel, xlim, legend

data = loadtxt("sunspots.txt", float)
x = data[:,0] # Estou pegando todos os pontos (:) da coluna 0
y = data[:,1] # Estou pegando todos os pontos (:) da coluna 1
# Se quisesse delimitar da 5 a 10 linha, só colocar data[5:10,0] por exemplo.
# Não preciso delimitar inicio e fim, basta um.
media_movel = []
for k in range(5,1001):
    aux1 = []
    for m in range(-5,5): # media_movel[k] é a média móvel do k+5-ézimo termo.
        aux2 = 0.1*y[k+m]
        aux1.append(aux2)
    soma = sum(aux1)
    media_movel.append(soma)
plot(x,y)
plot(x[4:1000],media_movel)
xlim(0,1000)
legend(["Número de manchas solares","Média móvel"])
xlabel("Meses a partir de 1749")
show()
