"""crud.py"""
import bson
import json
import os
import streamlit as st

from dotenv import load_dotenv
from io import StringIO
from nosql_sia.nosqlsia.sia import nosqlsia
from nosql_sia.utils.model import (
    base_template,
    faculty_collection,
    program_collection,
    student_collection,
    professor_collection,
)
from ..utils.funcs import get_collection

load_dotenv()


class FacultyCRUD:

    def __init__(self) -> None:
        pass
        
    def insert_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            name = st.text_input(label="Facultad")
            desc = st.text_area(label="Descripción")
            date = st.text_input(label="Fecha creación")
            departments = st.text_area(label="Departamento(s)").strip().split(",")

            if st.button("Insertar"):
                body = faculty_collection()
                body['document']['nombre'] = name
                body['document']['descripcion'] = desc
                body['document']['fecha_creacion'] = date

                def populate_dict_depto(_id, depto):
                    return {"_id": _id, "nombre": depto.strip()}

                body['document']['departamentos'] = [populate_dict_depto(str(bson.objectid.ObjectId()),  depto) for depto in departments]

                try:
                    r = nosqlsia.insert_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            uploaded_file = st.file_uploader("Choose a file")
            
            if uploaded_file is not None:
                # Convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.readlines()

                body = faculty_collection()
                docs = [json.loads(line) for line in string_data]
                body['documents'] = docs
                del body['document']

                try:
                    st.success("Se cargó el archivo correctamente")
                    r_ = nosqlsia.insert_multiple_documents(body)
                    st.write(r_)
                except Exception as e:
                    print(e)

            if r:
                st.success("Se insertó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def find_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_find_single_document")
            
            if st.button("Buscar"):
                body = base_template(os.getenv('faculty_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.find_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se buscó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def update_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_update_single_document")
            update_query = st.text_input(label="Update Query")
            
            if st.button("Actualizar"):
                body = base_template(os.getenv('faculty_collection'))

                if filter_query and update_query:
                    fquery = filter_query.split(":")
                    uquery = update_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                    body['update'] = json.loads("{ \"$set\": {" + f"\"{uquery[0].strip()}\":\"{uquery[1].strip()}\"" + "} }")
                    body['upsert'] = "false"                    
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.update_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)
    
    def delete_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_delete_single_document")
            
            if st.button("Eliminar"):
                body = base_template(os.getenv('faculty_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")                   
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.delete_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

class ProgramCRUD:

    def __init__(self) -> None:
        self.deptos = get_collection(os.getenv('faculty_collection')) # [f"{j['_id']}-{j['nombre']}" for j in nosqlsia.find_multiple_documents(data=base_template("facultad"))['documents']]

    def insert_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            id_dep = st.selectbox(label="Departamento", options=self.deptos)
            name = st.text_input(label="Programa")
            desc = st.text_area(label="Descripción")
            cap = st.text_input(label="Capacidad")
            academic_deg = st.text_input(label="Grado Académico")

            if st.button("Insertar"):
                body = program_collection()
                body['document']['id_departamento'] = id_dep
                body['document']['nombre'] = name
                body['document']['descripcion'] = desc
                body['document']['capacidad'] = cap
                body['document']['grado_academico'] = academic_deg

                try:
                    r = nosqlsia.insert_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            uploaded_file = st.file_uploader("Choose a file")
            
            if uploaded_file is not None:
                # Convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.readlines()

                body = program_collection()
                docs = [json.loads(line) for line in string_data]
                body['documents'] = docs
                del body['document']

                try:
                    st.success("Se cargó el archivo correctamente")
                    r_ = nosqlsia.insert_multiple_documents(body)
                    st.write(r_)
                except Exception as e:
                    print(e)

            if r:
                st.success("Se insertó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def find_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_find_single_document")
            
            if st.button("Buscar"):
                body = base_template(os.getenv('program_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.find_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se buscó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def update_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_update_single_document")
            update_query = st.text_input(label="Update Query")
            
            if st.button("Actualizar"):
                body = base_template(os.getenv('program_collection'))

                if filter_query and update_query:
                    fquery = filter_query.split(":")
                    uquery = update_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                    body['update'] = json.loads("{ \"$set\": {" + f"\"{uquery[0].strip()}\":\"{uquery[1].strip()}\"" + "} }")
                    body['upsert'] = "false"                    
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.update_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)
    
    def delete_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_delete_single_document")
            
            if st.button("Eliminar"):
                body = base_template(os.getenv('program_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")                   
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.delete_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

class StudentCRUD:

    def __init__(self) -> None:
        self.programs = get_collection(os.getenv('program_collection'))

    def insert_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            names = st.text_input(label="Nombres")
            last_names = st.text_input(label="Apellidos")
            birth_date = st.text_input(label="Fecha Nacimiento")
            id_number = st.text_input(label="Número Identificación")
            id_program = st.selectbox(label="Programa", options=self.programs)
            start_date = st.text_input(label="Fecha Inscripción")
            end_date = st.text_input(label="Fecha Finalización")
            is_active = st.text_input(label="Activo")
            coursers = st.text_area(label="Materias a ver").strip().split(",")

            if st.button("Insertar"):
                body = student_collection()
                body['document']['estudiante']['nombres'] = names
                body['document']['estudiante']['apellidos'] = last_names
                body['document']['estudiante']['fecha_nacimiento'] = birth_date
                body['document']['estudiante']['numero_identificacion'] = id_number
                body['document']['programa_estudio']['id_programa'] = id_program
                body['document']['programa_estudio']['fecha_inscripcion'] = start_date
                body['document']['programa_estudio']['fecha_finalizacion'] = end_date
                body['document']['programa_estudio']['activo'] = is_active

                def populate_dict_courses(course):
                    return {"nombre": course.strip(), "nota": None}
                
                body['document']['materias_inscritas'] = [populate_dict_courses(course) for course in coursers]

                try:
                    r = nosqlsia.insert_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            uploaded_file = st.file_uploader("Choose a file")
            
            if uploaded_file is not None:
                # Convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.readlines()

                body = student_collection()
                docs = [json.loads(line) for line in string_data]
                body['documents'] = docs
                del body['document']

                try:
                    st.success("Se cargó el archivo correctamente")
                    r_ = nosqlsia.insert_multiple_documents(body)
                    st.write(r_)
                except Exception as e:
                    print(e)
            if r:
                st.success("Se insertó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def find_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_find_single_document")
            
            if st.button("Buscar"):
                body = base_template(os.getenv('student_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.find_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se buscó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def update_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_update_single_document")
            update_query = st.text_input(label="Update Query")
            
            if st.button("Actualizar"):
                body = base_template(os.getenv('student_collection'))

                if filter_query and update_query:
                    fquery = filter_query.split(":")
                    uquery = update_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                    body['update'] = json.loads("{ \"$set\": {" + f"\"{uquery[0].strip()}\":\"{uquery[1].strip()}\"" + "} }")
                    body['upsert'] = "false"                    
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.update_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)
    
    def delete_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_delete_single_document")
            
            if st.button("Eliminar"):
                body = base_template(os.getenv('student_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")                   
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.delete_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

class ProfessorCRUD:

    def __init__(self) -> None:
        self.deptos = get_collection(collection=os.getenv('faculty_collection'))

    def insert_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            id_depto = st.selectbox(label="Departamento", options=self.deptos) # st.text_input(label="ID Departamento")
            names = st.text_input(label="Nombres")
            last_names = st.text_input(label="Apellidos")
            birth_date = st.text_input(label="Fecha Nacimiento")
            id_number = st.text_input(label="Número Identificación")
            acad_grade = st.text_input(label="Grado Académico")
            title = st.text_input(label="Título")

            if st.button("Insertar"):
                body = professor_collection()
                body['document']['id_departamento'] = id_depto
                body['document']['profesor']['nombres'] = names
                body['document']['profesor']['apellidos'] = last_names
                body['document']['profesor']['fecha_nacimiento'] = birth_date
                body['document']['profesor']['numero_identificacion'] = id_number
                body['document']['grado_academico'] = acad_grade
                body['document']['titulo'] = title

                try:
                    r = nosqlsia.insert_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            uploaded_file = st.file_uploader("Choose a file")
            
            if uploaded_file is not None:
                # Convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                # To read file as string:
                string_data = stringio.readlines()

                body = professor_collection()
                docs = [json.loads(line) for line in string_data]
                body['documents'] = docs
                del body['document']

                try:
                    st.success("Se cargó el archivo correctamente")
                    r_ = nosqlsia.insert_multiple_documents(body)
                    st.write(r_)
                except Exception as e:
                    print(e)

            if r:
                st.success("Se insertó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def find_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_find_single_document")
            
            if st.button("Buscar"):
                body = base_template(os.getenv('professor_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.find_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se buscó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)

    def update_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_update_single_document")
            update_query = st.text_input(label="Update Query")
            
            if st.button("Actualizar"):
                body = base_template(os.getenv('professor_collection'))

                if filter_query and update_query:
                    fquery = filter_query.split(":")
                    uquery = update_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")
                    body['update'] = json.loads("{ \"$set\": {" + f"\"{uquery[0].strip()}\":\"{uquery[1].strip()}\"" + "} }")
                    body['upsert'] = "false"                    
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.update_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)
    
    def delete_single_document(self):
        col1, col2 = st.columns(2)
        r = None
        e = None

        with col1:
            filter_query = st.text_input(label="Filter Query", key="filter_query_delete_single_document")
            
            if st.button("Eliminar"):
                body = base_template(os.getenv('professor_collection'))

                if filter_query:
                    fquery = filter_query.split(":")

                    body['filter'] = json.loads("{" + f"\"{fquery[0].strip()}\":\"{fquery[1].strip()}\"" + "}")                   
                else:
                    body['filter'] = {}

                try:
                    r = nosqlsia.delete_a_single_document(data=body)
                except Exception as e_:
                    e = e_
                
        with col2:
            if r:
                st.success("Se actualizó el documento correctamente")
                st.write(r)
            elif e is not None:
                st.error(e)


fcrud = FacultyCRUD()
pcrud = ProgramCRUD()
scrud = StudentCRUD()
pfcrud = ProfessorCRUD()
