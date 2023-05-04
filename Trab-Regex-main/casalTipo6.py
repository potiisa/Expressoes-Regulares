"""
O objetivo do algoritmo é reconhecer e sintetizar arranjos familiares
sobre o alfabeto {H, M, h, m}.
H -> homem;
M -> mulher;
h -> filho do sexo masculino;
m -> filha do sexo femenino;

Script:
Casais homossexuais mais velhos que os filhos com 
  1. qualquer quantidade de filhos homens e mulheres MAS
  2. que não tiveram dois filhos homens consecutivos
"""
# Importação da biblioteca 'random' para gerar números e fazer escolhas aleatórias.
# Importação da biblioteca 're' que permite a manipulação e validação de expressões regulares.
import re, random

def validaFam(familia: str) -> bool:
  """
  Analisa uma sentença e verifica se ela atende aos padrões do Script.

  Args:
    familia (str): uma sentença contendo os símbolos que podem ou não representar
    uma família válida.

  Returns:
    bool: True para uma sentença válida ou False para uma sentença inválida.
    
  Exemples:
    >>> validaFam('MMmmh')
    True
    >>> validaFam('HHmhh')
    False
  """
  padrao = '^(HH|MM)(h?m*(?!hh)| m*h?(?!hh))+$'  #Expressão regular
  validacao = re.match(padrao, familia)  #Busca do padrão na sentença passada
  return validacao

def geraFam() -> str:
  """
  Gera arranjos familiares de acordo com os padrões do Script

  Args:
    None

  Returns:
    str: uma string contendo um arranjo familiar válido.

  Exemples:
    >>> geraFamilia()
    MMmh
    >>> geraFamilia()
    HHmhm
  """
  familia = ""  #Inicializa a string
  while not (validaFam(familia)):  #Loop ocorre enquanto uma cadeia adequada não for criada
    familia = ""
    for i in range(random.randint(1,15)):  #Define o tamanho da cadeia (família)
      alfabeto = ['M', 'H', 'm','h']  #Caracteres disponíveis para representar cada membro
      membro = random.choice(alfabeto)  #Escolhe aleatóriamente um tipo de membro da lista
      familia += membro  #Concatena o integrante à família
  return familia

def geraFamiliaTesteTipo6():
  for i in range(0, 20):
    print(geraFam(), " é uma família válida.")

"""
def validaTestesCasalTipo6():
  #Verificação de cadeias pré-determinadas
  testes = [
    'H', 'MmHhM', 'mMhMhH', 'MM', 'mmHMhM', 'Hh', 'HHhm', 'HhHm', 'Mh', 'HM',
    'hMhMmH', 'HHmmh', 'Hhm', 'HmHhmM', 'h', 'hHhM', 'HHHhmMh', 'MMmmh', 'hM',
    "HHmhmhmh"
  ]

  for familia in testes:
    validacao = validaFam(familia)
    if validacao:
      print(f"A cadeia '{familia}' é válida.")
    else:
      print(f"A cadeia '{familia}' é inválida.")
"""