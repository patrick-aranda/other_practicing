# Fatorial inteiro por recursão.
def fatorial_recursao(n):
    if n==1:
        return 1
    else:
        return n*fatorial_recursao(n-1)

# Números de Catalan por recursão.
def Catalan(n):
    if n==0:
        return 1
    else:
        return ((4*n-2)/(n+1))*Catalan(n-1)

n = int(input("Entre com n:"))
print(fatorial_recursao(n), "|",Catalan(n))
