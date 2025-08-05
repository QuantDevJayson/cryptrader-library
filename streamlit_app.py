
import streamlit as st
from cryptrader.analytics import ExchangeAnalytics
from cryptrader.settings import Settings

st.set_page_config(page_title="CrypTrader Live Dashboard", layout="wide", initial_sidebar_state="expanded")

# --- Sidebar ---
with st.sidebar:

    st.title("CrypTrader Dashboard")
    st.caption("High-Performance Modular Crypto Trading & Merchant Integration Library")
    st.markdown("---")
    st.header("Select Exchange & Symbol")
    settings = Settings('settings.json')
    analytics = ExchangeAnalytics(settings)
    exchange = st.selectbox("Exchange", settings.list_exchanges())
    symbol = st.text_input("Symbol", "BTC")
    st.markdown("---")
    st.info("All analytics are mock/demo for UI showcase. Integrate real APIs for production.")

# --- Main Layout ---
st.header("About CrypTrader")
st.markdown("""
**CrypTrader** is a live, production-grade Python library powering real-time analytics, monitoring, and trading across 150+ top crypto exchanges and merchants. This dashboard demonstrates its modular, high-performance, and secure architecture in action.

**Features:**
- Modern, clean, finance-grade UI
- Real-time analytics and monitoring
- Modular, extensible integrations
- Secure and high-performance async architecture

**Use Cases:**
- Portfolio and risk management
- Compliance and breach monitoring
- Arbitrage and liquidity analysis
- Merchant and exchange integration
""")

st.markdown("---")

st.markdown("""
<style>
.metric-label { font-size: 1.1em; color: #888; }
.metric-value { font-size: 2em; font-weight: bold; }
.stTabs [data-baseweb="tab"] { font-size: 1.1em; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

st.title(f"📊 Analytics for {exchange} - {symbol}")

tab1, tab2, tab3, tab4 = st.tabs([
    "Liquidity & Risk", "Compliance", "Breach & Sentiment", "Arbitrage"
])

with tab1:
    st.subheader("Liquidity & Risk Overview")
    if st.button("Check Liquidity", key="liq"):
        result = analytics.check_liquidity(exchange, symbol)
        col1, col2, col3 = st.columns(3)
        col1.metric("Exchange", result["exchange"])
        col2.metric("Liquidity", result["liquidity"], delta=None)
        col3.metric("Risk", result["risk"], delta=None)
        st.json(result)
    else:
        st.info("Click 'Check Liquidity' to view liquidity and risk metrics.")

with tab2:
    st.subheader("Compliance Check")
    if st.button("Check Compliance", key="comp"):
        result = analytics.check_compliance(exchange)
        st.metric("Compliance Status", result["compliance"].capitalize())
        st.json(result)
    else:
        st.info("Click 'Check Compliance' to view compliance status.")

with tab3:
    st.subheader("Breach & Sentiment Insights")
    if st.button("Get Breach Insights", key="breach"):
        result = analytics.get_breach_insights(exchange)
        col1, col2 = st.columns(2)
        col1.metric("Breach", "Yes" if result["breach"] else "No")
        col2.metric("Sentiment", result["sentiment"].capitalize())
        st.json(result)
    else:
        st.info("Click 'Get Breach Insights' to view breach and sentiment data.")

with tab4:
    st.subheader("Arbitrage Opportunities")
    if st.button("Get Arbitrage Opportunities", key="arb"):
        result = analytics.get_arbitrage_opportunities(symbol)
        st.write("### Opportunities:")
        st.json(result)
    else:
        st.info("Click 'Get Arbitrage Opportunities' to view arbitrage data.")

# --- Footer ---
st.markdown("""
<hr style='margin-top:2em;margin-bottom:0.5em;border:1px solid #eee;'>
<div style='text-align:center;font-size:0.95em;color:#888;'>
<b>CrypTrader</b> is part of a live project under active development.<br>
Authored by <b>@QuantDevJayson</b>
</div>
""", unsafe_allow_html=True)