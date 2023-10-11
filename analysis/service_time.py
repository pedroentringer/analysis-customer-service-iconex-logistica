import seaborn as sns
import matplotlib.pyplot as plt

def service_time(df):
    # Criando um histograma do tempo de atendimento
    sns.histplot(data=df, x='serviceDaysUntilCompletion', bins=10)
    plt.show()

    # Criando um boxplot do tempo de atendimento por canal
    sns.boxplot(data=df, x='channel', y='serviceDaysUntilCompletion')
    plt.show()

    # Pirâmide de População - Resolvido vs Dias de atendimento
    sns.histplot(data=df, x='serviceDaysUntilCompletion', hue='problemHasBeenSolved', multiple='stack')
    plt.show()



