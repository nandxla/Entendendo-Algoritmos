# Algoritmo de ordenação

def encontra_menor(arr):
    """
    Sempre retorna menor indice de um array
    """
    menor_elem = arr[0]
    menor_indice = 0
    
    for i in range(1, len(arr)): # iterando sobre o tamanho do arr
        if arr[i] < menor_elem:  # se meu array no primeiro índice for menor que menor elemento, então vamos substituir a variável menor elemento e menor indice
            menor_elem = arr[i]  
            menor_indice = i
        
    return menor_indice


def ordenacao_por_selecao(arr):
    novo_arr = []
    
    for i in range(len(arr)):
        menor_elemento = encontra_menor(arr)
        novo_arr.append(arr.pop(menor_elemento))
    
    return novo_arr


array = [
    5, 
    4,
    3,
    10,
    1
]

print(ordenacao_por_selecao(array))
