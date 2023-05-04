'''
O algoritmo tem como objetivo verificar se uma string pode ser considerada um CPF ou não.
A expressão regular é usada em uma condição e os testes foram realizados com casos específicos para retornarem True (caso for aceita na condição) ou False (caso não for aceita).

Script:
1. Sentenças devem ter o formato xxx.xxx.xxx-xx, onde x ∈ N 
Ex. de sentenças aceitas: 123.456.789-09, 000.000.000-00
Ex. de cadeias rejeitadas: 123.456.789-0, 111.111.11-11'''
def ehCPF(cpf: str) -> bool:
  import re  # biblioteca utilizada para formar expressões regulares
  '''
  função que verifica uma string contida em 'cpf' e retorna um valor booleano
  que indica se ela é elegível para ser um CPF ou não.
  
  Args:
  cpf (str): uma sentença que pode ou não representar um CPF válido.
  
  Returns:
  True (caso a condição seja atendida) e False (caso a condição não seja atendida).

  Examples:
  >>> ehCPF('123.456.789-09')
  True
  >>> ehCPF('000.111.22-09')
  False
  '''
  if len(cpf) != 14 :  # considerando que 'cpf' contenha os caract. esp. o tamanho dela não poderá ser diferente de 14.
    return False       
  if re.search(r'\d{3}[.]\d{3}[.]\d{3}[-]\d{2}', cpf):  # 'cpf' precisa conter apenas dígitos, três '.' e um '-'.
    return True
  return False # caso 'cpf' tenha algum caractere que não seja dígito:

# exemplos de CPFs para testes
testes = [
  "123.456.789-09", "987.654.321-00", "111.222.333-96",
  "123.45.678/910", "12345678909", "123.456.789-0A",
  "555.666.777-22", "999.888.777-55", "333.222.111-44", "000.000.000-01",
  "123.456.789/09", "98a.999.123-9K", "000.111.22-09", "123.ABC.789-09",
  "123.456.78909", "123.456.789-091", "123,456,789-09", "123-456-789-09",
  "456.123.456-65", "901.283.987-00"
]

# validação das sentenças
for cpf in testes:
  if ehCPF(cpf):
    print("O CPF {} é válido.".format(cpf))
  else:
    print("O CPF {} é inválido.".format(cpf))