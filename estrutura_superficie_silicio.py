from numpy import loadtxt
from pylab import show,imshow

data = loadtxt("stm.txt",float)
imshow(data,origin="lower")
show()

# Lembre que a figura gerada carrega o problema dos eixos estarem invertidos.
