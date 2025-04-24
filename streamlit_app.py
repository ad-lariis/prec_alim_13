#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:44:04 2025

@author: alexandre
"""





import streamlit as st
from st_files_connection import FilesConnection
import streamlit.components.v1 as components
from PIL import Image
import requests
from io import BytesIO



response = requests.get('https://storage.googleapis.com/logo-lariis/logo_page_blanc.png')
image = Image.open(BytesIO(response.content))

st.set_page_config(layout='wide', page_title='Précarité alimentaire 13', page_icon=image)


@st.cache_data()


#carte
def get_map():
    conn = st.connection('gcs', type=FilesConnection)
    with conn.open("prec_alim_13/index.html", 'r') as map_file:
        map_html = map_file.read()
    return map_html




map_html = get_map()



page_bg_img = f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat&display=swap');
    
    .st-emotion-cache-1jicfl2 {{
    width: 100% !important;
    padding: 6rem 0rem 2rem;
    min-width: auto;
    max-width: initial;
    }}
    .block-container {{
        padding-top: 0.5rem;
        }}
    h1 {{
        font-family: "Montserrat", serif;
        color: white;
        font-size: 0.1em;
        margin-left: 10px;
        }}
    body {{
        font-family: "Montserrat", serif;
        }}
    
    [data-testid="stAppViewContainer"] {{
        background: rgb(0,140,149);
        }}
    [data-testid="stHeader"] {{
        background: rgba(0,0,0,0);
        }}
    iframe {{
        flex-grow: 1; 
        width: 100%;
        min-height: 80vh;
}}
    :has(iframe) {{
        display: flex;
        flex-direction: column;
        height: 100%; 
}}
</style>
"""



st.markdown(page_bg_img, unsafe_allow_html=True)



st.title('Précarité alimentaire dans les Bouches-du-Rhône: offre et besoins')



with st.container():  
    components.html(map_html)
