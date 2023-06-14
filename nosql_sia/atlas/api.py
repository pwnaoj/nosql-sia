"""api.py"""
import json
import httpx
import os
import streamlit as st

from ..config.cfg import config
from dotenv import load_dotenv

load_dotenv()


class Api:

    def __init__(self) -> None:
        self._base_url = os.getenv('base_url') # config.atlas_config['base_url']
        self._api_key = os.getenv('api_key') # config.atlas_config['api_key']
        self._headers = {'Content-Type': 'application/json', 'api-key': self._api_key}

    # Find a Single Document
    def find_a_single_document(self, data: dict, endpoint: str = '/action/findOne') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
    # Find Multiple Documents
    @st.cache_data(show_spinner=False)
    def find_multiple_documents(_self, data: dict, endpoint: str = '/action/find') -> dict:
        with httpx.Client(base_url=_self._base_url, headers=_self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
    # Insert a Single Document
    def insert_a_single_document(self, data: dict, endpoint: str = '/action/insertOne') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
    # Insert Multiple Documents
    def insert_multiple_documents(self, data: dict, endpoint: str = '/action/insertMany') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_

    # Update a Single Document
    def update_a_single_document(self, data: dict, endpoint: str = '/action/updateOne') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
    # Delete a Single Document
    def delete_a_single_document(self, data: dict, endpoint: str = '/action/deleteOne') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
    # Delete Multiple Documents
    def delete_multiple_documents(self, data: dict, endpoint: str = '/action/deleteMany') -> dict:
        with httpx.Client(base_url=self._base_url, headers=self._headers, timeout=15.0) as client:
            r = client.post(url=endpoint, data=json.dumps(data))
            r_ = r.json()

        return r_
    
