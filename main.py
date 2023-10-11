# install packages
# seaborn
# pandas
# matplotlib
# statsmodels
# openpyxl
import numpy as np

import pandas as pd
import seaborn as sns
from utils.missing_values import MissingValues
from analysis import *

# Lendo o arquivo Excel com o Pandas
df = pd.read_excel("./datasets/contacts.xlsx")

# Remover colunas não usadas
df.drop(['newDeadline'], axis=1, inplace=True)


macro_motive_days = {}
macro_motive_median = {}


def fn_counts(row):
    macro_motive = row['macroMotive']
    days = row['serviceDaysUntilCompletion']

    if macro_motive not in macro_motive_days:
        macro_motive_days[macro_motive] = []

    macro_motive_days[macro_motive].append(days)


def get_median():
    for key in macro_motive_days:
        macro_motive_median[key] = np.median(macro_motive_days[key])


df.apply(lambda x: fn_counts(x), axis=1)
get_median()
print(macro_motive_median)
exit(0)

# Tratando valores omissos
missing_values = MissingValues(df)
df_fixed = missing_values.fix_all()

# Define o tamanho das imagens geradas
sns.set(rc={'figure.figsize':(11.7,8.27)})

# Iniciando as análises
exploratory(df_fixed)
correlation(df_fixed)
customer_satisfaction(df_fixed)
service_time(df_fixed)
weight_and_shipping(df_fixed)
trends(df_fixed)


