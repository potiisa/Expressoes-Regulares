"""
O objetivo do algoritmo é reconhecer e sintetizar arranjos familiares
sobre o alfabeto {H, M, h, m}.
H -> homem;
M -> mulher;
h -> filho do sexo masculino;
m -> filha do sexo femenino;

Script:
Casais homossexuais mais velhos que os filhos
  1. pelo menos seis filhos
  2. os dois primeiros filhos formam um casal
  3. os dois últimos também formam um casal.
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
    >>> validaFamilia('HHhmmmhmhm')
    True
    >>> validaFamilia('HMhmm')
    False
  """
  regex = r'^(HH|MM)(hm|mh)[h,m]{2,}(hm|mh)$'  #Expressão regular
  validacao = re.fullmatch(regex, arranjo)  #Busca do padrão
  if validacao:
    return True
  return False

def geraFamilia() -> str:
  """
  Gera arranjos familiares de acordo com os padrões do Script

  Args:
    None
  
  Returns:
    str: uma string contendo um arranjo familiar.

  Exemples:
    >>> geraFamilia()
    HMhhhmhh
    >>> geraFamilia()
    MHmh
  """
  tamanho = randint(8, 25)  #Gera um número entre 3 e 10 que determina a quantidade de membros da família
  integrantes = ['H', 'M', 'h','m']  #Lista com os símbolos do alfabeto especificado
  familia = ''
  for i in range(tamanho):
    index = randint(0, 3)  #Gera números entre 0 e 3 que correspondem ao índice da lista de símbolos
    familia += integrantes[index]  #Concatena os símbolos para geração de arranjos
  return familia


def geraFamiliaTesteTipo4():
  # Bateria de testes que gera 50 arranjos
  print("Checando 50 famílias aleatórias:")
  for i in range(50):
    arranjo = geraFamilia()
    if validaFamilia(arranjo):
      print(f'Arranjo: {arranjo} é válido.')
    else:
      print(f'Arranjo: {arranjo} é inválido.')

"""
def validaTestesCasalTipo4():
  # Verificação de cadeias pré-determinadas
  print("\nChecando a lista pré-determinada:")
  testes = [
    'HHmhmhhm', 'HHhmhmhhhm', 'MMhmhmhm', 'HHmhmhhhmh', 'MMhmhhhmh', 'HHhmmhmh',
    'MMhmhmmh', 'HHhmhmhm', 'HHhmmhmh', 'HHmhmmhm', 'HHmhmmhmh', 'MMhmhmmh',
    'MMhmmhhmh', 'HHhmhhhmhhmhhm', 'HHmhmhmh', 'MMhmhhhm', 'MMmhhmmh',
    'HHmhhmmhhm', 'HHhmmhmh', 'MMhmhhhm'
  ]

  for familia in testes:
    if validaFamilia(familia):
      print(f"A cadeia '{familia}' é válida.")
    else:
      print(f"A cadeia '{familia}' é inválida.")
"""