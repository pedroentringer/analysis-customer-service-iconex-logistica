import seaborn as sns
import matplotlib.pyplot as plt

def correlation(df):
    # Calculando a matriz de correlação
    corr_matrix = df.corr(numeric_only=True)

    # Visualizando a matriz de correlação
    sns.heatmap(corr_matrix, annot=True)
    plt.show()

    # Visualizando a relação entre tempo de atendimento e valor do frete
    sns.scatterplot(data=df, x='serviceDaysUntilCompletion', y='order.freight')
    plt.show()

    # Outra visão da relação entre tempo de atendimento e valor do frete
    sns.lmplot(x='serviceDaysUntilCompletion', y='order.freight', data=df)
    plt.show()

    # Visualizando a relação entre satisfação do cliente e valor do frete
    sns.scatterplot(data=df, x='clientRating', y='order.freight')
    plt.show()

    # Visualizando a relação entre a duração do serviço e a satisfação do cliente
    sns.scatterplot(data=df, x='serviceDaysUntilCompletion', y='clientRating')
    plt.show()