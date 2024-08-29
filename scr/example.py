# Definindo as culturas
culturas = ["Café", "Cana-de-açúcar"]

# Vetores para armazenar os dados
areas = []
insumos = []


def calcular_area(comprimento, largura):
    return comprimento * largura


def calcular_insumos(area, dosagem):
    return area * dosagem


def menu():
    print("\nMenu de Opções:")
    print("1. Entrada de dados")
    print("2. Saída de dados")
    print("3. Atualização de dados")
    print("4. Deleção de dados")
    print("5. Sair do programa")


def entrada_dados():
    cultura = input("Escolha a cultura (Café/Cana-de-açúcar): ")
    comprimento = float(input("Comprimento da área (m): "))
    largura = float(input("Largura da área (m): "))
    dosagem = float(input("Dosagem de insumo por metro quadrado (mL): "))

    area = calcular_area(comprimento, largura)
    insumo = calcular_insumos(area, dosagem)

    areas.append(area)
    insumos.append(insumo)

    print(f"Área de plantio para {cultura}: {area} m²")
    print(f"Quantidade de insumo necessária: {insumo} mL")


def saida_dados():
    for i, (area, insumo) in enumerate(zip(areas, insumos)):
        print(f"{i + 1}. Área: {area} m², Insumo: {insumo} mL")


def atualizar_dados():
    index = int(input("Escolha o índice do dado a ser atualizado: ")) - 1
    if 0 <= index < len(areas):
        comprimento = float(input("Novo comprimento da área (m): "))
        largura = float(input("Nova largura da área (m): "))
        dosagem = float(input("Nova dosagem de insumo por metro quadrado (mL): "))

        area = calcular_area(comprimento, largura)
        insumo = calcular_insumos(area, dosagem)

        areas[index] = area
        insumos[index] = insumo

        print("Dados atualizados com sucesso!")
    else:
        print("Índice inválido!")


def deletar_dados():
    index = int(input("Escolha o índice do dado a ser deletado: ")) - 1
    if 0 <= index < len(areas):
        areas.pop(index)
        insumos.pop(index)
        print("Dados deletados com sucesso!")
    else:
        print("Índice inválido!")


while True:
    menu()
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        entrada_dados()
    elif opcao == 2:
        saida_dados()
    elif opcao == 3:
        atualizar_dados()
    elif opcao == 4:
        deletar_dados()
    elif opcao == 5:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida! Tente novamente.")