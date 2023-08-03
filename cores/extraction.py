import requests
import streamlit as st
from unstructured.partition.auto import partition

def send_file_to_unstructured_api(uploaded_file, api_key, **kwargs):
    """
    Send data to unstructed.io API. It will use unstructured.io server to process the extraction.

    :param uploaded_file: The file uploaded by the user

    :param api_key: The API key entered by the user

    :param kwargs: Required fields for submiting to unstructured.io

    :return: True if the input is valid, False otherwise
    """
    url = 'https://api.unstructured.io/general/v0.0.33/general'
    headers = {'accept': 'application/json', 'unstructured-api-key': api_key}

    # Prepare the files parameter for the API request
    # The dict must have a tuple format type
    files = {
        'pdf_infer_table_structure': (None, kwargs['pdf_infer_table_structure']),
        'xml_keep_tags': (None, kwargs['xml_keep_tags']),
        'include_page_breaks': (None, kwargs['include_page_breaks']),
        'encoding': (None, kwargs['encoding']),
        'strategy': (None, kwargs['strategy']),
        'output_format': (None, kwargs['output_format']),
        'files': uploaded_file,
        'gz_uncompressed_content_type': (None, ''),
        'ocr_languages': (None, kwargs['ocr_languages']),
        'coordinates': (None, ''),
        'hi_res_model_name': (None, ''),
    }

    try:
        response = requests.post(url, headers=headers, files=files)
        response.raise_for_status()  # raise exception if request was unsuccessful
        return response.json()
    except requests.exceptions.RequestException as e:
        # Display error message on Streamlit
        st.error(f"Failed to send file to API: {e}")
        return None

def extract_text(uploaded_file, **kwargs):
    """
    Process extraction data in streamlit server. 

    :param uploaded_file: The file uploaded by the user

    :param kwargs: Required settings fields for the extraction

    :return: True if the input is valid, False otherwise
    """
    try:
        elements = partition(file=uploaded_file, **kwargs)
        return "\n\n".join([str(el) for el in elements])
    except Exception as e:
        st.error(f"Failed to extract text: {e}")
        return None

