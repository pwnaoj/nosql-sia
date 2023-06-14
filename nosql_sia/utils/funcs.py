"""funcs.py"""
import numpy as np
import streamlit as st

from ..utils.model import base_template
from ..nosqlsia.sia import nosqlsia


st.cache_data
def get_collection(collection: str):
    if collection == "facultad":
        return [f"{j['_id']}-{j['nombre']}" for reg in nosqlsia.find_multiple_documents(data=base_template(collection))['documents'] for j in reg['departamentos']]
    elif collection == "programa":
        return [f"{j['nombre']}" for j in nosqlsia.find_multiple_documents(data=base_template("programa"))['documents']]
    
def avg_notas(regs: list):
    notas = [round(float(reg['nota']), 2) for reg in regs]

    return np.average(notas)
