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
        data_situacao_cadastral = str(row[6]).ljust(10)
        motivo_situacao_cadastral = str(row[7]).ljust(10)
        nome_cidade_exterior = str(row[8]).ljust(10)
        pais = str(row[9]).ljust(10)
        data_inicio_atividade = str(row[10]).ljust(10)
        cnae_fiscal_principal = str(row[11]).ljust(10)
        cnae_fiscal_secundario = str(row[12]).ljust(10)
        tipo_logradouro = str(row[13]).ljust(10)
        logradouro = str(row[14]).ljust(10)
        numero = str(row[15]).ljust(10)
        complemento = str(row[16]).ljust(10)
        bairro = str(row[17]).ljust(10)
        cep = str(row[18]).ljust(10)
        uf = str(row[19]).ljust(10)
        municipio = str(row[20]).ljust(10)
        ddd_1 = str(row[21]).ljust(10)
        telefone_1 = str(row[22]).ljust(10)
        ddd_2 = str(row[23]).ljust(10)
        telefone_2 = str(row[24]).ljust(10)
        ddd_FAX = str(row[25]).ljust(10)
        fax = str(row[26]).ljust(10)
        correio_eletronico = str(row[27]).ljust(10)
        situacao_especial = str(row[28]).ljust(10)
        data_situacao_especial =  str(row[29]).ljust(10)

        f.write(cnpj_basico + cnpj_ordem + cnpj_dv + identificador_matriz + nome_fantasia + situacao_cadastral + data_situacao_cadastral + motivo_situacao_cadastral + nome_cidade_exterior + pais +  data_inicio_atividade + 
                cnae_fiscal_principal + cnae_fiscal_secundario + tipo_logradouro + logradouro + numero + complemento + bairro + cep + uf + municipio + ddd_1 + telefone_1 + ddd_2 + telefone_2 + ddd_FAX + fax + correio_eletronico +
                situacao_especial + data_situacao_especial + '\n')
