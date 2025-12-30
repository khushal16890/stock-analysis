import streamlit as st
import pickle
import numpy as np
import pandas as pd
from itertools import combinations

@st.cache_resource
def load_models():
    with open("stock_models.pkl", "rb") as f:
        return pickle.load(f)

models = load_models()
similarity_df = models["similarity_df"]

st.title("📊 Portfolio Diversification Score")

portfolio = st.multiselect(
    "Select at least 2 stocks",
    similarity_df.index
)

def portfolio_diversity_score(portfolio):
    pairs = list(combinations(portfolio, 2))
    similarities = [similarity_df.loc[a, b] for a, b in pairs]
    score = 1 - np.mean(similarities)

    detail = pd.DataFrame(pairs, columns=["Stock A", "Stock B"])
    detail["Similarity"] = similarities

    return round(score, 3), detail.sort_values("Similarity", ascending=False)

if len(portfolio) >= 2:
    score, detail = portfolio_diversity_score(portfolio)

    st.metric("Diversification Score", score)
    st.dataframe(detail, use_container_width=True)

elif len(portfolio) > 0:
    st.warning("Select at least 2 stocks")
