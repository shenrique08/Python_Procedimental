# Lê a quantidade de linhas do texto
num_lines = int(input("Digite a quantidade de linhas: "))

# Inicializa uma lista para armazenar as palavras do texto
words = []

# Lê cada linha do texto e adiciona as palavras na lista
line = input()
for i in range(num_lines):

    words += line.split()

# Inicializa um dicionário para armazenar os palíndromos e suas quantidades
palindromes = {}

# Percorre a lista de palavras e verifica se cada palavra é um palíndromo
for word in words:
    # Remove pontuações da palavra e converte todas as letras para minúsculas
    clean_word = "".join(c for c in word if c not in ".,:;!?").lower()

    # Verifica se a palavra é um palíndromo
    is_palindrome = True
    for i in range(len(clean_word) // 2):
        if clean_word[i] != clean_word[-i - 1]:
            is_palindrome = False
            break

    # Se a palavra é um palíndromo, adiciona ela e sua quantidade no dicionário
    if is_palindrome:
        if clean_word not in palindromes:
            palindromes[clean_word] = 1
        else:
            palindromes[clean_word] += 1

# Imprime a lista de palíndromos seguindo a ordem em que são encontrados no texto
for word in words:
    # Remove pontuações da palavra e converte todas as letras para minúsculas
    clean_word = "".join(c for c in word if c not in ".,:;!?").lower()

    # Se a palavra é um palíndromo, imprime ela e sua quantidade
    if clean_word in palindromes:
        print(clean_word, palindromes[clean_word])
        del palindromes[clean_word]
