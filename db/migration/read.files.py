import resource
import os
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pandas as pd

from sqlalchemy import create_engine

file_name = "/home/rafaelamarques/Área de Trabalho/empresas_db"

df = pd.read_csv(file_name)

for col in df.columns:
  df[col] = df[col].apply(str)

#print(f'File Size is {os.stat(file_name).st_size / (1024 * 1024)} MB')


#txt_file = open(file_name)

#count = 0

#for line in txt_file:
    # we can process file line by line here, for simplicity I am taking count of lines
    #count += 1

#txt_file.close()

#print(f'Number of Lines in the file is {count}')

#print('Peak Memory Usage =', resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
#print('User Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_utime)
#print('System Mode Time =', resource.getrusage(resource.RUSAGE_SELF).ru_stime)


def conecta_db():
  con = psycopg2.connect(host='localhost', 
                         database='cnae_rn',
                         user='postgres', 
                         password='postgres')
  return con

# Dropando a tabela caso ela já exista
sql = 'DROP TABLE IF EXISTS public.empresas'
conecta_db(sql)

def criar_db(sql):
  con = conecta_db()
  cur = con.cursor()
  cur.execute(sql)
  con.commit()
  con.close()

# Criando a tabela das empresas
sql = '''CREATE TABLE public.empresas 
      ( cnpj_basico            character varying(10), 
        razao_social           character varying(100), 
        natureza_juridica          character varying(500), 
        qualificacao_responsavel    character varying(200), 
        capital_social       character varying(10), 
        porte_empresa character varying(10), 
        ente_federativo       character varying(100)
      )'''
criar_db(sql)

def inserir_db(sql):
    con = conecta_db()
    cur = con.cursor()
    try:
        for i in df.index:
          sql = """
          INSERT into public.empresas (cnpj_basico, natureza_juridica,qualificacao_responsavel,capital_social,porte_empresa,ente_federativo) 
          values('%s','%s','%s','%s','%s','%s','%s','%s','%s');
          """ % (df['cnpj_basico'][i], df['natureza_juridica'][i], df['qualificacao_responsavel'][i], df['capital_social'][i], df['porte_empresa'][i], df['ente_federativo'][i])
          inserir_db(sql)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        con.rollback()
        cur.close()
        return 1
    cur.close()