"""App main page"""

import requests
import streamlit as st

import api_service as api

API_URL = st.secrets["API_URL"]
                           
st.title("Hello, World!")

sidebar = st.sidebar.title("Forums list")

forums = api.get_forums()

for forum in forums:
    st.write(api.get_forum_by_name(forum["name"]))
