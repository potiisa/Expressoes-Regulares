"""
Algoritmo responsável por validar números reais que contenham ou não 
a especifcação de um sinal positivo ou negativo em sua entrada.

Script:
  1. As sentenças devem ser inciadas pelos símbolos '+', '-', ou vazio;
  2. Seguidamente por um ou mais símbolos do conjunto {0, 1, 2, ..., 9};
  3. Após, a sentença deve conter, um único símbolo separador '.';
  4. A sentença deve terminar com, no mínimo, um símbolo do conjunto {0, 1, 2, ..., 9};
  5. Exceção: números que não tenham sua parte fracionária representada, devem ser sentenças 
    consideradas.
"""

# Importação da biblioteca 're' que permite a manipulação e validação de expressões regulares.
import re

def validaNumReal(n: str) -> bool:
  """
  Analisa uma sentença e verifica se ela atende aos padrões do Script.

  Args:
    n (str): uma sentença que pode ou não representar um número real válido.

  Returns:
    bool: True para uma sentença válida e False para um sentença inválida.

  Examples:
    >>> validaNumReal('-25.467')
    True
    >>> validaNumReal('+64.')
    False
  """
  regex = "^[+|-]?(\d+\.\d+|\d+)$"  #Expressão regular
  padrao = re.compile(regex)  #Compilação da expressão
  busca = padrao.search(n)  #Busca do padrão na sentença passada
  if busca:
    return True
  return False

def Teste(validacao: bool, valor: str) -> None:
  """
  Mostra mensagem com o resultado do teste de uma dada sentença.

  Args:
    validacao (bool): True ou False.
    valor (str): uma sentença.

  Returns:
    None

  Exemples:
    >>> Teste(True, '+1')
    mensagem
    >>> Teste(False, '1.')
    mensagem 
  """
  if validacao:
    print(f'valor: "{valor}" (É válido)')
  else:
    print(f'valor: "{valor}" (É inválido)')

def validaTestesNumReal():
  # Exemplos de números para teste
  testes = ['-21.56', '+1.0', '-0.5', '64.90', '2.78', '-1', '+97', '156', '-0.01', '+99.0', '.1', '189.', '64,9', '-12.', '+.10', '3,14', '-000000,1', '+1,00005', '+0,1', '+2.']

  # Validação das sentenças - Itera pela lista de testes
  for numero in testes:
    Teste(validaNumReal(numero), numero)
