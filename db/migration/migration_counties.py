from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Definindo a classe modelo
Base = declarative_base()

class CNAE(Base):
    __tablename__ = 'municipios'
    id = Column(String(), primary_key=True)
    municipio = Column(String())

    
# Configurando a conexão com o banco de dados
engine = create_engine('postgresql://postgres:postgres@localhost/cnae_rn')
Session = sessionmaker(bind=engine)
session = Session()

# Criando a tabela
Base.metadata.create_all(engine)

# Para alterar a migration
# alter_sql = "ALTER TABLE .... ADD COLUMN ..."
# session.execute(alter_sql)
# session.commit()

session.close()