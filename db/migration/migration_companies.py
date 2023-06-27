from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


Base = declarative_base()

class CNAE(Base):
    __tablename__ = 'empresas'
    cnpj_basico = Column(String(), primary_key=True)
    razao_social = Column(String())
    natureza_juridica = Column(String())
    qualificacao_responsavel = Column(String())
    capital_social = Column(String())
    porte_empresa = Column(String())
    ente_federativo = Column(String())


# Configurando a conexão com o banco de dados
engine = create_engine('postgresql://postgres:postgres@localhost/cnae_rn')
Session = sessionmaker(bind=engine)
session = Session()

# Criando a tabela
Base.metadata.create_all(engine)

session.close()