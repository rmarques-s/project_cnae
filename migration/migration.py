from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Definindo a classe modelo
Base = declarative_base()

class CNAE(Base):
    __tablename__ = 'estabelecimentos'
    cnpj_basico = Column(String(), primary_key=True)
    cnpj_ordem = Column(String())
    cnpj_dv = Column(String())
    identificador_matriz = Column(String())
    nome_fantasia = Column(String())
    situacao_cadastral = Column(String())
    data_situacao_cadastral = Column(String())
    motivo_situacao_cadastral = Column(String())
    nome_cidade_exterior = Column(String())
    pais = Column(String())
    data_inicio_atividade = Column(String())
    cnae_fiscal_principal = Column(String())
    cnae_fiscal_secundario = Column(String())
    tipo_logradouro = Column(String())
    logradouro = Column(String())
    numero = Column(String())
    complemento = Column(String())
    bairro = Column(String())
    cep = Column(String())
    uf = Column(String())
    municipio = Column(String())
    ddd_1 = Column(String())
    telefone_1 = Column(String())
    ddd_2 = Column(String())
    telefone_2 = Column(String())
    ddd_FAX = Column(String())
    fax = Column(String())
    correio_eletronico =  Column(String())
    situacao_especial = Column(String())
    data_situacao_especial = Column(String())
    
# Configurando a conexão com o banco de dados
engine = create_engine('postgresql://postgres:postgres@localhost/cnae_rn')
Session = sessionmaker(bind=engine)
session = Session()

# # Criar o schema
# schema_name = 'estabelecimentos'
# create_schema = CreateSchema(schema_name)
# engine.execute(create_schema)
# session.commit()

# Criando a tabela
Base.metadata.create_all(engine)

# Para alterar a migration
# alter_sql = "ALTER TABLE pessoas ADD COLUMN email VARCHAR()"
# session.execute(alter_sql)
# session.commit()

session.close()
