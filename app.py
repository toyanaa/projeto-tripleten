import streamlit as st
import pandas as pd
import ploty.express as px

# Especifique o caminho do arquivo CSV
caminho_arquivo = r'C:\Users\regin\OneDrive\Desktop\projeto-tripleten\vehicles.csv'

# Use pd.read_csv() para ler o arquivo CSV
car_data = pd.read_csv(caminho_arquivo, delimiter=',') # lendo os dados

# Titulo do meu aplicativo web 
st.header('Meu primeiro aplicativo pela web')

print()

# criar um botão
hist_button = st.button('Criar histograma') 
     
if hist_button: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um histograma
         fig = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig, use_container_width=True)

print()

# criar um botão
hist_button1 = st.button('Criar um grafico de dispersão') 

if hist_button1: # se o botão for clicado
         # escrever uma mensagem
         st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
         
         # criar um grafico de dispersão
         fig1 = px.scatter(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
         st.plotly_chart(fig1, use_container_width=True)

print()

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')

if build_histogram: # se a caixa de seleção for selecionada
        # escrever uma mensagem
        st.write('Criando um histograma para a coluna odometer')

        # criar um histograma
        fig2 = px.histogram(car_data, x="odometer")
     
         # exibir um gráfico Plotly interativo
        st.plotly_chart(fig2, use_container_width=True)