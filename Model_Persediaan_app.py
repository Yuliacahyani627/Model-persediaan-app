import streamlit as st
import math

st.set_page_config(layout="centered")
st.title("📦 Model Persediaan EOQ (Economic Order Quantity)")

st.markdown("""
Model ini membantu menentukan jumlah pembelian optimal untuk meminimalkan total biaya persediaan.

### Rumus:
$EOQ = \\sqrt{\\frac{2DS}{H}}$
""")

st.subheader("📥 Masukkan Parameter:")

D = st.number_input("Permintaan tahunan (D)", min_value=1, value=10000)
S = st.number_input("Biaya pemesanan per pesanan (S)", min_value=1, value=50000)
H = st.number_input("Biaya penyimpanan per unit per tahun (H)", min_value=1, value=2000)

if st.button("Hitung EOQ"):
    eoq = math.sqrt((2 * D * S) / H)
    st.success(f"Jumlah pemesanan optimal (EOQ): {eoq:.2f} unit")

    biaya_total = (D / eoq) * S + (eoq / 2) * H
    st.write(f"Estimasi Total Biaya Persediaan: Rp {biaya_total:,.0f}")
