import math
import csv

# Dados em Vetores
culturas = ["Cafe", "Soja"]
areas = [100, 200]
quantidadesInsumos = [2000.0, 3000.0]
custosProducao = [300.00, 500.00, 400.00]
tiposInsumos = ["Fosfato", "Nitrogenio"]

# Métodos para calcular as formas geométricas
def area_circulo(raio, pi):
    pi = math.pi
    return pi * raio ** 2,


def area_retangulo(base, altura):
    return base * altura


def calcular_insumos(area, quantidade):
    return area * quantidade


# Métodos para opções
def calcular_area():
    cultura = input("Informe a cultura para o para o plantio:")
    culturas.append(cultura)

    # ----- VOLTAR A USAR ESSES DADOS FICTICIOS QUANDO ESTIVERMOS COM PY + R OK -----
    # maoDeObra = float(input("Informe o valor/hora gasto: \n(Café - Hora R$30, Soja - Hora R$25): "))
    # horasExecucao = int(input("Digite a quantidade de horas executadas por m²: \n(Café - Hora 1h30min 1Soja - Hora 1h): "))

    # totalProduzido = maoDeObra * horasExecucao
    # custoProducao.append(totalProduzido)

    print("Informe o tipo de figura geométrica para o plantio:")
    print("1. Círculo;")
    print("2. Retângulo;")

    formaGeometrica = int(input("Escolha uma opção: "))

    comprimento = float(input("Informe o comprimento da área do plantio: "))
    largura = float(input("Agora informe a largura da área do plantio: "))
    quantidadeInsumo = float(input("Informe a quantidade de insumo: "))
    tipodeInsumo = input("Informe a tipo de insumo: ")

    if formaGeometrica == 1:
        raio = float(input("Informe a área do raio: "))
        area = area_circulo(raio, math.pi)
    elif formaGeometrica == 2:
        area = area_retangulo(largura, comprimento)

    insumo = calcular_insumos(area, quantidadeInsumo)

    quantidadesInsumos.append(insumo)
    areas.append(area)
    tiposInsumos.append(tipodeInsumo)

    print(f"A cultura escolhida foi {cultura}.")
    print(f"A área do plantio é: {area:.2f} m².")
    print(f"A quantidade de {tipodeInsumo} necessário é de: {insumo:.2f} mL.")
    print("------------------(Retornando ao menu...)------------------\n")


def imprimir_dados():
    print("------------------(Dados imprimidos)------------------")
    print("Índice | Cultura | Área  | Insumos | Tipo Insumos")
    print("------------------")

    with open('./src/farm-tech/csv/teste.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Cultura", "Area", "Insumo", "Tipo de insumo", "Custo de producao"])

        for i, (cultura, area, insumo, tipoInsumo, custoProducao) in enumerate(
                zip(culturas, areas, quantidadesInsumos, tiposInsumos, custosProducao), start=1):
            print(f"{i:6d} | {cultura} | {area:6.2f} | {insumo:7.2f} | {tipoInsumo}")
            writer.writerow([cultura, area, insumo, tipoInsumo, custoProducao])


def atualizar_dados():
    index = int(input("Digite o índice que você quer atualizar: ")) - 1
    if 0 <= index < len(areas):
        novoComprimento = float(input("Informe o novo valor do comprimento: "))
        novaLargura = float(input("Informe o novo valor da largura: "))
        novaQuantidadeInsumo = float(input("Digite a nova quantidade de insumo: "))

        novoValorArea = area_retangulo(novaLargura, novoComprimento)
        novoValorInsumo = calcular_insumos(novoValorArea, novaQuantidadeInsumo)

        areas[index] = novoValorArea
        quantidadesInsumos[index] = novoValorInsumo

        print("Dados atualizados com sucesso!")
        print(f"A nova área é de: {areas[index]:.2f} m².")  # Acessa o valor específico da lista
        print(f"A nova quantidade de insumo é de: {quantidadesInsumos[index]:.2f} mL.")  # Acessa o valor específico da lista
    else:
        print("Erro!")


def delecao_dados():
    index = int(input("Informe o index que você quer excluir: ")) - 1
    if 0 <= index < len(areas):
        areas.pop(index)
        quantidadesInsumos.pop(index)
        tiposInsumos.pop(index)

        print(areas)
        print(quantidadesInsumos)
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
