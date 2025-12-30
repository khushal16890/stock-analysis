# stock-analysis
This application helps users analyze stocks using fundamental data instead of price movement. It is designed to answer three practical questions.  Which stocks are fundamentally similar How diversified is a portfolio What type of stock each company is  .

Overview

This project is a fundamental stock analysis application built using Python and Streamlit.
It focuses on understanding companies through financial metrics rather than predicting prices.

The application provides three independent tools.

Similar Stock Finder
Portfolio Diversification Score
Stock Type Classification

All models and calculations are prepared in advance and stored in a single artifact file.
The user interface only loads and displays results.

milar Stock Finder

Allows users to select a stock and view other stocks that are fundamentally similar.
Similarity is based on weighted financial indicators such as profitability, growth, valuation, and capital efficiency.

Portfolio Diversification Score

Measures how diversified a selected portfolio is.
The score is calculated using cosine similarity between stocks.
Lower similarity means better diversification.

Stock Type Classification

Classifies stocks into four broad types.

Growth stocks
Value stocks
Dividend stocks
Capital efficient stocks

Classification is based on dominant financial characteristics.
