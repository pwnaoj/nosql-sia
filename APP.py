"""APP.py"""
import streamlit as st

from PIL import Image
from nosql_sia.nosqlsia.crud import (
    fcrud,
    pcrud,
    scrud,
    pfcrud
)


st.set_page_config(
    page_title="NoSQL SIA",
)

st.sidebar.header("Migrando RDB a NoSQL")
st.sidebar.markdown("""
    En este proyecto se realizó la migración de un sistema universitario desde una base de datos relacional MySQL a una base de datos no relacional en MongoDB.\n
    A través de un servicio web interactivo se realizan operaciones CRUD sobre las diferentes colecciones de la base de datos NoSQL.\n
    La migración exitosa garantizó la integridad y consistencia de los datos, y la infraestructura en la nube desplegada en Google Cloud a través de Atlas Cloud de MongoDB 
    proporcionó un entorno confiable.
""")

st.title("Colecciones en NoSQL")
st.markdown("""
    El modelo de datos NoSQL del proyecto dispone de cuatro colecciones: **Facultad**, **Programa**, **Estudiante** y **Profesor**.
""")

col1, col2 = st.columns(2)

with col1:
    options = st.selectbox(label='Seleccione una colección', options=["Facultad", "Programa", "Estudiante", "Profesor"])


if options == "Facultad":
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open('./images/faculty_collection.png'))

    with col2:
        st.markdown(f"""
            La colección **{options}** contiene los campos `nombre`, `descripcion`, `fecha_creacion` y `departamentos` los cuales describen una facultad de la Universidad.\n
            Podemos observar que se modela la relación **1**:**M** entre **Facultad** y **Departamentos** (1 Facultad tiene muchos Departamentos) a través de una lista
            de departamentos.
        """)
elif options == "Programa":
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open('./images/program_collection.png'))

    with col2:
        st.markdown(f"""
            La colección **{options}** contiene los campos `id_departamento`, `nombre`, `descripcion`, `capacidad` y `grado_academico` los cuales describen un programa curricular de la Universidad.\n
        """)
elif options == "Estudiante":
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open('./images/student_collection.png'))

    with col2:
        st.markdown(f"""
            La colección **{options}** contiene dos campos principales: `estudiante` y `programa_estudio` los cuales describen un estudiante de la Universidad.\n 
            Para el campo `estudiante` se tienen los campos: `nombres`, `apellidos`, `fecha_nacimiento` y `numero_identificacion`.\n
            Para el campo `programa_estudio` se tienen los campos: `id_programa`, `fecha_inscripcion`, `fecha_finalizacion` y `activo`.\n
            Podemos ver la relación **1**:**M** entre **Estudiante** y **Materias Inscritas** (1 Estudiante inscribe muchas Materias).\n
        """)
elif options == "Profesor":
    col1, col2 = st.columns(2)

    with col1:
        st.image(Image.open('./images/professor_collection.png'))

    with col2:
        st.markdown(f"""
            La colección **{options}** contiene los campos `id_departamento`, `profesor` el cual se compone de los campos `nombres`, `apellidos`, `fecha_nacimiento` y `numero_identificacion`;
            `grado_academico` y `titulo`.\n
            Estos campos describen un profesor asociado a un departamento de la Universidad.
        """)


st.title("Operaciones CRUD")
st.markdown("""
    Las operaciones CRUD nos permiten **insertar/leer/actualizar/eliminar** documentos en las colecciones de nuestro modelo NoSQL SIA.
    Al seleccionar una colección, usted podrá ejecutar las operaciones CRUD teniendo en cuenta los campos definidos para cada documento.
""")

tab1, tab2, tab3, tab4 = st.tabs(["Create", "Read", "Update", "Delete"])

with tab1:
    st.markdown(f"""
        La operación **Create** añade nuevos documentos a la colección **{options}**. Puede insertar nuevos documentos diligenciando el formulario o
        cargando un archivo de datos.    
    """)

    if options == "Facultad":
        fcrud.insert_single_document()

    elif options == "Programa":
        pcrud.insert_single_document()

    elif options == "Estudiante":
        scrud.insert_single_document()
    
    elif options == "Profesor":
        pfcrud.insert_single_document()

with tab2:
    st.markdown(f"""
        La operación **Read** permite buscar documentos en la colección **{options}**
    """)

    if options == "Facultad":
        fcrud.find_single_document()

    elif options == "Programa":
        pcrud.find_single_document()

    elif options == "Estudiante":
        scrud.find_single_document()
    
    elif options == "Profesor":
        pfcrud.find_single_document()

with tab3:
    st.markdown(f"""
        La operación **Update** permite actualizar documentos de la colección **{options}**
    
    """)

    if options == "Facultad":
        fcrud.update_single_document()

    elif options == "Programa":
        pcrud.update_single_document()

    elif options == "Estudiante":
        scrud.update_single_document()

    elif options == "Profesor":
        pfcrud.update_single_document()

with tab4:
    st.markdown(f"""
        La operación **Delete** permite actualizar documentos de la colección **{options}**
    
    """)

    if options == "Facultad":
        fcrud.delete_single_document()

    elif options == "Programa":
        pcrud.delete_single_document()

    elif options == "Estudiante":
        scrud.delete_single_document()
    
    elif options == "Profesor":
        pfcrud.delete_single_document()
        