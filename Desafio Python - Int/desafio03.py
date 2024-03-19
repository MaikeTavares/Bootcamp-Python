# Desafio
# Você está trabalhando para uma empresa que utiliza extensivamente os 
# serviços da AWS, e após algumas análises a equipe de segurança identificou 
# que algumas senhas dos usuários no IAM são fracas e podem representar um 
# risco à segurança dos dados da empresa. 
# Para resolver esse problema, foi solicitado que você desenvolva um 
# programa capaz de analisar as senhas dos usuários e fornecer uma validação de 
# força com base em critérios predefinidos.

# Requisitos de segurança para a senha:

# A senha deve ter no mínimo 8 caracteres.
# A senha deve conter pelo menos uma letra maiúscula (A-Z).
# A senha deve conter pelo menos uma letra minúscula (a-z).
# A senha deve conter pelo menos um número (0-9).
# A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.
# Saiba mais sobre o Regex em: Java Regular Expressions

# Entrada
# A entrada será uma única string representando a senha que precisa ser validada.

# Saída
# Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

# Entrada	Saída
# - 0101
# - 030609saturno*
# - 010203Jupiter

# Saída
# - Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.
# - Sua senha atende aos requisitos de seguranca. Parabens!
# - Sua senha nao atende aos requisitos de seguranca.

def verificar_forca_senha(senha):


  comprimento_minimo = 8
  tem_letra_maiuscula = False
  tem_letra_minuscula = False
  tem_numero = False
  tem_caractere_especial = False
  caracteres_especiais = "!, @, #, $, %, *"

  # Verificando o comprimento da senha
  if len(senha) < comprimento_minimo:
    return f"Sua senha e muito curta. Recomenda-se no minimo {comprimento_minimo} caracteres."

  # TODO: Verifique se a senha contém letras maiúsculas e minúsculas
  for char in senha:
    if char.islower():
      tem_letra_minuscula = True
    elif char.isupper():
      tem_letra_maiuscula = True
    elif char.isdigit():
      tem_numero = True
    elif char in caracteres_especiais:
      tem_caractere_especial = True
  

  # Verificando se a senha contém sequências comuns
  sequencias_comuns = ["123456", "abcdef"]
  for sequencia in sequencias_comuns:
    if sequencia in senha:
      return "Sua senha contem uma sequencia comum. Tente uma senha mais complexa."

  # Verificando se a senha contém palavras comuns
  palavras_comuns = ["password", "123456", "qwerty"]
  if senha in palavras_comuns:
    return "Sua senha e muito comum. Tente uma senha mais complexa."

  # TODO: Verificar o comprimento mínimo e critérios de validação
  if tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial:
    return "Sua senha atende aos requisitos de seguranca. Parabens!"
  else:
    return "Sua senha nao atende aos requisitos de seguranca."



# Obtendo a senha do usuário
senha = input().strip()

# Verificando a força da senha
resultado = verificar_forca_senha(senha)

# Imprimindo o resultado
print(resultado)