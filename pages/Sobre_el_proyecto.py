"""Sobre_el_proyecto.py"""
import streamlit as st


st.header("Introducción")
st.markdown("""
    En el ámbito académico, el control de calificaciones es una parte fundamental para el seguimiento y evaluación del rendimiento de los estudiantes. Los sistemas universitarios suelen utilizar bases de datos relacionales para almacenar y gestionar esta información. Sin embargo, con el crecimiento constante de los datos y la necesidad de un análisis más eficiente, se hace necesario considerar alternativas que brinden mayor escalabilidad y flexibilidad.\n
    Este proyecto se enfoca en la migración de un sistema de control de calificaciones en un sistema universitario desde una base de datos relacional MySQL a una base de datos no relacional MongoDB. El objetivo principal es aprovechar las ventajas que ofrece MongoDB, como su capacidad de almacenar grandes volúmenes de datos de manera eficiente y su flexibilidad para adaptarse a cambios en la estructura de la información.\n
    Además de la migración de la base de datos, se desarrollará un servicio web utilizando el framework Streamlit. Este servicio web permitirá interactuar con los datos almacenados en MongoDB, facilitando la gestión y manipulación de las calificaciones de los estudiantes. Asimismo, se creará un dashboard de análisis de datos que proporcionará visualizaciones y métricas relevantes para evaluar el rendimiento académico.\n
    El proceso de migración se realizará mediante el desarrollo de scripts en Python que transfieran los datos desde MySQL a MongoDB, manteniendo las relaciones existentes y asegurando la integridad de la información. Para ello, se utilizará la infraestructura de Atlas Cloud, que permite desplegar y administrar clústeres de MongoDB en la nube, garantizando la disponibilidad y seguridad de los datos.\n
    La metodología empleada en este proyecto incluye el análisis y diseño de la estructura de la base de datos en MongoDB, la generación de datos de prueba para simular el sistema académico, la migración de los datos desde MySQL a MongoDB, el desarrollo del servicio web con Streamlit y la creación del dashboard de análisis de datos.\n
    Con la implementación de este proyecto, se espera mejorar la eficiencia y escalabilidad del sistema de control de calificaciones, así como facilitar el acceso y análisis de los datos para los usuarios. La migración a MongoDB y el uso de Streamlit proporcionarán una mayor flexibilidad en la gestión de la información académica, permitiendo un seguimiento más completo del rendimiento de los estudiantes y facilitando la toma de decisiones basada en datos.\n
""")

st.header("Sobre los creadores")
st.markdown("""
    El proyecto fue desarrollado por los estudiantes Camilo Alfonso Mosquera Benavides (camosquerab@unal.edu.co ), Julian Mauricio Rodriguez (jumrodriguezba@unal.edu.co ) y Joan Sebastian Tamayo Rivera (jstamayo@unal.edu.co) 
    como entregable del proyecto final del curso **Bases de Datos Avanzadas** visto en la **Universidad Nacional de Colombia**, **Sede Bogotá**.
""")