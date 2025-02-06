# Função fatorial inteiro.
def fatorial(n):
    if n==0:
        return 1
    else:
        f = 1
        for k in range(1,n+1):
            f *=k
        return f

# Função coeficientes binomiais (n>=k).
def binomial(n,k):
    return (fatorial(n)/(fatorial(k)*fatorial(n-k)))

n = int(input("Entre com n:"))
k = int(input("Entre com k:"))

print("O fatorial de",n,"é",fatorial(n))
print("O binomial de (",n,",",k,") é", binomial(n,k))
