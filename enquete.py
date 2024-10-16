import streamlit as st
import pandas as pd
import os

# Função para salvar as respostas em um arquivo Excel
def salvar_dados_em_excel(nome_arquivo, dados):
    # Se o arquivo já existir, carregue-o, senão crie um novo DataFrame
    if os.path.exists(nome_arquivo):
        df_existente = pd.read_excel(nome_arquivo)
        df_novo = pd.concat([df_existente, pd.DataFrame(dados)], ignore_index=True)
    else:
        df_novo = pd.DataFrame(dados)
    
    # Salva no arquivo Excel
    df_novo.to_excel(nome_arquivo, index=False)

# Exemplo de dados da enquete
st.title("Enquete")
pergunta = st.radio("Qual é sua linguagem favorita?", ("Python", "Java", "C++", "JavaScript"))

# Botão para submeter a resposta
if st.button("Enviar resposta"):
    dados_enquete = {"Resposta": [pergunta]}
    salvar_dados_em_excel("dados_enquete.xlsx", dados_enquete)
    st.success("Resposta salva com sucesso!")
