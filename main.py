import streamlit as st
import pandas as pd
import os

# Título da Aplicação
st.title('Teste Learning FNS')

# Diretório onde os arquivos Excel estão armazenados
directory = 'Planilhas_FNS/Recursos'  # Atualize se necessário

# Verificar se o diretório existe
if os.path.exists(directory):
    # Listar todos os arquivos Excel (.xlsx e .xls) no diretório
    excel_files = [f for f in os.listdir(directory) if f.endswith(('.xlsx', '.xls'))]

    # Se não houver arquivos, avise o usuário
    if not excel_files:
        st.write("Não foram encontrados arquivos Excel no diretório.")
    else:
        # Selecionar um arquivo
        selected_file = st.selectbox("Selecione um arquivo Excel:", excel_files)

        # Caminho completo do arquivo selecionado
        file_path = os.path.join(directory, selected_file)

        # Carregar os dados do Excel
        try:
            data = pd.read_excel(file_path)
            st.write("Dados Carregados:")
            st.dataframe(data)
            st.line_chart(data)
        except Exception as e:
            st.write(f"Erro ao carregar o arquivo: {e}")
else:
    st.write(f"O diretório '{directory}' não foi encontrado.")
