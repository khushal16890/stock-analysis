import streamlit as st

st.set_page_config(
    page_title="Stock Analytics",
    layout="wide"
)

st.title("Stock Analytics Dashboard")

st.markdown("""
Tools available
            
->Similar Stocks Find fundamentally similar stocks
              
->Portfolio DiversityMeasure diversification using cosine similarity
              
->Stock Types Growth / Value / Dividend / Capital-Efficient  
""")
