# Matriz testes
A = [[7,1,-1,4],
     [1,-5,1,-2],
     [1, 0, 3,-1],
     [3, 1, -3, 8]]

b = [-10,2, 11,-24]

criterio_parada = 0.0005

x_inicial = [-0.3, 1.3, 2.8,-2.3]

# calculo Gauss-seidel
#### primeiro: ajustar os as linhas para convergência
for i in range(len(A)):
    soma = 0
    melhor_linha = i
    for j in range(len(A)):
        if i != j:
            soma += abs(A[i][j])
    if abs(A[i][i]) < soma:
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
print("x̄ =\n")
for valor in x_resultado:
    print(f"{valor:.5f}")

# vetor residuo:
# A.x̄ - b -> vai usar a matriz A e multiplica com o vetor x_resultado, depois faz a diferença com o vetor b

def qualidadeAjusteVetorResiduo(A, b, x_resultado):
    vetResiduo = [] # apenas a declaração do vetor
    for i in range (len(x_resultado)): # iterador das linhas
        soma = 0 # soma resultante da multiplicação de matrizes
        for j in range(len(A[i])): # iterador das colunas, poderia iterar utilizando o mesmo parâmetro do iterador das linhas (o tamanho do vetor resultado, que sempre terá como tamanho a quantidade de linhas da matriz A, se não não tem como fazer o produto matricial), mas ao utilizar o tamanho da linha é possível incluir matrizes nao quadradas na solução. Esse foi um problema que percebi nos testes.
            soma += A[i][j] * x_resultado[j] # produto matricial
        residuo = soma - b[i] # quando termino de iterar todos as colunas da matriz e eu ja tenho o resultado da primeira linha da matriz resultante, eu tiro a diferença com a linha respectiva do vetor de termos independentes.
        vetResiduo.append(residuo) # no final apenas adiciona o residuo no fim do vetor residuo, o método .append() faz exatamente isso
    print("\nVetor Residuo:\n")
    for valor in vetResiduo: # printar o vetor residuo
        print(f"{valor:.5f}") # .5f indica que é para formatar o print para 5 casas decimais

qualidadeAjusteVetorResiduo(A, b, x_resultado) # chama a função do vetor residuo
