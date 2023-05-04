"""
O algoritmo tem o intuito de verificar se uma string que representa um endereço de e-mail é valido ou não.
A expressão regular é aplicada em uma função e o teste foi realizado a partir de uma iteração de uma lista de strings.

Script:
1. Sentenças devem conter um, e apenas um, símbolo “@”, que deve ser precedido, no mínimo, um símbolo do alfabeto Σ= {a, b, c, …, z}, e não pode estar no começo do endereço. 
2. Excetuando o símbolo “@”, as sentenças possuem apenas símbolos de  Σ.
3. Sentenças devem terminar com a subcadeia “.com.br” ou “.br” e ter, pelo menos, um símbolo de Σ entre o símbolo “@” e essas subcadeias.
"""

#Importação da biblioteca 're' para utilizar Regex em Python
import re

#Função para definir se um e-mail é válido ou não
def validaEmail(email: str) -> bool:
  """
  Verifica se uma sentença atende aos padrões exigidos para e-mail do script.

  Args:
  email (str): uma sentença que pode ou não representar um e-mail válido.
  
  Returns: 
  validacao (bool): True para uma sentença válida e False para um sentença inválida.
  
  Examples:
    >>> validaEmail('melissa@ufpa.com.br')
    True
    >>> validaEmail('ana@gmail.')
    False
  """
  padrao = r"^[a-z]+@[a-z]+(\.com\.br|\.br)$" #Expressão regular
  validacao = re.match(padrao, email)         #Busca do padrão na sentença passada
  return validacao

# Exemplos de e-mails para teste
testes = [
  "hotmail@python.br", "jessica@projeto.com.br", "carlos_2019@.com.br",
  "lauraa@12345", "maria@empresa.com.br", "nicolas@brasil.br",
  "ana-maria@.com", "alice@gmail.com.br", "maria@.br",
  "roberta@projeto.com.br", "roberta@projeto.", "fernanda@ufpa.com.br",
  "1@dominio", "joao@ufpa.", "joao@ufpa.br", "@python.org.br",
  "anya@site.com.br", "carlos@empresa.com.br", "@site.com.br", "@gmail.com"
]

# Validação das sentenças - Itera pela lista de testes
for email in testes:
  if validaEmail(email):
    print(f"O e-mail '{email}' é válido.")
  else:
    print(f"O e-mail '{email}' é inválido.")
