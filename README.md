# project_cnae

> Sobre a aplicação 

Projeto criado durante a disciplina ALGORITMO E PROGRAMACAO ORIENTADA AO OBJETO do curso de Engenharia Mecânica da UFRN. A aplicação consiste em traçar o perfil econômico do Rio Grande do Norte através do código CNAE das empresas do estado. Os dados foram coletados da API [https://dados.gov.br/](https://dados.gov.br/dados/conjuntos-dados/cadastro-nacional-da-pessoa-juridica---cnpj).]

> Para rodar o projeto:

Para criar sua tabela no banco, rode as migrations migration_companies.py e migration_establishments.py. Esses códigos irão criar sua tabela com todos os campos necessários para você importar os dados dentro do banco.

Para colocar os dados, abrimos os arquivos, selecionamos algumas linhas e colocamos em outro arquivo menor. Assim, ao entrar no PGAdmin basta clicar em "import/export data" e selecionar seu arquivo menor. Ele será lido pelo PostgreSQL e irá gerar sua tabela com os dados.

Para gerar uma tabela mais limpar, criamos uma view apenas com os dados mais necessários, se você optar por ter todas as colunas ou colunas diferentes, basta mudar a referência do endpoint.

Para rodar o template com a tabela que servirá de consulta, digite "python3 data.py" no terminal.

OBS: O projeto ainda está em andamento! Futuramente serão implementadas novas funcionalidades.

🖥 Ferramentas:

- Flask
- Google Colab
- Biblioteca Pandas
- HTML 5 / CSS / Javascript
- PgAdmin (PostgreSQL 12.15)

