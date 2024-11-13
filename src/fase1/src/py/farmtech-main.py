import math
import csv

# Lista de culturas disponíveis
culturasDisponiveis = ["Cafe", "Soja"]

# Dados em Vetores - Dados por padrão para demonstração
culturas = ["Cafe", "Soja"]
areas = [100, 200]
quantidadesInsumos = [2000.0, 3000.0]
custosProducao = [300.00, 500.00]
tiposInsumos = ["Fosfato", "Nitrogenio"]

# Métodos para calcular as formas geométricas
def areaCirculo(raio):
    return math.pi * raio ** 2  # Removido a vírgula para retornar um float

def areaRetangulo(base, altura):
    return base * altura

def calcularInsumos(area, quantidade):
    return area * quantidade

# Métodos para opções
def calcularArea():
    print("\nSelecione a cultura para o plantio:")
    for idx, cultura in enumerate(culturasDisponiveis, 1):
        print(f"{idx}. {cultura}")
    opcaoCultura = int(input("Escolha uma opção: "))
    if 1 <= opcaoCultura <= len(culturasDisponiveis):
        cultura = culturasDisponiveis[opcaoCultura - 1]
    else:
        print("Opção inválida.")
        return
    culturas.append(cultura)

    print("\nInforme o tipo de figura geométrica para o plantio:")
    print("1. Círculo")
    print("2. Retângulo")

    formaGeometrica = int(input("Escolha uma opção: "))

    quantidadeInsumo = float(input("Informe a quantidade de insumo por m²: "))
    tipodeInsumo = input("Informe o tipo de insumo: ")

    if formaGeometrica == 1:
        raio = float(input("Informe o valor do raio em metros: "))
        area = areaCirculo(raio)
    elif formaGeometrica == 2:
        comprimento = float(input("Informe o comprimento da área do plantio em metros: "))
        largura = float(input("Agora informe a largura da área do plantio em metros: "))
        area = areaRetangulo(largura, comprimento)
    else:
        print("Opção inválida.")
        return

    insumo = calcularInsumos(area, quantidadeInsumo)

    quantidadesInsumos.append(insumo)
    areas.append(area)
    tiposInsumos.append(tipodeInsumo)

    maoDeObra = float(input("Informe o valor/hora gasto em R$: "))
    horasExecucao = float(input("Digite a quantidade de horas executadas por m²: "))

    totalProduzido = maoDeObra * horasExecucao
    custosProducao.append(totalProduzido)

    print(f"\nA cultura escolhida foi: {cultura}")
    print(f"A área do plantio é: {area:.2f} m²")
    print(f"A quantidade de {tipodeInsumo} necessária é: {insumo:.2f} mL")
    print("------------------(Retornando ao menu...)------------------\n")

# Método para imprimir os dados
def imprimirDados():
    print("\n------------------(Dados imprimidos)------------------")
    print("Índice | Cultura |   Área   |  Insumos  | Tipo Insumos | Custo de Produção")
    print("-------------------------------------------------------------------------")

    with open('./src/farm-tech/csv/dados-planilha.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(["Cultura", "Area", "Insumo", "Tipo de insumo", "Custo de producao"])

        for i, (cultura, area, insumo, tipoInsumo, custoProducao) in enumerate(
                zip(culturas, areas, quantidadesInsumos, tiposInsumos, custosProducao), start=1):
            print(f"{i:6d} | {cultura:7} | {area:8.2f} | {insumo:9.2f} | {tipoInsumo:12} | R$ {custoProducao:.2f}")
            writer.writerow([cultura, area, insumo, tipoInsumo, custoProducao])

    print("\nDados exportados para 'dados-planilha.csv'.\n")

# Método para atualizar dados
def atualizarDados():
    index = int(input("Digite o índice que você quer atualizar: ")) - 1
    if 0 <= index < len(areas):
        print("\nAtualizando dados para a cultura:", culturas[index])
        novoComprimento = float(input("Informe o novo valor do comprimento em metros: "))
        novaLargura = float(input("Informe o novo valor da largura em metros: "))
        novaQuantidadeInsumo = float(input("Digite a nova quantidade de insumo por m²: "))

        novoValorArea = areaRetangulo(novaLargura, novoComprimento)
        novoValorInsumo = calcularInsumos(novoValorArea, novaQuantidadeInsumo)

        areas[index] = novoValorArea
        quantidadesInsumos[index] = novoValorInsumo

        print("\nDados atualizados com sucesso!")
        print(f"A nova área é de: {areas[index]:.2f} m²")
        print(f"A nova quantidade de insumo é de: {quantidadesInsumos[index]:.2f} mL\n")
    else:
        print("Erro: Índice inválido!\n")

# Método para deletar dados
def delecaoDados():
    index = int(input("Informe o índice que você quer excluir: ")) - 1
    if 0 <= index < len(areas):
        print(f"\nExcluindo dados da cultura: {culturas[index]}")
        culturas.pop(index)
        areas.pop(index)
        quantidadesInsumos.pop(index)
        tiposInsumos.pop(index)
        custosProducao.pop(index)

        print("Dados excluídos com sucesso! Imprima os dados para visualizar as alterações.\n")
    else:
        print("Erro: Índice inválido!\n")

# Loop para o menu
while True:
    print("------------------\nMENU\n------------------")
    print("1. Entrada de dados (cálculo)")
    print("2. Saída de dados (imprimir dados e arquivo CSV)")
    print("3. Atualizar dados")
    print("4. Deleção de dados")
    print("5. Sair do programa")

    opcaoEscolhida = int(input("\nEscolha uma opção: "))

    if opcaoEscolhida == 1:
        calcularArea()
    elif opcaoEscolhida == 2:
        imprimirDados()
    elif opcaoEscolhida == 3:
        atualizarDados()
    elif opcaoEscolhida == 4:
        delecaoDados()
    elif opcaoEscolhida == 5:
        print("\nSaindo do programa...")
        print("Programa finalizado.")
        break
    else:
        print("Erro: Opção inválida!\n")
