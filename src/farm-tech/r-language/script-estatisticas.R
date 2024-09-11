install.packages("dplyr")

# Carregar pacote dplyr para manipulação de dados
library(dplyr)

# Especificar o caminho do arquivo
dados_path <- "C:/Dev/Projetos/farmtech-solutions/src/farm-tech/csv/teste.csv"

# Tentar ler o arquivo usando read.csv com especificações extras
dados <- tryCatch({
  read.csv(dados_path, fileEncoding = "UTF-8", sep = ",", fill = TRUE, na.strings = c("", "NA"))
}, warning = function(w) {
  message("Aviso: ", w$message)
  return(NULL)
}, error = function(e) {
  message("Erro ao ler o arquivo: ", e$message)
  return(NULL)
})

# Verificar se os dados foram carregados corretamente
if (is.null(dados)) {
  message("Tentando com codificação Latin1 devido a falha com UTF-8...")
  dados <- read.csv(dados_path, fileEncoding = "Latin1", sep = ",", fill = TRUE, na.strings = c("", "NA"))
  if (is.null(dados)) {
    stop("Os dados não foram carregados. Verifique o caminho do arquivo e o formato do arquivo.")
  }
}

# Mostrar as primeiras linhas para confirmar a leitura correta
print("Primeiras linhas dos dados:")
print(head(dados))

# Checar os nomes das colunas para garantir que as operações seguintes sejam corretas
print("Nomes das colunas:")
print(colnames(dados))

# Remover linhas com valores NA nas colunas usadas para cálculos
# Assegure-se de que os nomes das colunas estão corretos
if ("Área" %in% colnames(dados) && "Insumos Necessários" %in% colnames(dados)) {
  dados <- dados %>%
    filter(!is.na(Área), !is.na(`Insumos Necessários`))
  
  # Calcular estatísticas gerais
  estatisticas_gerais <- dados %>%
    summarise(
      Media_Area = mean(Área, na.rm = TRUE),
      Desvio_Area = sd(Área, na.rm = TRUE),
      Media_Insumos = mean(`Insumos Necessários`, na.rm = TRUE),
      Desvio_Insumos = sd(`Insumos Necessários`, na.rm = TRUE)
    )
  
  # Imprimir estatísticas gerais
  print("Estatísticas Gerais:")
  print(estatisticas_gerais)
} else {
  print("Colunas necessárias para cálculos não foram encontradas.")
}
