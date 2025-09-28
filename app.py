import streamlit as st
import pandas as pd
from controller import ItemController
from models import Item

st.set_page_config(page_title="Cadastro de Itens", layout="centered")

controller = ItemController()

st.title("Cadastro e Listagem de Itens")
st.write("Aplicação demonstrando arquitetura em camadas (Model / DAO / Controller / View).")

with st.form("form_cadastro"):
    st.subheader("Cadastrar novo item")
    nome = st.text_input("Nome")
    descricao = st.text_area("Descrição", height=80)
    quantidade = st.number_input("Quantidade", min_value=0, value=1, step=1)
    submit = st.form_submit_button("Cadastrar")

if submit:
    try:
        novo = controller.criarItem(nome=nome, descricao=descricao, quantidade=quantidade)
        st.success(f"Item cadastrado com sucesso (id={novo.id})")
    except Exception as e:
        st.error(f"Erro ao cadastrar item: {e}")

st.markdown("---")
st.subheader("Itens cadastrados")

items = controller.obterTodosOsItens()
if not items:
    st.info("Nenhum item cadastrado ainda.")
else:
    df = pd.DataFrame([{"id": it.id, "nome": it.nome, "descricao": it.descricao, "quantidade": it.quantidade} for it in items])
    st.dataframe(df, use_container_width=True)

st.markdown("---")
st.caption("Observação: este exemplo persiste itens em um arquivo SQLite local chamado 'items.db'.")