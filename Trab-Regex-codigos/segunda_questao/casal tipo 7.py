"""
O algoritmo tem como objetivo validar sentenças que respeitem a regra:

1. Arranjo de no mínimo x∈ℕ e no máximo y∈ℕ , com x>0 , y>0 , e x≤y , de
adultos (Hs ou Ms) mais velhos que os filhos, com qualquer quantidade de filhos
homens e mulheres, mas que os três filhos mais novos não foram homens.
"""
import itertools #biblioteca para efetuar arranjos
import re
from random import randint

def regex_g(cadeia:str, x:int, y:int) -> bool:   
  """
  Função que valida cadeias que seguem a regra de arranjos de H e M definidos por x e y, com qualquer quantidade
  de filhos sendo que os três filhos mais novos não foram homens

  Args:
  cadeia (str): parâmetro que recebera a sentença que será avaliada, parâmetro do tipo string
  x (int): representa o valor minimo dos arranjos de H e M
  y (int): representa o valor maximo dos arranjos de H e M
  
  Return:
  bool: True caso a sentença seja valida, caso contrario a função retorna False.
  """
  regex = re.compile(fr'^(H|M){{{x},{y}}}(((h|m)*mh{{0,2}})|(h|m){{0,2}})?$') #Regex responsavel por validar as sentenças
  if regex.fullmatch(cadeia):
    return True
  return False

def arranjos(lista:list, qtd:int) -> list:
  """
  Função responsavel por fazer os arranjos de H, M

  Args: 
  lista (list): alfabeto que sera feito os arranjos,
  qtd (int): quantidade de arranjos que serão feitos com H, M 

  Return:
  list: lista que contém os arranjos de ['H', 'M']  
  """
  return list(itertools.product(lista, repeat=qtd)) #Retorna arranjos com repetição de caractere, em forma de tupla

def geraSentenca():
    """
    Função responsavel por criar cadeias utilizando os arranjos de H e M dado x e y

    Args:
        None

    Return:
        None
    """
    x = int(input("Digite o valor de X (Valor Mínimo): ")) 
    y = int(input("Digite o valor de Y(Valor Maximo): "))

    print(f'Os valores informados pelo usuario foram: X(Valor minimo) : {x}  Y(Valor maximo): {y}')

    if x > 0 and y > 0 and x <= y:
      

        listaPais = ['M', 'H'] #alfabeto
        arranjos_possiveis = [] #lista que contem tuplas, cada elemento é uma combinação possivel que vai de x até y
        listaCadeias = [] #lista que armazena cadeias criadas pelo gerador
        cadeiasValidas = []
        cadeiasInvalidas = []

        for j in range(5):
          
            for i in range(x, y+1):
                arranjo = arranjos(listaPais, i) #variavel que recebe lista com elementos em tupla

                for index in range (len(arranjo)): #estrutura de repetição para iterar cada elemento da lista arranjo
                    arranjos_possiveis.append(arranjo[index]) #convertendo cada elemento tupla em lista e posteriormente adicionando na lista contendo as tuplas

            for item in arranjos_possiveis: #acessar cada tupla da lista arranjos_possiveis
                cadeia = '' #variavel para incrementar com elementos da lista arranjos_possiveis

                for x in range(len(item)): #acessar cada elemento da tupla
                    cadeia += item[x] #nesta etapa o casal é formado

                tamanhoFilhos = randint(0, 15) #esta decidindo a quantidade de filhos entre 0 e 15
                listaFilhos = ['h', 'm'] #alfabeto filhos

                for i in range(tamanhoFilhos+1):
                    cadeia += listaFilhos[randint(0,1)] #adiciona a cadeia os filhos para fazer a avaliação
                
                listaCadeias.append(cadeia)

            for cadeiaTeste in listaCadeias:
                if regex_g(cadeiaTeste, x, y):
                    cadeiasValidas.append(cadeiaTeste)
                else:
                    cadeiasInvalidas.append(cadeiaTeste)
        
        for cadeiaValida in cadeiasValidas:
            print(f"Cadeia valida: {cadeiaValida}")

        print('---------------------------------------------------------')

        for cadeiaInvalida in cadeiasInvalidas:
            print(f'Cadeia Invalida: {cadeiaInvalida}')
    
    else: 
        print('Os valores de x e y são invalidos')

geraSentenca()

x = int(input("Digite o valor de X (Valor Mínimo): ")) 
y = int(input("Digite o valor de Y(Valor Maximo): "))

#Mais testes, se necessario:
cadeias = [
       'MMm','MMmmm', 'HHm', 
       'HHmhh', 'HMmhhh', 'HH', 'HHhhhhhm', 
       'HHm', 'HHh', 'MMmhhhhhhh', 'HMmhmh', 'Mh', 
       'HMMmmh', 'MMhmmhh', 'MHmhmhm', 'HMm', 'MMmmmhmhhmhmhmmhh',
       'MMhmmhm','MMhmhmm', 'MMMhmhhhmhmhhh'
]

sentValidas = []
sentInvalidas = []

for cadeia in cadeias:
  if regex_g(cadeia, x, y):
    print(f'Cadeia valida: {cadeia}')
    sentValidas.append(cadeia)
  else:
    print(f'Cadeia invalida: {cadeia}')
    sentInvalidas.append(cadeia)
print(sentValidas)
print(sentInvalidas)