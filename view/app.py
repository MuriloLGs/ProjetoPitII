import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'controller')))
from db import obter_dados  
import json
import pandas as pd
import altair as alt

def obter_dados_empresas(acoes, selecionar_empresas):
    dados_empresas = []
    
    for empresa in selecionar_empresas:
        
        dados_empresa = obter_dados(empresa)  
        
        
        dados_empresa_df = pd.DataFrame(dados_empresa, columns=['id', 'empresa', 'ticker', 'data', 'preco_fechamento'])
        
        dados_empresas.append(dados_empresa_df)
    
    
    if dados_empresas:
        return pd.concat(dados_empresas)
    else:
        return pd.DataFrame(columns=['id', 'empresa', 'ticker', 'data', 'preco_fechamento'])


with open('Dados/acoes.json', 'r') as file:
    acoes = json.load(file)


st.title("Projeto Pit II - Análise de Ações de Empresas de Tecnologia")


st.sidebar.title("Seleção de Empresas")
selecionar_empresas = st.sidebar.multiselect(
    "Escolha até 2 empresas para comparar:",
    list(acoes["empresas"].keys()),
    default=[list(acoes["empresas"].keys())[0]]  
)


if selecionar_empresas:
    dados_completos = obter_dados_empresas(acoes, selecionar_empresas)
else:
    dados_completos = pd.DataFrame(columns=['id', 'empresa', 'ticker', 'data', 'preco_fechamento'])


if not dados_completos.empty:
    
    dados_completos['data'] = pd.to_datetime(dados_completos['data'], errors='coerce')
    
    st.subheader("Dados das Ações Selecionadas")
    st.write(
        dados_completos.sort_values(by=['empresa', 'data']).style.format({
            'data': '{:%Y-%m-%d}',  
            'preco_fechamento': '{:.2f}'  
        })
    )
else:
    st.subheader("Nenhuma empresa selecionada ou sem dados disponíveis.")


if not dados_completos.empty:
    chart = alt.Chart(dados_completos).mark_line().encode(
        x=alt.X('data:T', title='Data', sort=[]),
        y=alt.Y('preco_fechamento:Q', title='Preço de Fechamento'),
        color=alt.Color('empresa:N', title='Empresa'),
        tooltip=['data:T', 'empresa:N', 'preco_fechamento:Q']
    ).properties(
        width=800,
        height=400,
        title="Preço de Fechamento das Ações"
    )
    st.altair_chart(chart, use_container_width=True)
else:
    st.write("Nenhum dado para exibir no gráfico.")
