from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import plotly.graph_objects as go
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    # Ler o arquivo CSV
    df = pd.read_csv('C:/Dev/Projetos/FIAP/FarmTech/src/fase4/py/csv/estrutura_tabelas.csv', delimiter=';')

    # Extrair as colunas para os gráficos
    area_total = df['area_total'].tolist()
    qtde_insumo_total = df['qtde_insumo_total'].tolist()
    valor_medido = df['valor_medido'].tolist()
    latitude_plantio = df['latitude_plantio'].tolist()

    # Criar um gráfico de Área Total vs Quantidade de Insumo Total
    fig_area_insumo = go.Figure(
        data=[go.Scatter(x=area_total, y=qtde_insumo_total, mode='markers')],
        layout=go.Layout(title="Área Total vs Quantidade de Insumo Total", xaxis=dict(title="Área Total"), yaxis=dict(title="Quantidade de Insumo Total"))
    )

    # Criar um gráfico de Valor Medido vs Latitude do Plantio
    fig_valor_latitude = go.Figure(
        data=[go.Scatter(x=latitude_plantio, y=valor_medido, mode='markers')],
        layout=go.Layout(title="Valor Medido vs Latitude do Plantio", xaxis=dict(title="Latitude do Plantio"), yaxis=dict(title="Valor Medido"))
    )

    # Obter o HTML dos gráficos
    area_insumo_html = fig_area_insumo.to_html(full_html=False)
    valor_latitude_html = fig_valor_latitude.to_html(full_html=False)

    # Combinar os HTMLs dos gráficos
    combined_html = f"""
    <html>
        <head>
            <title>Gráficos</title>
        </head>
        <body>
            <h1 style="font-family: sans-serif;">Comparativos de gráficos de Dispersão e Linha.</h1>
            <p style="font-size: 1.2rem; font-family: sans-serif;">Para ver a modelagem preditiva com o Scikit Learn, clique <a href="/predict">aqui.</a></p>
            {area_insumo_html}
            <hr>
            {valor_latitude_html}
        </body>
    </html>
    """

    return HTMLResponse(content=combined_html)

@app.get("/predict", response_class=HTMLResponse)
async def predict():
    # Ler o arquivo CSV
    df = pd.read_csv('C:/Dev/Projetos/FIAP/FarmTech/src/fase4/py/csv/estrutura_tabelas.csv', delimiter=';')

    # Selecionar as features e o target
    X = df[['area_total', 'latitude_plantio', 'longitude_plantio', 'qtde_insumo_total']]
    y = df['valor_medido']

    # Dividir os dados em treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o modelo Linear Regression
    lr_model = LinearRegression()
    lr_model.fit(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)
    mse_lr = mean_squared_error(y_test, y_pred_lr)

    # Treinar o modelo KNN
    knn_model = KNeighborsRegressor(n_neighbors=5)
    knn_model.fit(X_train, y_train)
    y_pred_knn = knn_model.predict(X_test)
    mse_knn = mean_squared_error(y_test, y_pred_knn)

    # Treinar o modelo Decision Tree
    dt_model = DecisionTreeRegressor(random_state=42)
    dt_model.fit(X_train, y_train)
    y_pred_dt = dt_model.predict(X_test)
    mse_dt = mean_squared_error(y_test, y_pred_dt)

    # Criar gráficos de dispersão das previsões
    fig_pred_lr = go.Figure(
        data=[go.Scatter(x=y_test, y=y_pred_lr, mode='markers')],
        layout=go.Layout(title="Previsões vs Valores Reais - Linear Regression", xaxis=dict(title="Valores Reais"), yaxis=dict(title="Previsões"))
    )

    fig_pred_knn = go.Figure(
        data=[go.Scatter(x=y_test, y=y_pred_knn, mode='markers')],
        layout=go.Layout(title="Previsões vs Valores Reais - KNN", xaxis=dict(title="Valores Reais"), yaxis=dict(title="Previsões"))
    )

    fig_pred_dt = go.Figure(
        data=[go.Scatter(x=y_test, y=y_pred_dt, mode='markers')],
        layout=go.Layout(title="Previsões vs Valores Reais - Decision Tree", xaxis=dict(title="Valores Reais"), yaxis=dict(title="Previsões"))
    )

    # Obter o HTML dos gráficos
    pred_html_lr = fig_pred_lr.to_html(full_html=False)
    pred_html_knn = fig_pred_knn.to_html(full_html=False)
    pred_html_dt = fig_pred_dt.to_html(full_html=False)

    # Combinar o HTML dos gráficos com os MSEs
    combined_html = f"""
    <html>
        <head>
            <title>Previsões</title>
        </head>
        <body>
            <h1 style="font-family: sans-serif;">Modelo Preditivo com Scikit Learn - KNN, Árvore de Decisão & Regressão Linear</h1>
            {pred_html_lr}
            <h2 style="font-size: 1.2rem; font-family: sans-serif;">Erro Quadrático Médio (Linear Regression): {mse_lr}</h2>
            <hr>
            <h1 style="font-family: sans-serif;">Previsões vs Valores Reais - KNN</h1>
            {pred_html_knn}
            <h2 style="font-size: 1.2rem; font-family: sans-serif;">Erro Quadrático Médio (KNN): {mse_knn}</h2>
            <hr>
            <h1 style="font-family: sans-serif;">Previsões vs Valores Reais - Decision Tree</h1>
            {pred_html_dt}
            <h2 style="font-size: 1.2rem; font-family: sans-serif;">Erro Quadrático Médio (Decision Tree): {mse_dt}</h2>
        </body>
    </html>
    """

    return HTMLResponse(content=combined_html)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)