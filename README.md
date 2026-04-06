# Customer Churn Analysis

## Objetivo

Este projeto tem como objetivo analisar e compreender os fatores que levam clientes de uma empresa de telecomunicações a cancelar seus serviços (churn), utilizando SQL e Python para gerar insights acionáveis.

---

## Problema de Negócio

A retenção de clientes é um dos principais desafios para empresas de telecomunicações. Altas taxas de churn impactam diretamente:

* Receita recorrente
* Crescimento sustentável
* Eficiência de aquisição de novos clientes

Este projeto busca responder:

> Quais fatores mais influenciam o churn e como podemos reduzi-lo?

---

## Arquitetura do Projeto

```
├── data/
│   ├── raw/           # Dados brutos originais
│   └── processed/     # Dados tratados e prontos para análise
│
├── notebooks/         # Análises exploratórias (EDA)
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
│
├── sql/
│   ├── schema.sql     # Modelagem do banco de dados
│   └── queries.sql    # Consultas analíticas
│
├── src/
│   └── database/
│       └── load_data.py  # Pipeline de ingestão de dados
```

---

## Tecnologias Utilizadas

* Python

  * Pandas (manipulação de dados)
  * Matplotlib (visualização)
  * SQLite3 (integração com banco de dados)

* SQL

  * Agregações
  * Group By
  * Análises de churn

* Jupyter Notebook

  * Análise exploratória interativa

---

## Pipeline de Dados

O fluxo de dados foi estruturado para simular um ambiente real:

1. Ingestão

   * Leitura do dataset bruto

2. Tratamento

   * Conversão de tipos
   * Tratamento de valores nulos
   * Padronização de variáveis

3. Armazenamento

   * Persistência em banco SQLite

4. Análise

   * Queries SQL + EDA em Python

---

## Modelagem de Dados

Os dados foram estruturados em uma tabela relacional (`customers`), preservando todas as variáveis relevantes para permitir análises completas de comportamento do cliente.

---

## Principais Análises

* Churn por tipo de contrato
* Churn por tempo de relacionamento (tenure)
* Churn por serviços contratados
* Churn por método de pagamento
* Identificação de perfis de alto risco

---

## Principais Insights

* Contratos mensais apresentam maior churn, indicando baixa fidelização
* Clientes novos são mais propensos a cancelar, sugerindo falhas no onboarding
* Ausência de suporte técnico aumenta significativamente o churn
* Pagamentos automáticos estão associados a maior retenção

---

## Recomendações de Negócio

Com base nos dados, algumas ações estratégicas incluem:

* Incentivar contratos de longo prazo
* Melhorar o processo de onboarding de novos clientes
* Expandir e promover suporte técnico
* Incentivar métodos de pagamento automáticos

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/FilipeMadeira13/churn-analysis-project.git
cd churn-analysis-project
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o pipeline de dados:

```bash
python src/database/load_data.py
```

4. Abra os notebooks na ordem sugerida:

* `01_data_understanding.ipynb`
* `02_data_cleaning.ipynb`
* `03_eda.ipynb`

---

## Próximos Passos

* Desenvolvimento de modelo preditivo de churn
* Criação de dashboard interativo (Streamlit)
* Automatização do pipeline de dados
* Deploy da aplicação

---

## Autor

Filipe Madeira
- [GitHub](https://github.com/FilipeMadeira13)
- [LinkedIn](https://www.linkedin.com/in/carlos-filipe-madeira-de-souza-16211922a)

---

## Considerações Finais

Este projeto foi desenvolvido com foco em simular um cenário real de análise de dados, combinando:

* Pensamento analítico
* SQL aplicado
* Manipulação de dados em Python
* Geração de insights de negócio
