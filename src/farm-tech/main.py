import math

# Dados em Vetores
cultura = []
areas = []
insumos = []

# Métodos para calcular as formas geométricas
def area_circulo(raio, pi):
  pi = math.pi
  return pi * raio ** 2

def area_retangulo(area, base, altura):
  area = base * altura 
  return area

def area_triangulo(area, base, altura):
  area = (base * altura) / 2
  return area

# Métodos para opções
def calcular_insumos():
  print("Informe o tipo de figura geométrica para o plantio:")
  print("1. Círculo;")
  print("2. Retângulo;")
  print("3. Triângulo.")
  area = int(input("Escolha uma opção:"))

  areas.append(area)

  if areas == 1:
    area_circulo()
  elif areas == 2:
    area_retangulo()
  elif areas == 3:
    area_triangulo()

def imprimir_dados():
  print("imprimir")
  
def atualizar_dados():
  print("atualizar")

def delecao_dados():
  print("delecao")

# Loop
while True:
  print("------------------\nMENU\n------------------")
  print("1. Entrada de dados (cálculo);")
  print("2. Saída de dados (imprimir);")
  print("3. Atualizar dados;")
  print("4. Deleção de dados;")
  print("5. Sair do programa.")
  opcaoEscolhida = int(input("\nEscolha uma opção: "))

  if opcaoEscolhida == 1:
    calcular_insumos()
    break
    # método de calculo
  elif opcaoEscolhida == 2:
    imprimir_dados()
    break
    # método de imprimir dados
  elif opcaoEscolhida == 3:
    atualizar_dados()
    break
    # método de atualizar dados
  elif opcaoEscolhida == 4:
    delecao_dados()
    break
    # método de deleção de dados
  elif opcaoEscolhida == 5:
    print("Saindo do programa...")
    print("Programa finalizado.")
    break
    

# culturaEscolhida = input(f"Informe o tipo de cultura: \n1.{tipoCultura[0]} \n2.{tipoCultura[1]}")

# print(culturaEscolhida)