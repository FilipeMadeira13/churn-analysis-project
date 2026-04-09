# Customer Churn Analysis

## Objetivo

Este projeto tem como objetivo analisar e compreender os fatores que levam clientes de uma empresa de telecomunicações a cancelar seus serviços (churn), utilizando SQL e Python para gerar insights acionáveis.

---
## Dataset

Este projeto utiliza o dataset público **Telco Customer Churn**, amplamente utilizado para análise de cancelamento de clientes em empresas de telecomunicações.

- Fonte: IBM Sample Data
- Total de registros: 7.043 clientes
- Variáveis: 21 colunas

Principais atributos:

- `customerID`: Identificador único do cliente  
- `tenure`: Tempo de relacionamento (meses)  
- `Contract`: Tipo de contrato (mensal, anual, etc.)  
- `MonthlyCharges`: Valor mensal pago  
- `TotalCharges`: Valor total pago  
- `Churn`: Indica se o cliente cancelou o serviço  

O dataset foi disponibilizado em formato CSV e armazenado na pasta `data/raw/` para ingestão no pipeline.

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

## Impacto Estimado

Considerando:

- Base de 7.043 clientes
- Ticket médio estimado de $64,76/mês

A redução de churn em apenas 5% pode representar:

→ Retenção de ~350 clientes  
→ Aproximadamente $22.000+ em receita mensal preservada  

Isso demonstra que pequenas melhorias na retenção podem gerar impacto financeiro significativo.

---

## Prioridades Estratégicas

Com base na análise, as ações com maior potencial de impacto são:

1. Reduzir churn em contratos mensais
2. Melhorar onboarding de novos clientes
3. Atuar sobre clientes de fibra óptica
4. Incentivar pagamento automático

---

## Como Executar

1. Clone o repositório:

```bash
git clone https://github.com/FilipeMadeira13/churn-analysis-project.git
cd churn-analysis-project
```

2. Crie e ative um ambiente virtual (recomendado):

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências de runtime:

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. Para usar Jupyter e abrir os notebooks, instale também as dependências de desenvolvimento:

```bash
pip install -r dev-requirements.txt
```

5. Execute o pipeline de dados:

```bash
python src/database/load_data.py
```

6. Abra os notebooks na ordem sugerida:

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
- [LinkedIn](https://www.linkedin.com/in/filipe-madeira-16211922a)

---

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## Considerações Finais

Este projeto simula um cenário real de negócio, combinando:

* Pensamento analítico
* SQL aplicado
* Manipulação de dados em Python
* Geração de insights de negócio
