# Introdução de número por usuário
num1 = input("Digite seu primeiro numero: ")
num2 = input("Digite seu segundo numero: ")
convert_num1 = float(num1)
convert_num2 = float(num2)

# Operações

def operacao():
  escolhaOperacao = input("Escolha a operação que deseja realizar: (1: soma; 2: subtração; 3: multiplicação; 4: divisão)")
  if escolhaOperacao == '1':
    print(convert_num1 + convert_num2)
  elif escolhaOperacao == '2':
      print(convert_num1 - convert_num2)
  elif escolhaOperacao == '3':
      print(convert_num1 * convert_num2)
  elif escolhaOperacao == '4':
      print(convert_num1 / convert_num2)
  else:
      print("Operação inválida. Tente novamente")

# Execução
operacao()
continuarNumeros = input('Deseja continuar? (S/N)')

while continuarNumeros == 'S':
  operacao()
  continuarNumeros = input('Deseja continuar? (S/N)')
else:
  print('Até a próxima!')
