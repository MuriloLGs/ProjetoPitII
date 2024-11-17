import sqlite3
import yfinance as yf
import pandas as pd
import json


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
        pass

    conn.close()



def obter_dados(empresa=None):
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()

    if empresa:
        cursor.execute('SELECT * FROM acoes WHERE empresa = ?', (empresa,))  
    else:    
        cursor.execute('SELECT * FROM acoes')

    dados = cursor.fetchall()    
    conn.close()
    return dados



def limitar_50_acoes(empresa):
    conn = sqlite3.connect('db/acoes.db')
    cursor = conn.cursor()

    
    cursor.execute('SELECT COUNT(*) FROM acoes WHERE empresa = ?', (empresa,))
    count = cursor.fetchone()[0]
    conn.close()

    
    return count < 50


def inserir_dados_com_yfinance():
    with open('Dados/acoes.json', 'r') as file:
        acoes = json.load(file)
    
   
    for empresa, ticker in acoes["empresas"].items():
        
        dados_acao = yf.download(ticker, period="6mo", interval="1wk")  

        
        for data, row in dados_acao.iterrows():
            if limitar_50_acoes(empresa):  
                preco_fechamento = float(row['Close'].iloc[0])  
                inserir_dados(empresa, ticker, data.strftime('%Y-%m-%d'), preco_fechamento)
            else:
                pass

criar_tabela()

inserir_dados_com_yfinance()
