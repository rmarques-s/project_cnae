import pandas as pd

dataframe = pd.read_csv('/home/rafaelamarques/project_cnae/estabelecimentos_RN.csv')

print(dataframe.head())  # Exibe as primeiras linhas do DataFrame
print(dataframe.shape)  # Exibe a forma do DataFrame (número de linhas e colunas)
print(dataframe.describe())  # Exibe estatísticas descritivas do DataFrame

# Salva o dataframe em um arquivo CSV
with open("Desktop\dados.xlsx", "w") as f:
    for row in dataframe.itertuples(index=False):
        cnpj_basico = str(row[0]).ljust(10) 
        cnpj_ordem = str(row[1]).ljust(10)
        cnpj_dv = str(row[2]).ljust(10)
        identificador_matriz = str(row[3]).ljust(10)
        nome_fantasia = str(row[4]).ljust(100)
        situacao_cadastral = str(row[5]).ljust(10)
        data_situacao_cadastral = str(row[5]).ljust(10)

        f.write(cnpj_basico + cnpj_ordem + cnpj_dv + identificador_matriz + nome_fantasia + situacao_cadastral + data_situacao_cadastral +'\n')