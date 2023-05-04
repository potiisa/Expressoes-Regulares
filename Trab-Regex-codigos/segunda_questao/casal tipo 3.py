"""
O algoritmo é responsavel por validar familias compostas pelo alfabeto ('M', 'H', 'm', 'h').
O objetivo é determinar casais heterossexuais que possuam o filho mais velho menina e o filho mais novo menino.

Script:

    Inicia com ou HM ou MH que representa um casal heterossexual onde ou o homem é mais velho que a mulher
    ou a mulher é mais velha que o homem.

    Após a definição do casal, é definida obrigatoriamente uma m -> filha mulher, assim definindo-a como a mais velha
    entre os filhos do casa.

    Após esta etapa é definido zero ou mais integrantes da familia, filhos homens ou mulheres, de forma aleatoria.

    Por fim é definido um h -> filho homem como sendo o filho mais novo da familia.
"""

from random import randint
import re

def regexFamilia(sentenca: str) -> bool:

    """
    Função regexFamilia que tem como objetivo casal heterossexual com o filho mais velho sendo mulher e o filho mais novo do casal sendo homem

    Args: 
        sentenca -> recebe uma cadeia a ser avalida na regex, para saber se esta cadeia de caracteres é valida ou não

    return: 
          retorna True se a cadeia for valida, caso contrário retorna False.
    """

    regex = re.compile(r'^(HM|MH)m(m|h)*h$')

    if regex.fullmatch(sentenca):
        return True
    return False

def geraFamilia() -> str:

  """
  Gera arranjos familiares de acordo com os padrões do Script

  Args:
    None

  Returns:
    familia -> str composta pela familia valida

  Exemples:
    >>> geraFamilia()
    HMhhhmhh
    >>> geraFamilia()
    MHmh
  """

  tamanho = randint(4, 10) #Gera um número entre 4 e 10 que determina a quantidade de membros da família
  integrantes = ['H', 'M', 'h', 'm'] #Lista com os símbolos do alfabeto especificado
  
  while True:
    familia = ''
    for i in range(tamanho):
      index = randint(0, 3) #Gera números entre 0 e 3 que correspondem ao índice da lista de símbolos 
      familia += integrantes[index] #Concatena os símbolos para geração de arranjos
    
    print(f'Familia Criada: {familia}')
      
    if regexFamilia(familia): #Verifica o padrão do Script
        break
  
  print(f'Cadeia Valida: {familia}')
  return familia

familiaValida = geraFamilia()
print(f'Cadeia retornada: {familiaValida}')


#Testes com cadeias pré-definidas:

testes = [
  "HHMmmh", "MHmmh", "HM", "HHMMh", "MHhhm", "HMhmm", "HHMMmmmhhmm",
  "MHhMHhhhMh", "HMmmm", "HHMhm", "HHM", "HHMM", "HMmhhmm", "HMm", "HHMMmmmm",
  "HHMMhhhM", "HMmhhhhh", "HHMMhhmmmm", "HMmm", "MHhhm"
]

for familia in testes:
  validacao = regexFamilia(familia)
  if validacao:
    print(f"A cadeia '{familia}' é válida.")
  else:
    print(f"A cadeia '{familia}' é inválida.")

