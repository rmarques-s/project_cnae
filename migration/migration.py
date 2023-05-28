from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Definir a classe do modelo
Base = declarative_base()

class CNAE(Base):
    __tablename__ = 'estabelecimentos'
    id = Column(Integer, primary_key=True)
    cnpj_ordem = Column(String(100))
    cnpj_dv = Column(String(100))
    identificador_matriz = Column(String(100))
    nome_fantasia = Column(String(100))
    situacao_cadastral = Column(String(100))
    data_situacao_cadastral = Column(String(100))
    motivo_situacao_cadastral = Column(String(100))
    nome_cidade_exterior = Column(String(100))
    pais = Column(String(100))
    data_inicio_atividade = Column(String(100))
    cnae_fiscal_principal = Column(String(100))
    cnae_fiscal_secundario = Column(String(100))
    tipo_logradouro = Column(String(100))
    logradouro = Column(String(100))
    numero = Column(String(100))
    complemento = Column(String(100))
    bairro = Column(String(100))
    cep = Column(String(100))
    uf = Column(String(100))
    municipio = Column(String(100))
    ddd_1 = Column(String(100))
    telefone_1 = Column(String(100))
    ddd_2 = Column(String(100))
    ddd_FAX = Column(String(100))
    fax = Column(String(100))
    correio_eletronico =  Column(String(100))
    situacao_especial = Column(String(100))
    data_situacao_especial = Column(String(100))
    
# Configurar a conexão com o banco de dados
engine = create_engine('postgresql://postgres:postgres@localhost/cnae_rn')
Session = sessionmaker(bind=engine)
session = Session()

# # Criar o schema
# schema_name = 'estabelecimentos'
# create_schema = CreateSchema(schema_name)
# engine.execute(create_schema)
# session.commit()

# Criar a tabela
Base.metadata.create_all(engine)
if Base.metadata.create_all(engine) == True:
  print("Banco de dados conectado e tabela criada com sucesso!")

# Para alterar a migração
# alter_sql = "ALTER TABLE pessoas ADD COLUMN email VARCHAR(100)"
# session.execute(alter_sql)
# session.commit()

# Encerrar a sessão
session.close()
