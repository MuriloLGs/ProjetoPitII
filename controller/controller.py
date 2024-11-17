import sys
import os
import pandas as pd


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'model')))

from finance import obter_dados  

def obter_dados_empresas(acoes, selecionar_empresas):
    dados_empresas = []
    for empresa in selecionar_empresas:
        ticker = acoes["empresas"][empresa]  
        dados_empresas.append(obter_dados(empresa, ticker)) 
    
    dados_completos = pd.concat(dados_empresas) 
    return dados_completos
