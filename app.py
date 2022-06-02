import streamlit as st
from annotated_text import annotated_text
import requests
import os
from utils import my_table, create_tbody

# ===========================================#
#                 SideBar                   #
# ===========================================#
# st.sidebar.title("📖 Classificador gramatical")
# st.sidebar.markdown("Você pode escolher um das anotações abaixo:")

# tagset = st.sidebar.selectbox(
#    "Qual você prefere?", ("Spacy", "Bosque", "GSD", "Linguateca", "Macmorpho")
# )

API_URL = os.getenv("API_URL")


def get_classification(text):
    r = requests.get(os.path.join(API_URL, "get_classification"), params={"text": text})
    if r.status_code == 200:
        data = r.json()
        tagged_words, frase_morph, tokens = (
            data["tagged_words"],
            data["frase_morph"],
            data["tokens"],
        )
        tagged_words = [tuple(l) if type(l) == list else " " for l in tagged_words]
        return tagged_words, frase_morph, tokens
    else:
        return None, None, None


def get_tip():
    r = requests.get(os.path.join(API_URL, "get_tip"))
    if r.status_code == 200:
        data = r.json()
        return data["tip"]


desc = "Classificador gramatical para fins didáticos!"


def main():
    st.info(get_tip())
    st.title("Classificador Gramatical")
    st.write(desc)
    user_input = st.text_input("Informe o seu texto aqui:")

    if st.button("Verificar") or user_input:
        tagged_words, frase_morph, tokens = get_classification(user_input)
        # print("tags: ", tagged_words)
        if tagged_words:
            annotated_text(*tagged_words)

        st.markdown("# Análise morfológica")
        if st.button("Analisar"):
            st.markdown(
                my_table.format(body=create_tbody(tokens, frase_morph)),
                unsafe_allow_html=True,
            )


if __name__ == "__main__":
    main()
