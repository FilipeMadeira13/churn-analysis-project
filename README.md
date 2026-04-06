# Churn Analysis Project

Este projeto analisa dados de churn de clientes de uma empresa de telecomunicações, identificando padrões e fatores que influenciam a perda de clientes.

## Estrutura do Projeto

```
├── data/
│   ├── raw/           # Dados brutos originais
│   └── processed/     # Dados processados e limpos
├── notebooks/         # Análises exploratórias em Jupyter
│   ├── 01_data_understanding.ipynb
│   ├── 02_data_cleaning.ipynb
│   └── 03_eda.ipynb
├── sql/               # Queries SQL para análise
│   ├── schema.sql     # Esquema do banco de dados
│   └── queries.sql    # Consultas analíticas
└── src/
    └── database/      # Scripts de carregamento de dados
        └── load_data.py
```

## Tecnologias Utilizadas

- **Python**: Pandas, Matplotlib, SQLite3
- **SQL**: Análises estruturadas
- **Jupyter Notebook**: Exploração de dados interativa

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

3. Execute o carregamento dos dados:
   ```bash
   python src/database/load_data.py
   ```

4. Abra os notebooks na ordem sugerida para acompanhar a análise.

## Principais Insights

- Clientes com contratos mensais têm maior taxa de churn
- Novos clientes (menos de 1 ano) são mais propensos a cancelar
- Falta de suporte técnico aumenta significativamente o risco de churn
- Métodos de pagamento automático correlacionam com melhor retenção

## Próximos Passos

- Implementar modelo preditivo de churn
- Dashboard interativo para monitoramento
- Estratégias de retenção baseadas nos insights