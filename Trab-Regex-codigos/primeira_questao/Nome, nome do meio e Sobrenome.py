"""
O algoritmo tem o intuito de verificar se uma sentença é composta de:
    Nome, Nome do meio (opcional) e Sobrenome

Script:
    1. As sentenças devem possuir três cadeias de caracteres separadas por espaço.
    2. As três cadeias de caracteres devem conter uma letra maíuscula(A-Z) no inicio da cadeia e 
    quaisquer quantidade de letras minusculas (a-z) antes do espaço em branco (se for no caso da ultima cadeia, antes do final da frase).
    3. No caso da cadeia que represeta o nome do meio, ela é opcional. se estiver presente, 
    deve seguir as regras de verificação de cadeia da regex responsável pela verificação.    
"""

import re

def validaNome(sentenca: str) -> bool:
    """
    Função "validaNome" tem por objetivo validar sentenças compostas por Nome, Nome do meio (opcional) e Sobrenome

    Args: 
    sentenca (str): Argumento do tipo string que deve ser composta por no minimo cadeias de caracteres separadas por espaço

    Returns: 
    bool: True caso o argumentos recebidos sejam validos na regex, caso contrário, retorna False

    Exemples:
      >>> validaNome('Alan Turing')
      True
      >>> validaNome('Alan turing')
      False
    """
    regex = re.compile(r'^[A-Z][a-z]+(\s[A-Z][a-z]+)?\s[A-Z][a-z]+$') #regex construida para verificar se a sentença(argumento) recebida obedece as regras
    if regex.fullmatch(sentenca):
        return True
    return False

# Exemplos de nomes para teste
testes = ["Ana Luiza Ferreira", "Clara Fernanda", "Gustavo Santos", 
        "Maria das Graças", "Rafaela Couto", "Henrique Campos",
        "Ana Luiza dos Santos Ferreira", "Henrique de campos", "Marcos Vinicius Mendes",
        "Renato Araújo de Oliveira", "pedro da silva santos", "Andreza Santos Ferreira.",
        "Júlia Soares da", "Lu1z Carlos Oliveira", "Maria Carolina de Oliveira", "Caio Lopes da Silva"
         ]

# Validação das sentenças
for teste in testes:
    if validaNome(teste):
      print(f"O nome '{teste}' é válido.")
    else:
      print(f"O nome '{teste}' é inválido.")
