import streamlit as st

st.title(f"แอปพลิเคชันแปลงปี พ.ศ. เป็น ค.ศ.")

bh_year = st.number_input("2554", value=2569)
ce_year = bh_year - 543

st.header(f"ปี ค.ศ. คือ : {ce_year}")
