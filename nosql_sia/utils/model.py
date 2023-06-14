"""model.py"""
import os

from ..config.cfg import config
from dotenv import load_dotenv

load_dotenv()

class CollectionTemplate:
    
    def __init__(self) -> None:
        self._datasource = os.getenv('datasource')
        self._database = os.getenv('database')
        self._faculty_collection = os.getenv('faculty_collection')
        self._program_collection = os.getenv('program_collection')
        self._student_collection = os.getenv('student_collection')
        self._professor_collection = os.getenv('professor_collection')

    def base_template(self, collection: str = None) -> dict:
        body = {
            "dataSource": self._datasource,
            "database": self._database,
            "collection": collection,
        }

        return body

    def faculty_collection(self) -> dict:
        body = {
            "dataSource": self._datasource,
            "database": self._database,
            "collection": self._faculty_collection,
            "document": {
                "nombre": None,
                "descripcion": None,
                "fecha_creacion": None,
                "departamentos": [{"_id": None, "nombre": None}],
            },
        }

        return body

    def program_collection(self) -> dict:
        body = {
            "dataSource": self._datasource,
            "database": self._database,
            "collection": self._program_collection,
            "document": {
                "id_departamento": None,
                "nombre": None,
                "descripcion": None,
                "capacidad": None,
                "grado_academico": None
            },
        }

        return body

    def student_collection(self) -> dict:
        body = {
            "dataSource": self._datasource,
            "database": self._database,
            "collection": self._student_collection,
            "document": {
                "estudiante": {
                    "nombres": None,
                    "apellidos": None, 
                    "fecha_nacimiento": None,
                    "numero_identificacion": None
                },
                "programa_estudio": {
                    "id_programa": None,
                    "fecha_inscripcion": None,
                    "fecha_finalizacion": None,
                    "activo": None,
                },
                "materias_inscritas": [
                    {
                        "nombre": None,
                        "nota": None
                    }
                ]
            },
        }

        return body
    
    def professor_collection(self) -> dict:
        body = {
            "dataSource": self._datasource,
            "database": self._database,
            "collection": self._professor_collection,
            "document": {
                "id_departamento": None,
                "profesor": {
                    "nombres": None, 
                    "apellidos": None, 
                    "fecha_nacimiento": None,
                    "numero_identificacion": None,
                },
                "grado_academico": None,
                "titulo": None
            }
        }

        return body


collection_template = CollectionTemplate()
base_template = collection_template.base_template
faculty_collection = collection_template.faculty_collection
program_collection = collection_template.program_collection
student_collection = collection_template.student_collection
professor_collection = collection_template.professor_collection
