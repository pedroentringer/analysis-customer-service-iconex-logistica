# missing_values
# Vamos buscar os valores omissos e fazer o tratamento de cada um deles.

import pandas as pd

class MissingValues:
    def __init__(self, df):
        self.df = df

    # search_missing_values
    # Apresenta as colunas com valores omissos e uma contagem dos dados
    # Estes dados serão usados para definir como os valores serão tratados
    def __search_missing_values(self):
        for coln in self.df.columns:
            if self.df[coln].isnull().values.any():
                print("-------------------------------------")
                print(f'Coluna "{coln}" possuí valores omissos')
                print(">> Dados da coluna:")
                print(self.df[coln].value_counts())


    # fix_actor
    # Essta função vai corrigir os valores omissos para a coluna "actor"
    # Baseado na proporção, vamos definir como "sender" os valores omissos
    def __fix_actor(self):
        print("-------------------------------------")
        print("Ajustando valores omissos para actor")
        for i, actor in enumerate(self.df["actor"]):
            if pd.isnull(actor):
                self.df.loc[i, "actor"]  = "sender"
                print(f'Linha {i} com valor "null", substituído para "{self.df["actor"][i]}"')

    # fix_channel
    # Essta função vai corrigir os valores omissos para a coluna "channel"
    # Usaremos duas regras para definir o "channel":
    # 1) Se o cliente for W2W E-COMMERCE DE VINHOS S/A vamos usar o "salesforce", pois só ele usa essa ferrameta e também baseado na proporção
    # 2) Para os demais, vamos definir como "email" baseado na proporção
    def __fix_channel(self):
        print("-------------------------------------")
        print("Ajustando valores omissos para channel")
        for i, channel in enumerate(self.df["channel"]):
            if pd.isnull(channel):
                client = self.df["order.sender"][i]
                self.df.loc[i, "channel"] = "salesforce" if client == "W2W E-COMMERCE DE VINHOS S/A" else "email"
                print(f'Linha {i} com valor "null", substituído para "{self.df["channel"][i]}", para o cliente "{client}"')

    # fix_order_finish
    # Essta função vai corrigir os valores omissos para a coluna "order.isFinish"
    # Vamos validar se foi finalizado ou não usando a coluna "order.status"
    def __fix_order_finish(self):
        print("-------------------------------------")
        print("Ajustando valores omissos para order.isFinish")
        for i, order_is_finish in enumerate(self.df["order.isFinish"]):
            if pd.isnull(order_is_finish):
                order_status = self.df["order.status"][i]
                self.df.loc[i, "order.isFinish"] = True if order_status == "ENTREGA REALIZADA - ICONEX" else False
                print(f'Linha {i} com valor "null", substituído para "{self.df["order.isFinish"][i]}", para o status "{order_status}"')

    # fix_client_rating
    # Essta função vai corrigir os valores omissos para a coluna "clientRating"
    # Como os valores omissos são apenas para problemas não resolvidos, vamos supor que o cliente ficou muito insatisfeito e por isso não avaliou
    def __fix_client_rating(self):
        print("-------------------------------------")
        print("Ajustando valores omissos para clientRating")
        for i, client_rating in enumerate(self.df["clientRating"]):
            if pd.isnull(client_rating):
                self.df.loc[i, "clientRating"] = 1
                print(f'Linha {i} com valor "null", substituído para "{self.df["clientRating"][i]}"')

    def fix_all(self):
        self.__search_missing_values()
        self.__fix_actor()
        self.__fix_channel()
        self.__fix_order_finish()
        self.__fix_client_rating()
        return self.df


