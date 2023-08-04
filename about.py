import streamlit as st
from streamlit_extras.buy_me_a_coffee import button


def intro():
    st.markdown("<br>", unsafe_allow_html=True)
    button(username="rririanto", floating=True, width=221)
    st.markdown("""
    ## AnyDocGPT - Extract and Query your doc""")
    st.info("""
Approximately 80% of enterprise data exists in challenging formats such as HTML, PDF, CSV, PNG, PPTX, and more. 
With AnyDocGPT, you can streamline this process by effortlessly extracting and converting this complex data for use with GPT AI.     
    
The extraction process involves utilizing unstructured-io with streamlit and GPT OpenAI to retrieve information from your document. 
We do not store your OpenAI API and doc data, and you can review the source code since it is an open-source project. [![Star](https://img.shields.io/github/stars/rririanto/anydoc-gpt.svg?logo=github&style=social)](https://github.com/rririanto/anydoc-gpt)
    """)
    st.markdown("""
<font size="3"><i>If you find my code helpful, you can support me by buying me a coffee. 🙌</font>&nbsp;&nbsp;[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/rririanto)</i>
<br><font size="3"><i> Follow me to get update my latest post</i></font> &nbsp;&nbsp; [![Follow](https://img.shields.io/twitter/follow/rririanto?style=social)](https://www.twitter.com/rririanto)
""", unsafe_allow_html=True)

    st.markdown("---")
