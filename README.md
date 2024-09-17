# FarmTech Solutions - Aplicação de Agricultura Digital 🌱
Este projeto foi desenvolvido como parte de um exercício acadêmico voltado para a implementação de uma aplicação que auxilia na transição para a Agricultura Digital. A aplicação foi criada em Python para realizar cálculos de área de plantio, gestão de insumos e organizar dados de diferentes culturas agrícolas. Além disso, integra-se com R para cálculos estatísticos, como média e desvio padrão. O sistema conta com um menu interativo para entrada, atualização, exclusão e visualização de dados, garantindo flexibilidade na manipulação das informações.

# Funcionalidades 🎯
- **Suporte a múltiplas culturas**: A aplicação oferece suporte a duas culturas agrícolas, definidas de acordo com as principais demandas regionais.
- **Cálculo de área de plantio**: Calcula a área de plantio de acordo com a geometria definida para cada cultura.
- **Manejo de insumos**: Realiza o cálculo de insumos necessários, considerando tipo de cultura, insumos aplicados e área de plantio.
- **Menu interativo**: Permite a entrada, atualização, deleção e visualização de dados.
- **Análise estatística**: Dados coletados são processados em R para cálculos de média e desvio padrão.

# Passos para executar o projeto 👨🏽‍💻
Para o projeto funcionar da maneira que esperamos, recomendamos seguir os seguintes passos:

1. Clonar o projeto em um **lugar de fácil acesso**.
  
2. Para o programa fluir da melhor maneira, primeiro faça o **cálculo da area/insumos**, depois **imprima os dados para gerar o CSV** e exclua/atualize os dados.
   
3. Se o programa não imprimir o CSV, vá no código e deixe o caminho para gerar o CSV limpo.
   
![image](https://github.com/user-attachments/assets/c84dfd7a-04c3-4b99-8e0c-d2e716b35f5a)

4. Após isso, vá para o arquivo **estatisticas.R** para poder calcular a media e desvio.
   
5. Defina o caminho de arquivo de acordo com que está na sua máquina para o programa ler os dados CSV e calcular a média e desvio.
   
![image](https://github.com/user-attachments/assets/47076878-38f1-4037-ae3b-378dbb48d7b4)

6. Por padrão deixamos **vários dados** no arquivo CSV para poder calcular o desvio, pois com poucos dados não é possível calcular o desvio no R.

7. Quando realizado o cálculo no programa do Python, **para exibir e atualizar** a planilha basta escolhar a opção para imprimir os dados.

**Extra:** Se caso não ouver o Excel na sua máquina e você quiser visualizar o CSV no próprio VS Code, recomendamos instalar o **Rainbow CSV** para a melhor visualização dos dados gerados.

![image](https://github.com/user-attachments/assets/a8062d0c-8e70-4feb-8c21-178bcfb11510)


O projeto foi desenvolvido utilizando GitHub para versionamento, promovendo um ambiente colaborativo de desenvolvimento entre os colaboradores do projeto.
