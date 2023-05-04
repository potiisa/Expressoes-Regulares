"""
O objetivo do algoritmo é reconhecer e sintetizar arranjos familiares
sobre o alfabeto {H, M, h, m}.
H -> homem;
M -> mulher;
h -> filho do sexo masculino;
m -> filha do sexo femenino;

Script:
  1. Sentenças que contenham um casal heterossexual.
  2. Conter uma quantidade ímpar de filhas mulheres.
"""
# Importação da função randint() da biblioteca 'random' para gerar números aleatórios
# Importação da biblioteca 're' que permite a manipulação e validação de expressões regulares.
from random import randint
import re

def validaFamilia(arranjo: str) -> bool:
  """
  Analisa uma sentença e verifica se ela atende aos padrões do Script.

  Args:
    arranjo (str): uma sentença contendo os símbolos que podem ou não representar
    uma família válida.

  Returns:
    bool: True para uma sentença válida ou False para uma sentença inválida.
    
  Exemples:
    >>> validaFamilia('MHhmhmm')
    True
    >>> validaFamilia('HMhmm')
    False
  """
  regex = r'^(MH|HM)(m+h*|h*m+|m*h*m*|h*m*h*)+$'  #Expressão regular
  impar = arranjo.count('m') % 2 != 0 #Verifica se o número de filhas é um valor ímpar
  validacao = re.match(regex, arranjo) #Busca do padrão 
  if impar and validacao:
    return True
  return False

def geraFamilia() -> str:
  """
  Gera arranjos familiares de acordo com os padrões do Script

  Args:
    None

  Returns:
    str: uma string contendo um arranjo familiar válido.

  Exemples:
    >>> geraFamilia()
    HMhhhmhh
    >>> geraFamilia()
    MHmh
  """
  tamanho = randint(3, 10)  #Gera um número entre 3 e 10 que determina a quantidade de membros da família
  integrantes = ['H', 'M', 'h','m']  #Lista com os símbolos do alfabeto especificado
  while True:
    familia = ''
    for i in range(tamanho):
      index = randint(0, 3)  #Gera números entre 0 e 3 que correspondem ao índice da lista de símbolos
      familia += integrantes[index]  #Concatena os símbolos para geração de arranjos
    if validaFamilia(familia):  #Verifica o padrão do Script
      break
  return familia

# Bateria de testes que gera 50 arranjos
for i in range(50):
  arranjo = geraFamilia()
  filhas = arranjo.count('m')
  print(f'Arranjo: {arranjo} ({filhas} filhas)')

# Verificação de cadeias pré-determinadas
testes = ["MHhmhmmh", "MHhmmmm", "HMhmhmh", "HMhmmmm", "MHmhhmm", "HMhhmmm", "MHmhmhmh",         "HMhmmhmm", "MHhmmhmh", "HMhmhhm", "MHhmmh", "HMhmh", "MHmhmh", "HMhmmhmh", "MMhhhh", "HHmmmm",         "HHhmmmm", "MHmhmhm", "HMhmmmmmm", "HHhhmmmm"
]

for familia in testes:
  if validaFamilia(familia):
    print(f"A cadeia '{familia}' é válida.")
  else:
    print(f"A cadeia '{familia}' é inválida.")


