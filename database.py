import sqlite3

DATABASE_NAME = 'data.db'

def get_db_connection():
    """Cria e retorna uma conexão com o banco de dados."""
    conn = sqlite3.connect(DATABASE_NAME)
    
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Inicializa o banco de dados e cria a tabela se não existir."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                value TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )"""
        )
        conn.commit()
        print("Banco de dados inicializado com sucesso.")
    except Exception as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
    finally:
        if conn:
            conn.close()

def add_data(value):
    """Adiciona um novo valor ao banco de dados."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO data (value) VALUES (?)', (value,))
        conn.commit()
    finally:
        conn.close()

def get_all_data():
    """Recupera todos os valores do banco de dados."""
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT id, value, created_at FROM data')
        rows = cursor.fetchall()
        
        return [dict(row) for row in rows]
    finally:
        conn.close()
