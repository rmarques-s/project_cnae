# 📊 project_cnae

> Sobre a aplicação 

Projeto criado durante a disciplina ALGORITMO E PROGRAMACAO ORIENTADA AO OBJETO do curso de Engenharia Mecânica da UFRN. A aplicação consiste em traçar o perfil econômico do Rio Grande do Norte através do código CNAE das empresas do estado. Os dados foram coletados da API [https://dados.gov.br/](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj).]

> Para rodar o projeto:

- Criando sua tabela no banco: Rode as migrations migration_companies.py e migration_establishments.py. Esses códigos irão criar sua tabela com todos os campos necessários para você importar os dados dentro do banco.

- Lendo e inserindo dados no banco: Abra os arquivos, selecione algumas linhas e coloque em outro arquivo menor. Assim, ao entrar no PGAdmin basta clicar em "import/export data" e selecionar seu arquivo menor. Ele será lido pelo PostgreSQL e irá gerar sua tabela com os dados.

- Sugestão: Para gerar uma tabela mais limpa, crie uma view apenas com os dados mais necessários, se você optar por ter todas as colunas ou colunas diferentes das que eu selecionei, basta mudar a referência do endpoint.

- Rodando o template: Digite "python3 data.py" no terminal e a tabela com os estabelecimentos será gerada.

**OBS: O projeto ainda está em andamento! Futuramente serão implementadas novas funcionalidades.**

# 🖥 Ferramentas:

- Flask
- Google Colab
- Biblioteca Pandas
- HTML 5 / CSS / Javascript
- PgAdmin (PostgreSQL 12.15)

