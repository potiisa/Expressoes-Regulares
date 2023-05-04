'''
O algoritmo tem como objetivo verificar se uma string pode ser considerada uma senha ou não.
A expressão regular é usada em uma condição e os testes foram realizados com casos específicos para retornarem True (caso for aceita na condição) ou False (caso não for aceita).

Script:
1. Sentenças podem conter símbolos de Σ∪Γ∪N
2. Sentenças devem ter pelo menos um símbolo de Γ e outro de N
3. Sentenças devem ter comprimento igual a 8
Ex. de sentenças aceitas: 518R2r5e, F123456A, 1234567T, ropsSoq0
Ex. de cadeias rejeitadas: F1234567A, abcdefgH, 1234567HI
'''

def ehSenha(senha: str) -> bool:
  import re
  '''
  função que verifica uma string contida em 'senha' e retorna um valor booleano
  que indica se ela é elegível para ser uma senha ou não.

  Args:
  senha (str): uma sentença que pode ou não representar uma senha válida.

  Returns:
  True (caso a condição seja atendida) e False (caso a condição não seja atendida).

  Examples:
  >>> ehSenha('518R2r5e')
  True
  >>> ehSenha('abcdefgH')
  False
  '''
  if len(senha) != 8:  # primeiramente verificamos se tem 8 caracteres ou não.
    return False
  if re.search(r'[A-Z]+', senha) and re.search(r'[0-9]+', senha):  # agora verificamos se a string apresenta uma letra maius. e um dígito.
    return True
  return False # caso tenha apenas letras minúsculas ou não passe na condição acima:

# exemplos de senhas para testes
testes = [
  "aB3cD5eF", "Zz8hG7jT", "1aB3cD5e", "qQ2wW4eE",
  "4fF6gG5h", "abcdefgH", "12345678", "pqrstuvw",
  "aBcdEFGH", "1a2b3c4d", "2dD6fF8h", "pP7rR2tT",
  "mM1nN9bB", "4fF6gG5h", "mkjnds98", "kajhdns78",
  "mdkslnL0", "0dnais82", "senhA123", "omaiGOD8"
]

# validação das sentenças
for senhas in testes:
  if ehSenha(senhas):
    print("A senha {} é válida.".format(senhas))
  else:
    print("A senha {} é inválida.".format(senhas))