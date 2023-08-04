from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.docstore.document import Document
from langchain.chains.qa_with_sources import load_qa_with_sources_chain

from langchain.prompts import PromptTemplate

# Use a shorter template to reduce the number of tokens in the prompt
template = """Create a final answer to the given questions using the provided document excerpts(in no particular order) as references. ALWAYS include a "SOURCES" section in your answer including only the minimal set of sources needed to answer the question. If you are unable to answer the question, simply state that you do not know. Do not attempt to fabricate an answer and leave the SOURCES section empty.

---------

QUESTION: What  is the purpose of ARPA-H?
=========
Content: More support for patients and families. \n\nTo get there, I call on Congress to fund ARPA-H, the Advanced Research Projects Agency for Health. \n\nIt’s based on DARPA—the Defense Department project that led to the Internet, GPS, and so much more.  \n\nARPA-H will have a singular purpose—to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more.
Source: 1-32
Content: While we’re at it, let’s make sure every American can get the health care they need. \n\nWe’ve already made historic investments in health care. \n\nWe’ve made it easier for Americans to get the care they need, when they need it. \n\nWe’ve made it easier for Americans to get the treatments they need, when they need them. \n\nWe’ve made it easier for Americans to get the medications they need, when they need them.
Source: 1-33
Content: The V.A. is pioneering new ways of linking toxic exposures to disease, already helping  veterans get the care they deserve. \n\nWe need to extend that same care to all Americans. \n\nThat’s why I’m calling on Congress to pass legislation that would establish a national registry of toxic exposures, and provide health care and financial assistance to those affected.
Source: 1-30
=========
FINAL ANSWER: The purpose of ARPA-H is to drive breakthroughs in cancer, Alzheimer’s, diabetes, and more.
SOURCES: 1-32

---------

QUESTION: {question}
=========
{summaries}
=========
FINAL ANSWER:"""

STUFF_PROMPT = PromptTemplate(
    template=template, input_variables=["summaries", "question"]
)


def split_text_into_chunks(text, model):
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        # , length_function=len  # 800
        model_name=model, chunk_size=256, chunk_overlap=20,
    )
    chunked_docs = []
    chunks = text_splitter.split_text(text)
    for i, chunk in enumerate(chunks):
        doc = Document(
            page_content=chunk,
            metadata={"page": "1", "chunk": i + 1, "source": "1-1"},
        )
        chunked_docs.append(doc)
    return chunked_docs


def create_vectorstore(text_chunks, openai_api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return FAISS.from_documents(documents=text_chunks, embedding=embeddings)


def query_file(query, openai_api_key, model, vectorstore):
    if "gpt" in model:
        llm = ChatOpenAI(
            openai_api_key=openai_api_key, temperature=0.25, model=model
        )
    else:
         llm = OpenAI(
            openai_api_key=openai_api_key, temperature=0.25, model=model
        )
    chain = load_qa_with_sources_chain(
        llm=llm,
        chain_type="stuff",
        prompt=STUFF_PROMPT,
    )

    relevant_docs = vectorstore.similarity_search(query, k=5)
    result = chain(
        {"input_documents": relevant_docs, "question": query}, return_only_outputs=True
    )

    return result["output_text"].split("SOURCES: ")[0]
