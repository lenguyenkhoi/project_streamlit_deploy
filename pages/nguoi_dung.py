import streamlit as st
# st.set_page_config(layout="wide",page_title="Dashboard")

# st.markdown("<hr />",True)

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True) #ẩn các pagelink
# Xử lý Sidebar
st.sidebar.header("Menu")

# st.sidebar.radio("Điều hướng", ["Trang chủ", "Báo cáo", "Người dùng","Cài đặt"])
st.sidebar.page_link("pages/bao_cao.py",label="Báo cáo")
st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/trang_chu.py",label="Trang chủ")
st.sidebar.page_link("pages/bt_menu.py",label="Bài tập menu")