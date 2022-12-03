#Librerias Importadas
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np 
import pandas as pd 
import re
import plotly.express as px
import streamlit as st 
import requests
import plotly.graph_objects as go
from PIL import Image
import io

st.sidebar.header('Syafiq Web App')

#Menú de la Barra Lateral
with st.sidebar: 
    selected = option_menu(
        menu_title=None,
        options=['Controles','Gráficas','Mapas'])

if selected == 'Controles':

    url="https://raw.githubusercontent.com/jeaggo/tc3068/master/Superstore.csv"
    s=requests.get(url).content
    df=pd.read_csv(io.StringIO(s.decode('utf-8')))

    df2 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/df2.csv')
    df3 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/df3.csv')

    st.title('WALMART Visualización de Datos')

    st.write('En este proyecto se busca mostrar la selección de datos del DataFrame de la empresa mundial WALMART, utilizando algunos botones que segmentaran la busqueda deseada')

    st.dataframe(df)

    st.slider('Discount')

    st.selectbox('Selecciona la Categoría',df2['Category'])


    st.radio('Selecciona el Ship Mode',df3['Ship Mode'])



if selected == 'Gráficas':

    st.title('Gráficas de la empresa Walmart')

    st.write('Para esta pagína se busca mostrar con el mismo DataFrame de WALMART la visualización de algunos de los datos con los que cuentan la empresa')

    st.subheader('Cantidad de Categorias de los Productos de Walmart')
    
    df2 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/df2.csv')
    fig12 = px.pie(df2, values='Número de Categories',names='Category',color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig12.update_traces(textinfo='percent+label')
    st.plotly_chart(fig12)

    st.subheader('Cantidad de Regiones donde se ubica Walmart')
    
    df4 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/df4.csv')
    fig13 = px.bar(df4, x='Region', y='Número de Regions',
             hover_data=['Region','Número de Regions'], color='Número de Regions',
             color_continuous_scale="Brwnyl",
             labels={'Regiones':'Cantidad de Regiones'}, height=400)
             
    st.plotly_chart(fig13, use_container_width=True)

    st.subheader('Cantidad de Estados donde se ubica Walmart')

    df5 = pd.read_csv(r'/Users/sofiaalmeraya/Desktop/ActM1/WALMART/df5.csv')
    fig14 = px.histogram(df5, x="State", y='Número de States',color_discrete_sequence=px.colors.sequential.Brwnyl)
    fig14.update_layout(yaxis_type="log")

    st.plotly_chart(fig14, use_container_width=True)
