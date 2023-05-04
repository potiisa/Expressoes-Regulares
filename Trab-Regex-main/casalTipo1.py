"""
O objetivo do algoritmo é reconhecer e sintetizar arranjos familiares
sobre o alfabeto {H, M, h, m}.
H -> homem;
M -> mulher;
h -> filho do sexo masculino;
m -> filha do sexo femenino;

Script:
Casais heterossexuais mais velhos que os filhos com 
  1. pelo menos duas filhas mulheres OU
  2. pelo menos um filho homem OU
  3. pelo menos dois filhos homens e uma filha mulher.
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
    >>> validaFam('MHhmm')
    True
    >>> validaFam('HMHm')
    False
  """
  #Foram necessárias mais exp. reg. para evitar erros e garantir a clareza do código
  padrao1 = '^(HM|MH)(m{2,}h*m*|h*m{2,}h*)+$'  #no min. 2 filhas
  padrao2 = '^(HM|MH)(m*h{1,}|h{1,}m*)+$'  #no min. 1 filho
  padrao3 = '^(HM|MH)(h{2,}m{1,}|m{1,}h{2,})+$'  #no min. 2 filhos e 1 filha
  validacao = re.match(padrao1, familia) or re.match(padrao2, familia) or re.match(padrao3, familia)  #Busca do padrão na sentença passada
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
    HMhhmmm
    >>> geraFamilia()
    MHhh
  """
  familia = ""  #Inicializa a string
  while not (validaFam(familia)): #Loop ocorre enquanto uma cadeia adequada não for criada
    familia = ""
    for i in range(random.randint(1, 15)):  #Define o tamanho da cadeia (família)
      alfabeto = ['M', 'H', 'm', 'h']  #Caracteres disponíveis para representar cada membro
      membro = random.choice(alfabeto)  #Escolhe aleatóriamente um tipo de membro da lista
      familia += membro  #Concatena o integrante à família
  return familia

def geraFamiliaTesteTipo1():
  #Impressão de cadeias válidas
  for i in range(0, 20):
    print(geraFam(), " é uma família válida.")

"""
def validaTestesCasalTipo1():
  
  #Verificação de cadeias pré-determinadas
  testes = [
    "HHMmm", "MHhmm", "HM", "HHMMh", "MHhhm", "HMhmm", "HHMMmmmhhmm",
    "MHhMHhhhMh", "HMmmm", "HHMhm", "HHM", "HHMM", "HMmhhmm", "HMm", "HHMMmmmm",
    "HHMMhhhM", "HMhm", "HHMMhhmmmm", "HMmm", "MHhhm"
  ]
  for familia in testes:
    validacao = validaFam(familia)
    if validacao:
      print(f"A cadeia '{familia}' é válida.")
    else:
      print(f"A cadeia '{familia}' é inválida.")
"""

