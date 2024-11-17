import sqlite3
import yfinance as yf
import pandas as pd
import json

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS acoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa TEXT,
            ticker TEXT,
            data TEXT,
            preco_fechamento REAL,
            UNIQUE(empresa, data, ticker)  -- Garantindo que a combinação empresa, data, ticker seja única
        )
    ''')
    conn.commit()
    print(cursor.fetchall())
    conn.close()


# Função para inserir dados no banco de dados com verificação para dados duplicados
def inserir_dados(empresa, ticker, data, preco_fechamento):
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO acoes (empresa, ticker, data, preco_fechamento)
            VALUES (?, ?, ?, ?)
        ''', (empresa, ticker, data, preco_fechamento))
        conn.commit()
    except sqlite3.IntegrityError:
        # Caso os dados já existam (violando a restrição UNIQUE), não faça nada
        pass

    conn.close()


# Função para obter dados do banco de dados
def obter_dados(empresa=None):
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()

    if empresa:
        cursor.execute('SELECT * FROM acoes WHERE empresa = ?', (empresa,))  # Retorna todos os dados da tabela
    else:    
        cursor.execute('SELECT * FROM acoes')

    dados = cursor.fetchall()    
    conn.close()
    return dados


# Função para verificar e limitar o número de ações inseridas por empresa
def limitar_50_acoes(empresa):
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()

    # Contar quantas ações já foram inseridas para a empresa
    cursor.execute('SELECT COUNT(*) FROM acoes WHERE empresa = ?', (empresa,))
    count = cursor.fetchone()[0]
    conn.close()

    # Se a empresa já tiver 50 ou mais ações, retorna False
    return count < 50


# Função para inserir dados financeiros usando yfinance e inserir no banco de dados
def inserir_dados_com_yfinance():
    with open('Dados/acoes.json', 'r') as file:
        acoes = json.load(file)
    
    # Acessando as empresas e seus respectivos tickers
    for empresa, ticker in acoes["empresas"].items():
        # Usando o yfinance para buscar os dados históricos da ação
        dados_acao = yf.download(ticker, period="6mo", interval="1wk")  # Obtendo 1 ano de dados

        # Inserir os dados de fechamento de cada dia no banco de dados
        for data, row in dados_acao.iterrows():
            if limitar_50_acoes(empresa):  # Verifica se há espaço para mais ações da empresa
                preco_fechamento = float(row['Close'].iloc[0])  # Atualizado para evitar o FutureWarning
                inserir_dados(empresa, ticker, data.strftime('%Y-%m-%d'), preco_fechamento)
            else:
                pass

# Função para criar a tabela no banco de dados ao iniciar
criar_tabela()

# Inserir os dados com yfinance (somente uma vez)
inserir_dados_com_yfinance()
