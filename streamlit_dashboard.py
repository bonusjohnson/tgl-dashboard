import streamlit as st
import pandas as pd
import yfinance as yf
from datetime import datetime

st.set_page_config(
    page_title="TGL Investment Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(\"\"\"
    <style>
        body {
            font-family: 'Inter', sans-serif;
        }
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
        .css-1d391kg {
            background-color: #f0f2f6;
        }
    </style>
\"\"\", unsafe_allow_html=True)

st.sidebar.header("Watchlist Filters")
section = st.sidebar.selectbox("Choose Section", ["Portfolio", "Watchlist", "TGLive1MM"])

TGLIVE_TICKERS = ["SU.PA", "SIE.DE", "ETN", "CRVW", "MELI", "DDOG", "SMCI", "WELL.TO", "TOI.V"]

def fetch_data(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            current_price = hist["Close"].iloc[-1] if not hist.empty else 0
            data.append({
                "Ticker": ticker,
                "Price": round(current_price, 2),
                "Date": datetime.now().strftime('%Y-%m-%d')
            })
        except Exception:
            data.append({"Ticker": ticker, "Price": "Error", "Date": datetime.now().strftime('%Y-%m-%d')})
    return pd.DataFrame(data)

st.title("📊 TGLive Investment Dashboard")
st.markdown(\"\"\"
    This modular, real-time investment dashboard allows you to monitor live market data across your Portfolio,
    Watchlist, and the TGLive1MM segment. Choose a section on the left to begin.
\"\"\")

if section == "TGLive1MM":
    st.subheader("🔎 TGLive1MM Real-Time Data")
    tickers = TGLIVE_TICKERS
elif section == "Watchlist":
    st.subheader("📌 Watchlist Overview")
    tickers = TGLIVE_TICKERS
else:
    st.subheader("💼 Portfolio Overview")
    tickers = TGLIVE_TICKERS

data_df = fetch_data(tickers)
st.dataframe(data_df, use_container_width=True)

st.markdown("---")
st.markdown(\"\"\"
    Designed in the aesthetic spirit of OpenAI and Perplexity: clean, modular, and responsive.

    **Customize:** Add more filters, charts, or connect to your investment logic layer.
\"\"\")
