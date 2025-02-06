# 2L é a quantidade de átomos de cada lado da rede cúbica.

L=int(input("Entre com L:"))

M = 0
for i in range(-L,L+1,1):
    for j in range(-L,L+1,1):
        for k in range(-L,L+1,1):
            if i==j==k==0:
                None
            else:
                if (i+j+k)%2==0:
                    termo = (i**2+j**2+k**2)**(-1/2)
                    print("i=",i,"j=",j,"k=",k)
                else:
                    termo = -(i**2+j**2+k**2)**(-1/2)
                M = M - termo

print("A contante de Magelung é M =",M)
