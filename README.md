# fiap_tech_challenge_04

## Pre-requisitos
- Deve ser aberto no VSCODE, para que execute o docker-compose que cria os servicos docker necessarios para que funcione.
- O Python 3.13.0 deve estar instalado
- Este projeto usa o poetry para controlar as dependecias, localizadas no arquivo pyproject.toml.

## Objetivo
Este projeto tem como objetivo baixar os dados das Carteiras Diarias do movimento da B3 e carregar num banco de dados para que fiquem disponiveis para uma API. Esta tem a funcao de carregar os dados deste banco de dados e treinar um modelo de Machine Learning que fara a predicao dos valores de quantidade teorica baseado nos dados historicos ja existentes. Este modelo ficara disponivel para que uma aplicacao de Dashboard obtenha as metricas relacionada.

## Funcionamento
- **Ambiente Virtual**
Existe uma configuracao de devcontainer usada pelo VSCODE. Ela chama um docker-compose que sobe um banco de dados postgres localmentte no seguinte endereco: **http://localhost:8090**.
Para acessa-lo use o usuario postgres e senha postgres. Existe uma tabela chamada raw_data que armazena todos os dados baixados da B3 da Carteira do Dia.

- **Download**

Nesta fase os arquivos das Carte Diarias do movimento da B3, que sao baixados num diretorio dentro deste repositorio chamado **temp_files/downloaded**. Logo em seguida sao movidos para o diretorio **temp_files/AAAAMMDD**, para que fiquem organizados por data, ja que a data nao existe dentro do arquivo como sendo uma coluna.
- **Banco de Dados**

Com o arquivo da movimentacao diaria baixado, suas informacoes sao inseridas numa tabela de uma banco de dados POSTGRES (iniciado pelo ambiente virtual do VSCODE) chamada raw_data.
- **API**

Para executara a API basta executar os seguintes comandos:
- source venv_3.13.0/bin/activate
- poetry run python3.13 src/main.py
Apos a inicializacao, deve ser deixada em execucao para que a aplicacao de Dashboard de Metricas funcione.

A documentacao da API pode ser localizada neste endereco **http://localhost:8080/docs**

Os endpoints disponiveis sao:
- **load**: faz o download e carrega os dados da tabela raw_data do banco de dados e os deixa disponivel para um modelo de Regressao Linear.
- **train**: treina o modelo com todos os dados carregados atualmente e anteriormente
- **predict**: faz a previsao das quantidades teoricas baseado no treinamento do modelo feito anteriormente
## Dashboard de Metricas

Um dashboard de metricas simples sobre a qualidade do modelo. Para executa-lo basta executar os seguintes comandos (em outro terminal):
- source venv_3.13.0/bin/activate
- poetry run python3.13 src/dashboard.py

A aplicacao executara os endpoints acima em ordem (load, train e predict) e obtera as metricas em relacao a qualidade do modelo. Estas sao exibidas na saida do console.

## Melhorias
Existem melhorias a serem feitas na aplicacao, como salvar o modelo de uma forma mais eficiente para o uso das APIs e uma aplicacao que efetivamente mostre um grafico sobre o desempenho do modelo.
