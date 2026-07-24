import streamlit as st
st.title("คำนวนสินค้าราคารวมภาษี7%")
bh_x=st.number_input("กรอกราคาสินค้า")
ce_x=bh_x*1.07
st.header(f"ราคาสินค้ารวมภาษีคือ : {ce_x}")
