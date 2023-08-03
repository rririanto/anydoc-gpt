import streamlit as st
from cores.ai import  split_text_into_chunks, create_vectorstore, query_file
from cores.extraction import extract_text, send_file_to_unstructured_api
import time
from about import intro

def boolean_to_string(value):
    return 'true' if value else ''


@st.cache_data
def process_document(uploaded_file, unstructured_api_input, openai_api_key, **settings):
    start_time = time.time()
    with st.spinner("Extracting document. This may take a while⏳"):
        try:
            if unstructured_api_input:
                texts = send_file_to_unstructured_api(
                    uploaded_file=uploaded_file, api_key=unstructured_api_input, **settings)
            else:
                texts = extract_text(
                    uploaded_file=uploaded_file, **settings)

            text_chunks = split_text_into_chunks(texts)
            return create_vectorstore(text_chunks, openai_api_key)
        except Exception as e:
            st.error(f"Failed to process document: {e}")

    execution_time = time.time() - start_time  # Calculate the execution time
    # Display the execution time
    st.write(f"Extraction time: {execution_time} seconds")


def main():
    """
    The main function for the Streamlit app.

    :return: None.
    """
    intro()

    if "enable_api" in st.session_state and st.session_state.enable_api:
        st.session_state.advance = True

    openai_api_key = st.text_input(
            "OpenAI API Key",
            type="password",
            placeholder="Paste your OpenAI API key here (sk-...)",
            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501,
    )

    active_online_api = None 
    unstructured_api_input = None
    with st.expander("Advance Options", expanded=st.session_state.get("advance", False)):
        active_online_api = st.checkbox(
            "Use unstructured.io API?", help="Please note: The file will be uploaded and extracted through the unstructured.io server.", key="enable_api")

        if active_online_api:
            unstructured_api_input = st.text_input(
                'Input your API key:', st.secrets["UNSTRUCTURED_API_KEY"], help="You can use mine first, you can also request your own API key here: https://unstructured.io/api-key/#get-api-key")

        settings = {
            'strategy': st.radio("Choose the strategy", ('auto', 'hi_res', 'fast', 'ocr_only'), horizontal=True, index=1),
            'pdf_infer_table_structure': boolean_to_string(st.checkbox('pdf_infer_table_structure')),
            'xml_keep_tags': boolean_to_string(st.checkbox('xml_keep_tags')),
            'include_page_breaks': boolean_to_string(st.checkbox('include_page_breaks')),
            'encoding': st.text_input('encoding', 'utf_8'),
            'ocr_languages': st.text_input('ocr_languages', 'en'),
            'output_format': st.radio("Choose the output format", ('text/json', 'text/csv'), horizontal=True, index=0)
        }
        st.info(
            "For more information visit: https://unstructured-io.github.io/unstructured/api.html")

    uploaded_file = st.file_uploader(
        "Upload your document. Accept (HTML, PDF, CSV, PNG, PPTX, and more)")
    if uploaded_file is not None:
        vectorstore = process_document(uploaded_file, unstructured_api_input, openai_api_key, **settings)

        query = st.text_input("Ask your document")
        if not query:
            st.stop()

        answer = query_file(query, openai_api_key, vectorstore)
        st.write("### ANSWER")
        st.write(answer)


if __name__ == '__main__':
    main()
