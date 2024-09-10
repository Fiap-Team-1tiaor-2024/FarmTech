#Instalar um package
install.packages("tidyr", "dplyr")

#Usar o package na aplicacao
library(tidyr)
library(dplyr)

#Remover variavel
rm(valor)
rm(dados)

#Declaracao de variavel
nota1 <- 2
nota2 <- 3
nota3 <- 50

media <- (nota1 + nota2 + nota3)/3
print(media)

#Criar uma lista
lista <- c(1, 2, 3, 4, 5)

#Adicionar novo valor a lista
lista <- c(lista, "Novo valor")
print(lista)

#Para pegar os dados do Python e gerar a estatistica
dados <- data.frame(
  nome = c("Lucas", "Vitor", "Tiago", "Camila", "Natalia"),
  idade = c(18, 24, 32, 13, 17),
  genero = c(0, 0, 0, 1, 1)
)
print(dados)

#Filtrar os dados com a idade maior que 10
dados_filtrados <- dados %>% filter(idade >= 18)
print(dados_filtrados)

#Agrupar esses dados e calcular a media de idade
dados_agrupados <- dados %>% group_by(genero) %>% summarise(media_idade = mean(idade))
print(dados_agrupados)

idade2 <- c(1, 2, 10, 40)

#Calcular desvio
desvio_padrao <- sd(idade2)
print("Desvio padrão é de: ", desvio_padrao)
