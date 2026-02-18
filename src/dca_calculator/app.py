# src/dca_calculator/app.py
import streamlit as st

from core import dca_calculate

st.set_page_config(
    page_title="DCA Calculator by LVKSH©",
    page_icon="🚀",
    layout="centered",
)

st.title("🚀 DCA (Dollar Cost Averaging) Calculator")
st.caption("by LVKSH© / @lvksh.py")

usd_amount = st.number_input(
    "Monthly investment (USD)",
    min_value=0.0,
    value=100.0,
    step=10.0,
)

apy_input = st.number_input(
    "APY (annual %)",
    min_value=0.0,
    value=10.0,
    step=0.1,
)

months = st.number_input(
    "Number of months",
    min_value=1,
    value=12,
    step=1,
)

deposit_timing_label = st.selectbox(
    "When do you invest each month?",
    options=["End of month (default)", "Beginning of month"],
)

timing = "end" if deposit_timing_label == "End of month (default)" else "begin"

try:
    result = dca_calculate(
        monthly_contribution=usd_amount,
        apy_percent=apy_input,
        months=int(months),
        timing=timing,
    )
except ValueError as e:
    st.error(str(e))
    st.stop()

total = result["total"]
principal = result["principal"]
extra = result["extra"]
roi = result["roi"]
monthly_rate = result["monthly_rate"]

st.divider()

col1, col2, col3 = st.columns(3)
col1.metric("Invested (Principal)", f"${principal:,.2f}")
col2.metric("Profit (Extra)", f"${extra:,.2f}")
col3.metric("ROI", f"{roi:.2f}%")

st.subheader("Total Portfolio Value")
st.success(f"${total:,.2f}")

with st.expander("Details"):
    st.write(f"Monthly rate: **{monthly_rate * 100:.4f}%**")
    st.write(f"APY: **{apy_input:.2f}%**")
    st.write(f"Timing: **{timing}**")

st.divider()
st.caption(
    "⚠️ Projection does not include inflation, taxation, "
    "transaction costs, management fees, or market risk. "
)
