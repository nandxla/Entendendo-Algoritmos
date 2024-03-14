"""
SOBRE PESQUISA BINÁRIA:
Pesquisa binária é um algoritmo usado para problemas de busca, exatamente, 
qualquer problema relacionado a busca de algum elemento dentro de algum conjunto de dados, 
seja ele uma lista ou banco de dados (SQL ou NoSQL) pode ser usado uma busca binária.

Mas como funciona uma busca binária? Vamos supor que você esteja procurando uma palavra no dicionários,
sendo mais específico, a palava "Orelha". Não faz nenhum sentido você começar procurando essa palavra
abrindo a primeira página do dicionário, lá estão as palavras com a letra "A", logo, eu tenho certeza que você 
começa abrindo o meio do dicionário, poís ali, está mais perto da letra "O".

A pesquisa binária usa a mesma lógica, imagina que você vai logar no facebook ou instagram, você coloca seu nome de usuário e sua senha,
agora, um algoritmo precisa percorrer a gigantesca base de dados para localizar o seu nome lá. Com isso, ele usa a busca binária.

Um algoritmo de pesquisa binária recebe como argumento: Uma lista ordenada e um elemento, e caso o elemento exista, retorna 
o número da posição daquele elemento, caso contrário, retorna None.

Vamos a um exemplo prático de pesquisa binária: Vamos supor que eu estou pensando em um número de 1 a 100, e falo pra 
você adivinhar o número que eu to pensando e a partir de cada chute, eu falo que se o número está acima 
ou abaixo do número que você falou. Você tem duas opções para pode adivinha.

1. Pesquisa simples: Ir falando número por número, em ordem. Primeiro o número 1, segundo o número 2 e por ai vai... 
com isso, se eu tiver pensando no número 98, você vai precisar chutar 97 vezes até adivinhar. Nada performático né?

2. Pesquisa binária: Começar chutando pelo 50, com isso, caso o número tiver acima, você já eliminou metado das tentativas.
Logo em seguida o 75 e por ai vai...

É possível calcular o número total de tentativas possíveis, log n = T -> onde n é a quantidade de elementos e T o total de tentativas.

"""


lista = [1, 2, 3, 5, 6, 7, 10, 11, 13, 15, 16, 19, 20, 23]

def busca_binaria(lista_ordenada, item):
    baixo = 0  # primeiro indice do array
    alto = len(lista_ordenada) - 1  # último indice do array

    # enquanto o houver itens entre o valor mais baixo e o valor mais alto
    while baixo <= alto:
        meio = (baixo + alto) // 2  # indice elemento central
        chute = lista_ordenada[meio]  # elemento retornado pelo chute
    
        if chute == item:
            return meio 
        
        if chute > item:
            alto = meio - 1 
        
        else:
            baixo = meio + 1  # agora o valor mais baixo vai ser o valor central (somamos 1 por conta do índice dos arrays), com isso nosso range de elementos muda
        
    return None

print(busca_binaria(lista, 7))
