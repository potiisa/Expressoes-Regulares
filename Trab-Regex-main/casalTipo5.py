'''
O algoritmo tem como objetivo reconhecer e produzir arranjos familiares sobre o alfabeto {H, M, h, m}.
H -> homem;
M -> mulher;
h -> filho do sexo masculino;
m -> filha do sexo feminino.

Script:
1. Casais homossexuais.
2. O sexo dos filhos é alternado conforme a ordem de nascimento.
'''
def ehFamilia_5(fml: str) -> bool:
  import re  # biblioteca utilizada para formar expressões regulares
  '''
  Analisa uma string 'fml' e verifica se ela atende aos requisitos do Script.

  Args:
  fml (str): uma sentença que contendo os símbolos do alfabeto que podem ou não representar uma família válida.

  Returns:
  bool: True (caso a sentença seja válida) ou False (caso a sentença seja inválida).

  Examples:
    >>> ehFamilia_5('MMhmhm')
    True
    >>> ehFamilia_5('HMmmhh')
    False
  '''
  exp = r'^(HH|MM)(h|m|(hm)+h?|(mh)+m?)$' # Expressão regular
  if re.match(exp, fml): # busca do padrão dentro de 'fml'
    return True
  return False # caso o padrão não seja encontrado:

def gerador_fml() -> str:
  from random import randint  # biblioteca utilizada para gerar números aleatórios
  '''
  Gera arranjos familiares de acordo com os padrões do Script.
    
  Args:
  None
    
  Returns:
  str: uma string contendo um arranjo familiar válido.
    
  Examples:
    >>> gerador_fml()
    HHmhmh
    >>> gerador_fml()
    MMhmhm
  '''
  tam = randint(3, 10)   # gera um número que determina a quantidade de membros da família
  integrantes = ['H', 'M', 'h', 'm']  # lista com os símbolos do alfabeto especificado
  while True:
    fam = ''
    for i in range(tam):
      index = randint(0, 3)   # gera um número que corresponde ao index da lista de símbolos
      fam += integrantes[index]  # concatenação dos símbolos para geração dos arranjos
    if ehFamilia_5(fam): # verifica o padrão do Script
      break
    return fam

def geraFamiliaTesteTipo5():
# Bateria de testes que gera 20 arranjos
  familias = []
  for i in range(20):
      arranjo = gerador_fml()
      familias.append(arranjo)
  print(familias)

"""
def validaTestesCasalTipo5():
  # Bateria de testes com casos pré-determinados
  testes = [
    "HMhmmhmmh", "MHhmhmhm", "MMhmhm", "HHmhmh", "MMmmhmh",
    "MHmhmh", "MMmhmhmh", "HHmhmhmhmh", "HMmhhmhm", "MMhmhmmh",
    "HHhmmhmmh", "MMhmmhm", "MMh", "HHm", "HMm",
    "MHh", "MHhmmmm", "HHhmhmhm", "MMmmhmmh", "HHhmhm"
  ]

  for familia in testes:
    if ehFamilia_5(familia):
      print(f"A cadeia {familia} é válida.")
    else:
      print(f"A cadeia {familia} é inválida.")
"""