install.packages("tidyr")
install.packages("dplyr")

library(tidyr)
library(dplyr)

setwd("C:/Users/gsrxy/PycharmProjects/FarmTech/src/farm-tech/csv")

data <- read.csv("teste.csv", fileEncoding = "UTF-8", sep = ";", fill = TRUE)

dados_filtrados <- data %>%  group_by(CULTURA) %>% summarize(MEDIA_AREA = mean(AREA))
dados_filtrados2 <- data %>%  group_by(CULTURA) %>% summarize(MEDIA_CUSTO = mean(CUSTO.DE.PRODUCAO))

print(dados_filtrados)
print(dados_filtrados2)
