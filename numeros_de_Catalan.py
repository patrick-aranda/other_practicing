# Obter os números de Catalan até 1 bilhão.

C = 1
i=0

while C<=1000000000:
    print(C)
    i=1+i
    C=(4*i+2)*C/(i+2)
