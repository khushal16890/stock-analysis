import streamlit as st
import pickle

@st.cache_resource
def load_models():
    with open("stock_models.pkl", "rb") as f:
        return pickle.load(f)

models = load_models()
similarity_df = models["similarity_df"]

st.title("📌 Similar Stock Finder")

stock = st.selectbox(
    "Select a stock",
    similarity_df.index
)

top_n = st.slider(
    "Number of similar stocks",
    min_value=5,
    max_value=30,
    value=10
)

if stock:
    result = (
        similarity_df.loc[stock]
        .drop(stock)
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
        .rename(columns={"index": "Stock", stock: "Similarity"})
    )

    st.dataframe(result, use_container_width=True)
