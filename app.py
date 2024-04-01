import streamlit as st
import pandas as pd
import ploty.express as px

# Especifique o caminho do arquivo CSV
caminho_arquivo = r'C:\Users\regin\OneDrive\Desktop\projeto-tripleten\vehicles.csv'

# Use pd.read_csv() para ler o arquivo CSV
car_data = pd.read_csv(caminho_arquivo) # lendo os dados

