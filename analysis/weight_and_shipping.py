import seaborn as sns
import matplotlib.pyplot as plt

def weight_and_shipping(df):
    # Criando um scatterplot do peso vs. frete
    sns.scatterplot(data=df, x='order.weight', y='order.freight')
    plt.show()

    # Criando um boxplot do frete por cidade
    sns.boxplot(data=df, x='order.uf', y='order.freight')
    plt.xticks(rotation=90)
    plt.show()




