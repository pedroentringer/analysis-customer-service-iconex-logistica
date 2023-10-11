import seaborn as sns
import matplotlib.pyplot as plt

def exploratory(df):
    # Verificando as primeiras linhas do conjunto de dados
    print(df.head())

    # Verificando o tamanho do conjunto de dados
    print(df.shape)

    # Verificando as informações dos dados
    print(df.info())

    # Verificando as estatísticas descritivas do conjunto de dados
    print(df.describe())

    # Contagem dos valores e ordenação dos 5 maiores
    macro_counts = df['macroMotive'].value_counts().head(5)

    # Barras de motivos macros
    sns.barplot(x=macro_counts.values, y=macro_counts.index, order=macro_counts.index, palette='viridis')
    plt.title('Top 5 Macro Motives')
    plt.xlabel('Count')
    plt.ylabel('Macro Motive')
    plt.show()

    # Contagem dos valores e ordenação dos 5 maiores
    micro_counts = df['microMotive'].value_counts().head(5)

    # Barras de motivos micros
    sns.barplot(x=micro_counts.values, y=micro_counts.index, order=micro_counts.index, palette='viridis')
    plt.title('Top 5 Micro Motives')
    plt.xlabel('Count')
    plt.ylabel('Macro Motive')
    plt.show()

    # Filtro dos dados pelo MacroMotive específico
    filtered_data = df[df['macroMotive'] == 'Atualização do pedido']

    # Contagem dos valores e ordenação dos 5 maiores
    counts = filtered_data['microMotive'].value_counts().head(5)

    # Criação do gráfico de barras horizontal
    sns.barplot(x=counts.values, y=counts.index, order=counts.index, palette='viridis')
    plt.title('Top 5 Micro Motives for Macro Motive: Atualização do pedido')
    plt.xlabel('Count')
    plt.ylabel('Micro Motive')
    plt.show()

    # Barras de Canal
    sns.countplot(x='channel', data=df)
    plt.show()

    # Barras de Ator
    sns.countplot(x='actor', data=df)
    plt.show()

    # Histograma - Dias de atendimento
    sns.histplot(data=df, x='serviceDaysUntilCompletion')
    plt.show()

    # Visualizando a distribuição da satisfação do cliente
    sns.histplot(data=df, x='clientRating')
    plt.show()


