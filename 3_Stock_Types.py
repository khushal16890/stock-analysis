import streamlit as st
import pickle
import pandas as pd

@st.cache_resource
def load_models():
    with open("stock_models.pkl", "rb") as f:
        return pickle.load(f)

models = load_models()
cluster_map = models["cluster_map"]
cluster_labels = models["cluster_labels"]

df = pd.read_csv("company.csv")

df["Cluster"] = df["Name"].map(cluster_map)
df["Stock Style"] = df["Cluster"].map(cluster_labels)

st.title("🏷 Stock Type Classification")

st.dataframe(
    df[["Name", "Stock Style"]],
    use_container_width=True
)
