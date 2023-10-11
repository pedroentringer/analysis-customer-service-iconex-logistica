import seaborn as sns
import matplotlib.pyplot as plt

def customer_satisfaction(df):
    # Criando um histograma da satisfação do cliente
    sns.histplot(data=df, x='clientRating', bins=5)
    plt.show()

    # Criando um boxplot da satisfação do cliente por ator
    sns.boxplot(data=df, x='actor', y='clientRating')
    plt.show()

    # Boxplot - Canal vs satisfação do cliente
    sns.boxplot(x='channel', y='clientRating', data=df)
    plt.show()


