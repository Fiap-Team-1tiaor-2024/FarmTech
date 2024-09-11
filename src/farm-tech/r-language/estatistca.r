install.packages("tidyr")
install.packages("dplyr")
install.packages("gridExtra")

library(tidyr)
library(dplyr)
library(gridExtra)

setwd("C:/Users/gsrxy/PycharmProjects/FarmTech/src/farm-tech/csv")

data <- read.csv("teste.csv", fileEncoding = "UTF-8", sep = ";", fill = TRUE)

media_area <- data %>%  group_by(Cultura) %>% summarize(MEDIA_AREA = mean(Area))
media_producao <- data %>%  group_by(Cultura) %>% summarize(MEDIA_CUSTO = mean(Custo.de.producao))
media_insumo <- data %>%  group_by(Tipo.de.insumo) %>% summarize(MEDIA_CUSTO = mean(Insumo))

grid.table(media_area)
grid.table(media_producao)
grid.table(media_insumo)

desvio_area <- data %>%  group_by(Cultura) %>% summarize(DESVIO_AREA = sd(Area))
desvio_producao <- data %>%  group_by(Cultura) %>% summarize(DESVIO_CUSTO = sd(Custo.de.producao))
desvio_insumo <- data %>%  group_by(Tipo.de.insumo) %>% summarize(DESVIO_CUSTO = sd(Insumo))

grid.table(desvio_area)
grid.table(desvio_producao)
grid.table(desvio_insumo)
      
      
      
      