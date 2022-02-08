# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 19:39:59 2022

@author: mvdan
"""

import pandas as pd
import streamlit as st
import plotly.express as px


#read the dataset
df = pd.read_csv('covid-variants.csv')
#convert date column to date type
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d') 
#get list of countries
paises = list(df['location'].unique()) 
#get list of variants
variants = list(df['variant'].unique())
#create title
tipo = 'Casos diários'
titulo = tipo + ' para '   
#allow user to select a country (or show all)
pais = st.sidebar.selectbox('Selecione o pais', ['Todos']+ paises)
#allow user to select a variant
variante = st.sidebar.selectbox('Selecione a variante', ['Todas'] + variants )  
#select part of the dataframe that matches the user selection
if(pais !=  'Todos'):    
    st.header('Mostrando dados para ' + pais)    
    df = df[df['location'] == pais]    
    titulo = titulo + pais
else:    
    st.header('Mostrando dados para todos os países') 
if(variante !=  'Todas'):    
    st.text('Mostrando dados para a variante ' + variante)    
    df = df[df['variant'] == variante]    
    titulo = titulo + ' (variante : ' + variante + ')' 
else:    
    st.text('Mostrando dados para todas as variantes')    
    titulo = titulo + '(todas as variantes)'     
#sum values in other columns according to the same date
dfShow   = df.groupby(by=["date"]).sum() 
#create figure
fig = px.line(dfShow, x=dfShow.index, y='num_sequences')
fig.update_layout(title=titulo )
st.plotly_chart(fig, use_container_width=True)