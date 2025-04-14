# Matriz testes
A = [[7,1,-1,4],
     [1,-5,1,-2],
     [1, 0, 3,-1],
     [3, 1, -3, 8]]

b = [-10,2, 11,-24]

criterio_parada = 0.0005

x_inicial = [-0.3, 1.3, 2.8,-2.3]

# calculo Gauss-seidel
#### primeiro: ajustar os as linhas para convergência (não sei se essa é a melhor solução)
def testeConvergencia(A):
    for i in range(len(A)):
        soma = 0
        melhor_linha = i
        for j in range(len(A)):
            if i != j:
                soma += abs(A[i][j])

        if A[i][i] < soma:
            melhor_criterio = abs(A[i][i]) - soma

            for k in range (i+1, len(A)):
                soma_k = 0
                for j in range (len(A)):
                    if i != j:
                        soma_k += abs(A[k][j])

                criterio_k = abs(A[k][i]) - soma_k

                if criterio_k > melhor_criterio:
                    melhor_criterio = criterio_k
                    melhor_linha = k

        if melhor_linha != i:
            A[i], A[melhor_linha] = A[melhor_linha], A[i]

#### descobrindo a precisao necessaria
expoente = 0
temp = criterio_parada
while (temp < 1):
    temp *= 10
    expoente+=1
precisao = expoente+1

#### calculo arredondamento
def arredondamento (numero, casas_decimais):
    fator = 10 ** casas_decimais  # 10^casas_decimais
    numero = numero * fator

    parte_inteira = int(numero)
    parte_decimal = numero - parte_inteira

    if parte_decimal == 0.5:
        if (numero * 10) % 1 != 0:
            parte_inteira += 1
        elif parte_inteira % 2 != 0:
            parte_inteira += 1
    elif parte_decimal > 0.5:
        parte_inteira += 1

    return parte_inteira / fator

#### calculo Gauss-Seidel
x_resultado = x_inicial
diferenca_maior = float('inf')

while(diferenca_maior > criterio_parada):
    diferenca_maior = 0
    for i, linha in enumerate(A):
        soma = 0
        for j, elemento in enumerate(linha):
            if j != i:
                soma += elemento * x_resultado[j]

        novo_valor = (b[i] - soma)/A[i][i]
        novo_valor = arredondamento(novo_valor, precisao)
        diferenca = abs(x_resultado[i] - novo_valor)

        if diferenca > diferenca_maior:
            diferenca_maior = diferenca

        x_resultado[i] = novo_valor

#### printa resultado
for valor in x_resultado:
    print(f"{valor:.5f}")

# calculo pelo método de jacobi, com teste de convergência, trocas de linha
def jacobi(A, b, x_inicial, criterio_parada, precisao):
    x_resultado = x_inicial[:] # cria uma cópia do vetor resultado
    diferenca_maior = float('inf') # garantindo que diferenca_maior > criterio_parada na primeira iteracao para que haja pelo menos uma iteracao

    while diferenca_maior > criterio_parada:
        x_anterior = x_resultado[:]  # cria uma cópia dos valores antigos
        diferenca_maior = 0

        for i, linha in enumerate(A):
            soma = 0 # inicializa a soma aqui pois ela zera a cada novo x calculado
            for j, elemento in enumerate(linha):
                if j != i: # se o elemento nao for da diagonal principal
                    soma += elemento * x_anterior[j]  # usa os valores antigos na hora de somar

            novo_valor = (b[i] - soma) / A[i][i] # formula
            novo_valor = arredondamento(novo_valor, precisao) # arredonda
            diferenca = abs(x_anterior[i] - novo_valor) # calcula a diferenca

            if diferenca > diferenca_maior:
                diferenca_maior = diferenca

            x_resultado[i] = novo_valor  # atualiza só depois de calcular tudo

    return x_resultado

# vetor residuo;




