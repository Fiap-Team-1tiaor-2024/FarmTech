import math

# Dados em Vetores
cultura = []
areas = []
insumos = []

# Métodos para calcular as formas geométricas
# ---POSSIVEL MELHORIA: colocar as informações da area diretamente no metodo das formas---
def area_circulo(raio, pi):
  pi = math.pi
  return pi * raio ** 2

def area_retangulo(base, altura):
  return base * altura 

def area_triangulo(base, altura):
  return (base * altura) / 2

def calcular_insumos(area, quantidade):
  return area * quantidade

# Métodos para opções
def calcular_area():
  print("Informe o tipo de figura geométrica para o plantio:")
  print("1. Círculo;")
  print("2. Retângulo;")
  print("3. Triângulo.")
  
  formaGeometrica = int(input("Escolha uma opção: "))

  comprimento = float(input("Informe o comprimento da área do plantio: "))
  largura = float(input("Agora informe a largura da área do plantio: "))
  quantidadeInsumo = float(input("Informe a quantidade de insumo: "))

  if formaGeometrica == 1:
    raio = float(input("Informe a área do raio: "))
    area = area_circulo(raio, math.pi)
  elif formaGeometrica == 2:
    area = area_retangulo(largura, comprimento)
  elif formaGeometrica == 3:
    area = area_triangulo(largura, comprimento)

  insumo = calcular_insumos(area, quantidadeInsumo)
  
  insumos.append(insumo)
  areas.append(area)

  print(f"A área do plantio é: {area:.2f} m².")
  print(f"A quantidade de insumos necessário é de: {insumo:.2f} mL.")
  print("------------------(Retornando ao menu...)------------------")

def imprimir_dados():
  print("------------------(Dados imprimidos)------------------")
  print("Índice | Área  | Insumos")
  print("------------------")
  
  for i, (area, insumo) in enumerate(zip(areas, insumos), start=1):
    print(f"{i:6d} | {area:6.2f} | {insumo:7.2f}")

def atualizar_dados():
  index = int(input("Digite o índice que você quer atualizar: ")) - 1
  if 0 <= index < len(areas):
    novoComprimento = float(input("Informe o novo valor do comprimento: "))
    novaLargura = float(input("Informe o novo valor da largura: "))
    novaQuantidadeInsumo = float(input("Digite a nova quantidade de insumo: "))

    novoValorArea = area_retangulo(novaLargura, novoComprimento)
    novoValorInsumo = calcular_insumos(novoValorArea, novaQuantidadeInsumo)

    areas[index] = novoValorArea
    insumos[index] = novoValorInsumo

    print("Dados atualizados com sucesso!")
    print(f"A nova área é de: {areas[index]:.2f} m².")  # Acessa o valor específico da lista
    print(f"A nova quantidade de insumo é de: {insumos[index]:.2f} mL.")  # Acessa o valor específico da lista
  else:
    print("Erro!")
 
def delecao_dados():
  index = int(input("Informe o index que você quer excluir: ")) - 1
  if 0 <= index < len(areas):
    areas.pop(index)
    insumos.pop(index)
      
    print(areas)
    print(insumos)
    print("Dados excluídos.")

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
    calcular_area()
  elif opcaoEscolhida == 2:
    imprimir_dados()
  elif opcaoEscolhida == 3:
    atualizar_dados()
  elif opcaoEscolhida == 4:
    delecao_dados()
  elif opcaoEscolhida == 5:
    print("Saindo do programa...")
    print("Programa finalizado.")
    break
  else:
    print("Erro!")