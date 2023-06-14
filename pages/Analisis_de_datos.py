"""Analisis_de_datos.py"""
import json
import os
import pandas as pd
import plotly.express as px
import streamlit as st

from dotenv import load_dotenv
from nosql_sia.nosqlsia.sia import nosqlsia
from nosql_sia.utils.model import (
    base_template,
)
from nosql_sia.utils.funcs import avg_notas


load_dotenv()

st.set_page_config(layout="wide")

with st.spinner('Calculando parámetros de fuerza...'):
    faccoll = nosqlsia.find_multiple_documents(data=base_template(os.getenv('faculty_collection')))['documents']
    progcoll = nosqlsia.find_multiple_documents(data=base_template(os.getenv('program_collection')))['documents']
    stucoll = nosqlsia.find_multiple_documents(data=base_template(os.getenv('student_collection')))['documents']
    profcoll = nosqlsia.find_multiple_documents(data=base_template(os.getenv('professor_collection')))['documents']


st.sidebar.header("EDA de datos académicos tomados de un sistema NoSQL")
st.sidebar.markdown("""
    Análisis exploratorio de los datos del sistema universitario.\n
    Se exploran las relaciones entre las facultades, departamentos, programas curriculares, estudiantes y profesores, mostrando 
    estadísticas descriptivas de los datos almacenados en las diferentes colecciones de la base de datos NoSQL.
""")

st.title("Análisis de datos académicos")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")

col1, col2 = st.columns([.3, .7])

with col1:
    selected_faculty = st.selectbox(label="Facultad", options=[facultad['nombre'] for facultad in faccoll])
    depto_tuples = [(depto['_id'], depto['nombre']) for faculty in faccoll if faculty['nombre'] == selected_faculty for depto in faculty['departamentos']]
    selected_depto = st.selectbox(label="Departamento", options=[depto[1] for depto in depto_tuples][1:-1])
    depto_id = [depto[0] for depto in depto_tuples if depto[1] == selected_depto]
    prog_list = [prog for prog in progcoll if prog['id_departamento'].strip() == depto_id[0].strip()]
    selected_prog = st.selectbox(label="Programa", options=[prog['nombre'] for prog in prog_list])

with col2:
    fig1 = px.pie(pd.DataFrame(prog_list), values='capacidad', names='nombre', title='Capacidad de Programas Curriculares', hole=0.5)
    fig1

    df2 = pd.DataFrame([{'id_programa': reg['programa_estudio']['id_programa'], 'materias_inscritas': avg_notas(reg['materias_inscritas'])} for reg in stucoll]).groupby(['id_programa']).mean().reset_index()
    df2.columns = ["Programa Curricular", "AVG(notas)"]
    df2['Programa Curricular'] = df2['Programa Curricular'].replace("1",'Ingeniería Electrónica').replace("3",'Ingeniería Mecatrónica').replace("4",'Ingeniería de Sistemas y Computación').replace("6",'Ingeniería Eléctrica').replace("7",'Ingeniería Industrial').replace("9",'Ingeniería Mecánica')

    fig2 = px.bar(df2, x=df2['Programa Curricular'], y=['AVG(notas)'], title="Promedio de notas por Programa Curricular")
    fig2

    df3 = pd.DataFrame([{'id_programa': reg['programa_estudio']['id_programa'], 'activo': reg['programa_estudio']['activo']} for reg in stucoll]).groupby(['id_programa']).count().reset_index()
    df3.columns = ["id_programa", "activo"]
    df3['id_programa'] = df3['id_programa'].replace("1",'Ingeniería Electrónica').replace("3",'Ingeniería Mecatrónica').replace("4",'Ingeniería de Sistemas y Computación').replace("6",'Ingeniería Eléctrica').replace("7",'Ingeniería Industrial').replace("9",'Ingeniería Mecánica')

    fig3 = px.pie(df3, values='activo', names='id_programa', title="Proporción de estudiantes activos por Programa Curricular")
    fig3

    df4 = pd.DataFrame([{'Departamento': reg['id_departamento'], 'Conteo': 1} for reg in profcoll]).groupby(['Departamento']).count().reset_index()
    df4['Departamento'] = df4['Departamento'].replace("2",'Departamento de Ingenieria Civil y Agricola').replace("6",'Departamento de Ingenieria Mecanica y Mecatronica').replace("8",'Departamento de Ingenieria Electronica y Electrica')

    fig4 = px.bar(df4, y='Departamento', x='Conteo', title="Cantidad de profesores por Departamento", orientation='h')
    fig4

    df5 = pd.DataFrame([{'Grado Académico': reg['grado_academico'], 'Conteo': 1} for reg in profcoll]).groupby(['Grado Académico']).count().reset_index()
    
    fig5 = px.pie(df5, values='Conteo', names='Grado Académico', title="Proporción de profesores por Grado Académico", hole=.5)
    fig5

