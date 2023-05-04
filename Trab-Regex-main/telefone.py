'''
O algoritmo tem como objetivo verificar se uma string pode ser um número de telefone que atende à determinadas regras de composição.
A expressão regular é usada em uma condição e os testes foram realizados com casos específicos para retornarem True (caso seja aceita) ou False (caso não).

Script:
AS sentenças aceitas devem ter um dos formatos seguintes
- (xx) 9xxxx-xxxx
- (xx) 9xxxxxxxx
-  xx  9xxxxxxxx
Ex. de cadeias aceitas: (91) 99999-9999, (91) 999999999, 91 999999999
Ex. de cadeias rejeitadas: (91) 59999-9999, 99 99999-9999, (94)95555-5555
'''


def eh_telefone(tel: str) -> bool:
  import re  # Biblioteca utilizada para formar expressões regulares
  '''
    Função que verifica se uma string atende a regras de composição de um número de telefone e retorna um valor booleano que indica se ela é elegível para ser um telefone ou não.

    Args:
        tel (str): Uma sentença que pode ou não representar um CPF válido.

    Returns:
        True (caso a condição seja atendida) 
        False (caso a condição não seja atendida).

    Examples:
    >>> eh_telefone('91 984505972')
    True
    >>> eh_telefone('91 98430-3893')
    False
  '''
  if re.fullmatch(
      r"^\(\d{2}\)\s9\d{4}\-\d{4}$|^\(\d{2}\)\s9\d{8}$|^\d{2}\s9\d{8}$", tel):
    return True
  return False

def validaTestesTelefone():

  # Exemplos de telefones para testes.
  testes = [
    "(11) 99999-9999", "(22) 98888-8888", "(33) 97777-7777", "(44) 966666666",
    "(55) 955555555", "(66) 944444444", "77 933333333", "88 922222222",
    "99 911111111", "(11) 8999-9999", "(22) 77777", "(33) 85555-555",
    "44 733333333", "(55) 72222-22", "66 61111-111", "(77) 49999-999",
    "(88) 37777-p999", "99 2555-5555"
  ]

  # Validação das sentenças.
  for telefone in testes:
    if eh_telefone(telefone):
      print(f"O Telefone {telefone} é válido.")
    else:
      print(f"O Telefone {telefone} é inválido.")
