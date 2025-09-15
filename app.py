# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 23:27:09 2025

@author: angel
"""

# Librerias
import pandas as pd
import plotly.graph_objects as go
import plotly.express as go2
import streamlit as st

# Carga del dataframe de veiculos
df = pd.read_csv('vehicles_us.csv')

# Imagen del proyecto
st.image("tripleten.png")

# Titulo del proyecto
st.title("Sprint 7 - Project")

# Encabezado
st.header('Informacion de carros')

# Muestra breve del dataframe
st.write(df.head(10))

# Creacion de inputs
genre = st.radio(
    "Grafica que deseas mostrar",
    ["***Histograma***", "***Diagrama de dispercion***"],
    captions=[
        "Datos del odometro.",
        "Datos de valor por año",
    ],
)

if genre == "***Histograma***":
    st.write("Se creara histograma")
elif genre == "***Diagrama de dispercion***":
    st.write("Se creara diagrama de dispercion")
else:
    st.write("No has seleccionado")

# Se crea boton generador de la grafica
generar_button = st.button('Generar grafica')


# Depende de la seleccion de grafica que desees, esta se generara
if generar_button:
    if genre == "***Histograma***":
        st.write(
            'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

        # Se crea una figura vacía y luego se añade un rastro de histograma
        fig = go.Figure(data=[go.Histogram(x=df['odometer'])])
    
        # Se le da un titulo a la grafica
        fig.update_layout(title_text='Distribución del Odómetro')
    
        # Se muestra la grafica
        st.plotly_chart(fig, use_container_width=True)

    elif genre == "***Diagrama de dispercion***":
        st.write('Se crea grafica de dispercion del valor del carro por modelo')
        
        # Se crea la grafica de dispercion de modelo del año por precio
        fig_d = go2.scatter(df, x='model_year', y='price')
        
        # Se agrega un titulo a la grafica
        fig_d.update_layout(title_text='Valor por año')
        
        # Se muestra 
        st.plotly_chart(fig_d, use_container_width=True)
        
    
