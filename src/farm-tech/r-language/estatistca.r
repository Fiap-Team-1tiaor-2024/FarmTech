install.packages("tidyr")
install.packages("dplyr")

library(tidyr)
library(dplyr)

getwd()

setwd("C:/Dev/Projetos/farmtech-solutions/src/farm-tech/csv")

data <- read.csv("teste.csv", fileEncoding = "UTF-8", sep = ";", fill = TRUE)

dados_filtrados <- data %>%  group_by(AREA) %>% summarize(AREA_TOTAL = mean(AREA))
print(dados_filtrados)
