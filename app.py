import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv(
    'C:/Users/julio/Desktop/sprint5_project/sprint5_project/vehicles_us.csv')  # lendo os dados
st.header('Criação de gráficos de dados de carros:')

hist_button = st.button('Criar histograma')  # criar um botão de histograma
disp_button = st.button('Criar dispersão')  # criar um botão de dispersão
build_histogram = st.checkbox('Criar um histograma')

if hist_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

elif disp_button:  # se o botão for clicado
    # escrever uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncios de vendas de carros')

    # criar um histograma
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

elif build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')
