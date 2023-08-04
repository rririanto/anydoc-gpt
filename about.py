import streamlit as st
from streamlit_extras.buy_me_a_coffee import button


def intro():
    st.markdown("<br>", unsafe_allow_html=True)
    button(username="rririanto", floating=True, width=221)
    st.markdown("""
    ## AnyDocGPT - Extract and Query your docs""")
    with st.expander("## About AnyDocGPT", expanded=True):

     st.info("""
Approximately Around 80% of enterprise data is in difficult formats like HTML, PDF, CSV, PNG, PPTX, etc. AnyDocGPT simplifies this by effortlessly extracting and converting the complex data for use with GPT AI. 

The process involves using unstructured.io and GPT OpenAI to retrieve information from your document. We don't store your OpenAI API and doc data, and the source code is open-source for your review.
 
If you find my code helpful, you can support me by buying me a coffee. [![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/rririanto)

Follow me to get update my latest post [![Follow](https://img.shields.io/twitter/follow/rririanto?style=social)](https://www.twitter.com/rririanto)

            """)
