"""Pipeline de carregamento de dados para análise de churn.

Este módulo carrega dados processados em CSV e os armazena em um banco SQLite
para permitir análises SQL posteriores.
"""

import sqlite3
import logging
from pathlib import Path

import pandas as pd


# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def get_project_paths():
    """Retorna caminhos do projeto de forma agnóstica ao diretório atual."""
    # Encontrar raiz do projeto (onde está .git)
    current = Path(__file__).resolve()
    while current != current.parent:
        if (current / ".git").exists():
            return {
                "root": current,
                "data_processed": current / "data" / "processed",
                "db": current / "data" / "churn.db"
            }
        current = current.parent
    
    # Fallback se não encontrar .git
    return {
        "root": Path.cwd(),
        "data_processed": Path.cwd() / "data" / "processed",
        "db": Path.cwd() / "data" / "churn.db"
    }


def load_data(csv_path=None, db_path=None):
    """Carrega dados CSV no banco SQLite com validação e tratamento de erros.
    
    Args:
        csv_path (str, optional): Caminho para o arquivo CSV.
                                  Default: data/processed/churn_clean.csv
        db_path (str, optional): Caminho para o banco SQLite.
                                 Default: data/churn.db
    
    Returns:
        bool: True se carregamento bem-sucedido, False caso contrário
        
    Raises:
        FileNotFoundError: Se o arquivo CSV não for encontrado
        Exception: Para outros erros durante o carregamento
    """
    
    paths = get_project_paths()
    
    # Usar defaults se não especificados
    if csv_path is None:
        csv_path = paths["data_processed"] / "churn_clean.csv"
    else:
        csv_path = Path(csv_path)
    
    if db_path is None:
        db_path = paths["db"]
    else:
        db_path = Path(db_path)
    
    # Validar arquivo CSV
    if not csv_path.exists():
        logger.error(f"❌ Arquivo CSV não encontrado: {csv_path}")
        raise FileNotFoundError(f"Arquivo {csv_path} não existe")
    
    # Criar diretório de dados se não existir
    db_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        logger.info(f"📂 Lendo dados de: {csv_path}")
        df = pd.read_csv(csv_path)
        logger.info(f"✓ Carregado {len(df)} registros com {len(df.columns)} colunas")
        
        logger.info(f"💾 Conectando ao banco: {db_path}")
        conn = sqlite3.connect(str(db_path))
        
        df.to_sql("customers", conn, if_exists="replace", index=False)
        conn.close()
        
        logger.info(f"✅ Dados inseridos com sucesso em {db_path}")
        return True
        
    except pd.errors.ParserError as e:
        logger.error(f"❌ Erro ao ler CSV: {e}")
        raise
    except sqlite3.Error as e:
        logger.error(f"❌ Erro ao acessar banco de dados: {e}")
        raise
    except Exception as e:
        logger.error(f"❌ Erro inesperado: {e}")
        raise


if __name__ == "__main__":
    try:
        load_data()
    except Exception as e:
        logger.error(f"Falha ao executar pipeline: {e}")
        exit(1)
