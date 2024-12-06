# Projeto FarmTech - Sistema de Monitoramento e Modelagem Preditiva

Este projeto integra um sistema de monitoramento de sensores para agricultura de precisão utilizando ESP32 e um sistema de modelagem preditiva com Python, Scikit-learn, e Plotly. 

## Funcionalidades
1. **Monitoramento em Tempo Real com ESP32**:
   - Sensores DHT22 para umidade.
   - LDR para intensidade luminosa.
   - Botões representando sensores de Fósforo (P) e Potássio (K).
   - Relé para ativar/desativar uma bomba de irrigação.
   - Exibição dos dados em um display LCD.

2. **Modelagem Preditiva com Python e Scikit-learn**:
   - Treinamento de modelos de Regressão Linear, KNN, e Árvore de Decisão.
   - Visualização de gráficos interativos utilizando Plotly.
   - Interface FastAPI para exibição de resultados.

3. **Monitoramento no Serial Plotter**:
   - Demonstração do uso do Serial Plotter para acompanhamento de variáveis.

---

## Estrutura do Projeto

### Código Python - Modelagem Preditiva e Interface
- Requisitos: 
  - `Python 3.9+`
  - Bibliotecas: `fastapi`, `pandas`, `scikit-learn`, `plotly`, `uvicorn`

#### Execução
1. Instale as dependências:
   ```bash
   pip install fastapi pandas scikit-learn plotly uvicorn

2. Execute o servidor:
  ```bash
  uvicorn main:app --
  ```
3. Acesse a interface interativa:
  Gráficos: http://localhost:8000
  Previsões: http://localhost:8000/predict

### Código C/C++ - Monitoramento com ESP32

Sensores monitorados:
 - Umidade (DHT22);
 - Intensidade luminosa (LDR);
 - Fósforo (P) e Potássio (K) (botões simulados)

Critérios para irrigação:
 - Umidade abaixo de 50%.
 - Detecção de Fósforo ou Potássio.
 - Baixa intensidade luminosa (LDR abaixo de 2000).

Otimizações Implementadas:
 - Configuração eficiente do display LCD.
 - Controle lógico do relé com base em critérios de múltiplos sensores.
 - Intervalo de leitura ajustável para economia de recursos.


### Fluxo do Projeto

Monitoramento de Sensores:
 - O ESP32 coleta os dados dos sensores e toma decisões sobre irrigação.
 - Os dados são exibidos no LCD e enviados ao Serial Plotter para análise.

Modelagem Preditiva:
 - Os dados históricos são usados para treinar modelos de regressão.
 - A interface exibe gráficos interativos de análise.
