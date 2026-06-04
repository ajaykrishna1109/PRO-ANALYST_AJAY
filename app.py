import streamlit as st
import time

from rag import retrieve_docs
from api import ask_llm

st.set_page_config(
    page_title="Upwork AI Consultant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>

.main {
background-color:#0f172a;
}

.stTextInput>div>div>input{
border-radius:15px;
}

.answer-box{
padding:20px;
background:#111827;
border-radius:15px;
border-left:5px solid #3b82f6;
}

.source-box{
padding:15px;
background:#1f2937;
border-radius:12px;
margin-bottom:10px;
}

</style>
""", unsafe_allow_html=True)

st.title("🤖 Upwork API AI Consultant")

st.caption(
"RAG + ChromaDB + Llama 3.1 + Streamlit"
)

query = st.text_input(
    "Ask anything about Upwork API"
)

if query:

    start_time = time.time()

    docs = retrieve_docs(query)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    answer = ask_llm(
        context,
        query
    )

    latency = round(
        time.time()-start_time,
        2
    )

    st.markdown(
        f"""
        <div class="answer-box">
        {answer}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.metric(
        "Latency",
        f"{latency} sec"
    )

    st.subheader("📚 Sources")

    for doc in docs:

        st.markdown(
            f"""
            <div class="source-box">
            {doc.page_content}
            </div>
            """,
            unsafe_allow_html=True
        )