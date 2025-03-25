# Projeto TED 7 – Análise de Dados de Filmes

Este repositório contém um projeto de análise de dados que utiliza uma abordagem ETL (Extração, Transformação e Carga) para coletar, processar e analisar informações de filmes. O fluxo do projeto é dividido em etapas: extração dos dados via API, limpeza e transformação dos dados, análise exploratória e, finalmente, aplicação de um modelo de regressão linear que relaciona o orçamento (budget) à receita (revenue).

## Visão Geral do Projeto

O projeto tem como objetivo demonstrar como realizar um fluxo completo de ETL, desde a obtenção dos dados de uma API (neste caso, a TMDb), passando pelo tratamento e análise exploratória, até a aplicação de um modelo estatístico (regressão linear) para prever a receita dos filmes a partir do orçamento.  
As principais etapas são:

- **Extração (Extract):**  
  O arquivo `api_data.py` é responsável por coletar os dados de filmes a partir da API do The Movie Database (TMDb). Ele faz requisições paginadas, extrai os IDs dos filmes e, em seguida, coleta os detalhes de cada filme, adicionando a data de ingestão.

- **Transformação (Transform):**  
  Os notebooks `data-cleaning.ipynb` e `exploratory_analysis.ipynb` tratam e exploram os dados coletados. Nesta fase, os dados são limpos, transformados e preparados para análise.

- **Carga e Análise (Load & Analyze):**  
  O dataset final é armazenado em um arquivo JSON na pasta `dataset`. Em seguida, o notebook `linear-reg.ipynb` utiliza os dados do dataset silver para realizar um cálculo de regressão linear, onde a variável independente (X) é o orçamento e a variável dependente (Y) é a receita dos filmes.

## Estrutura do Repositório

- **analysis/** – Contém os notebooks de análise exploratória dos dados.  
- **api-requests/** – Inclui scripts (como `api_data.py`) que fazem a extração dos dados da API.  
- **data-treatment/** – Notebook(s) e scripts para limpeza e transformação dos dados.  
- **dataset/** – Pasta onde o dataset final (por exemplo, o arquivo JSON com os detalhes dos filmes) é armazenado.  
- **linear-regression/** – Notebook `linear-reg.ipynb` com o cálculo da regressão linear (Budget vs Revenue).  
- **requirements.txt** – Lista de dependências necessárias para rodar o projeto.  
- **.gitignore** – Arquivos e pastas que não serão versionados.

## Instalação e Execução

### Pré-requisitos

- **Git:** para clonar o repositório.  
- **Python 3:** instalado no sistema.  
- **Jupyter Notebook:** para executar os notebooks.  
- **Virtualenv:** para isolar as dependências do projeto.

### Passos para Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/LuizGPassos/ted-7-projeto-final.git
   cd ted-7-projeto-final
   ```

2. **Crie e ative um ambiente virtual:**

   No Linux/macOS:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   No Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**

   O script `api_data.py` utiliza a variável de ambiente `API_TOKEN` para autenticar na API do TMDb. Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API, por exemplo:

   ```
   API_TOKEN=seu_token_aqui
   ```

5. **Execute os notebooks:**

   Inicie o Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

   Abra os notebooks desejados (por exemplo, `data-cleaning.ipynb`, `exploratory_analysis.ipynb` e `linear-reg.ipynb`) e execute as células conforme as instruções contidas em cada um.
