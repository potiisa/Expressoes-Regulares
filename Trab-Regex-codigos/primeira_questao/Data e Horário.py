'''
O algoritmo tem como objetivo verificar se uma string tem a formatação de data e horario que atendem a determinadas regras de composição.
A expressão regular é usada em uma condição e os testes foram realizados com casos específicos para retornarem True (caso seja aceita) ou False (caso não).

Script:
Sentenças devem ter o formato dd/mm/aaaa hh:mm:ss, onde d, m, a, h, m, s ∈ N. 
Ex. de sentenças aceitas: 31/08/2019 20:14:55, 99/99/9999 23:59:59
Ex. de cadeias rejeitadas: 99/99/9999 3:9:9, 9/9/99 99:99:99, 99/99/999903:09:09
'''
def eh_data_horario(dh: str) -> bool:
  import re  # Biblioteca utilizada para formar expressões regulares
  '''
    Função que verifica se uma string atende a regras de composição de data e horario e retorna um valor booleano que indica se ela é elegível para ser considerada data e horario ou não.

    Args:
        dh (str): Uma sentença que pode ou não representar uma data e horário válidos.

    Returns:
        True (caso a condição seja atendida) 
        False (caso a condição não seja atendida).

    Examples:
    >>> eh_data_horario('03/09/2002 12:00:00')
    True
    >>> eh_data_horario('31/08/2004 14:0:2')
    False
    '''
  if re.fullmatch(r"^\d{2}\/\d{2}\/\d{4}\s\d{2}\:\d{2}\:\d{2}$", dh):
    return True
  return False

# Exemplos de datas para testes.
testes = [
  "01/01/2002 03:00:00", "17/09/2002 00:00:00", "31/12/2023 00:00:00",
  "99/99/9989 12:12:12", "01/01/2023 00:00:01", "67/58/2002 29:30:00",
  "01/0/200203:00:00", "6/09/20 0:9:00", "dd/mm/aa 00:00:00",
  "99/19899 11:11:11", "01/01 00:00", "3/9/2002 59:30:00"
]

# Validação das sentenças.
for data_horario in testes:
  if eh_data_horario(data_horario):
    print(f"A data e horário {data_horario} são válidos.")
  else:
    print(f"A data e horário {data_horario} são inválidos.")
