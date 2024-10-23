import streamlit as st
import pandas as pd
import os
import openpyxl as op

# Título da Aplicação
st.title('Teste Learning FNS')

# Diretório onde os arquivos Excel estão armazenados
directory = '.planilhas_FNS/.recursos'  # Certifique-se de que esse é o caminho correto

# Função para carregar todos os arquivos Excel
def load_all_excel_files(directory):
    all_data = []
    for file in os.listdir(directory):
        if file.endswith(('.xlsx', '.xls')):
            file_path = os.path.join(directory, file)
            try:
                data = pd.read_excel(file_path)
                all_data.append(data)
            except Exception as e:
                st.write(f"Erro ao carregar {file}: {e}")
    return pd.concat(all_data, ignore_index=True) if all_data else pd.DataFrame()

# Carregar os dados de todos os arquivos Excel
data = load_all_excel_files(directory)

# Verificar se os dados foram carregados
if not data.empty:
    st.write("Dados Carregados:")
    st.dataframe(data)

    # Verifique se existem colunas para 'Ano' e 'Tipo de Recurso'
    if 'DATA OB' in data.columns and 'BLOCO' in data.columns:
        # Agrupar os dados por Ano e Tipo de Recurso
        grouped_data = data.groupby(['Data', 'Tipo de Recurso']).size().reset_index(name='Contagem')

        # Criar gráfico
        st.write("Comparação de Tipos de Recursos por Ano:")
        st.bar_chart(grouped_data.set_index(['Ano', 'Tipo de Recurso'])['Contagem'])
    else:
        st.write("As colunas 'Ano' e 'Tipo de Recurso' não foram encontradas nos dados.")
else:
    st.write("Não foram encontrados dados para exibir.")
