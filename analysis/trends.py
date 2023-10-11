import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

def __order_timeline(df):
    # Convertendo a coluna 'createdAt' para formato datetime
    df['createdAt'] = pd.to_datetime(df['createdAt'])

    # Agrupando por dia e contando o número de pedidos
    pedidos_por_dia = df.groupby(pd.Grouper(key='createdAt', freq='D')).size().reset_index(name='num_pedidos')

    # Criando um gráfico de linha com o número de pedidos ao longo do tempo
    sns.lineplot(data=pedidos_por_dia, x='createdAt', y='num_pedidos')
    plt.show()

def __contacts_by_sender(df):
    # Agrupando por cliente e contando o número de pedidos
    pedidos_por_cliente = df.groupby('order.sender').size().reset_index(name='num_pedidos')

    # Ordenando por número de pedidos e selecionando os 10 primeiros
    top_10_clientes = pedidos_por_cliente.sort_values(by='num_pedidos', ascending=False).head(10)

    # Criando um gráfico de barras com a quantidade de pedidos por cliente
    sns.barplot(data=top_10_clientes, x='num_pedidos', y='order.sender')
    plt.show()

    # Criando um histograma do peso dos pedidos por canal
    sns.histplot(data=df, x='order.weight', hue='channel', bins=10)
    plt.show()

def __time_series_to_completion(df):
    # Convertendo a coluna 'createdAt' para formato datetime
    df['createdAt'] = pd.to_datetime(df['createdAt'])

    # Criando uma série temporal dos dias de serviço até a conclusão
    series_temporal = df.groupby(pd.Grouper(key='createdAt', freq='D')).size().reset_index(
        name='num_pedidos')
    series_temporal = series_temporal.set_index('createdAt').asfreq('D')

    print(series_temporal)

    # Decompondo a série temporal em tendência, sazonalidade e resíduo
    decomposicao = sm.tsa.seasonal_decompose(series_temporal, model='additive')

    # Plotando a decomposição
    fig, ax = plt.subplots(4, 1, figsize=(10, 10))
    ax[0].set_title('Série Temporal dos Dias de Serviço Até a Conclusão')
    series_temporal.plot(ax=ax[0])
    ax[1].set_title('Tendência')
    decomposicao.trend.plot(ax=ax[1])
    ax[2].set_title('Sazonalidade')
    decomposicao.seasonal.plot(ax=ax[2])
    ax[3].set_title('Resíduo')
    decomposicao.resid.plot(ax=ax[3])

    plt.tight_layout()
    plt.show()

def __resolution_rate(df):
    # converter a coluna 'createdAt' em um objeto de data e hora
    df['createdAt'] = pd.to_datetime(df['createdAt'])

    # formatar a coluna 'createdAt' no formato 'ano-mês'
    df['resolution_rate_period'] = df['createdAt'].dt.strftime('%Y-%m')

    sns.set_style("whitegrid")
    plt.figure(figsize=(12, 6))
    plt.title("Taxa de Resolução de Problemas ao Longo do Tempo", fontsize=16)
    sns.lineplot(data=df, x="resolution_rate_period", y="problemHasBeenSolved", estimator="mean")
    plt.xlabel("Data de Criação", fontsize=14)
    plt.ylabel("Taxa de Resolução de Problemas", fontsize=14)
    plt.show()

def trends(df):
    __order_timeline(df)
    __contacts_by_sender(df)
    __time_series_to_completion(df)
    __resolution_rate(df)







