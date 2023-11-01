"""Service to fetch data from API"""

import requests
import streamlit as st

API_URL = st.secrets["API_URL"]

def _get(url: str) -> dict:
    """Fetch data from API"""
    response = requests.get(url)
    with st.spinner(f"Fetching data from {url}..."):
        if not response.ok:
            st.error(f"Error {response.status_code} fetching data from {url}: {response.text}")
            st.stop()
        
        return response.json()["data"]

def get_forums() -> list:
    """Get forums list.

    Returns:
        list: Forums list
    """
    return _get(f"{API_URL}/forums/")

def get_forum_by_name(name: str) -> dict:
    """Get forum by name.

    Args:
        name (str): Forum name

    Returns:
        dict: Forum data
    """
    return _get(f"{API_URL}/forums/{name}/")