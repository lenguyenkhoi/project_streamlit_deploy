import streamlit as st

st.set_page_config(layout="wide",page_title="Dashboard")

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
st.sidebar.page_link("app.py",label="Điều hướng")
st.sidebar.page_link("pages/bao_cao.py",label="Báo cáo")
st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/trang_chu.py",label="Trang chủ")
st.sidebar.page_link("pages/bt_menu.py",label="Bài tập menu")


#Wrap_content
st.header("Admin Dashboard")

st.set_page_config(layout="wide")
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Doanh thu hôm nay" , "12.5M", "+5%")
with col2:
    st.metric("Người dùng mới", 327," +12")
with col3:
    st.metric("Đơn hàng",142,"-3")
with col4:
    st.metric('Tỉ lệ chuyển đổi', "3.8%" , "+0.4%")

st.markdown("<hr />",True)

doanh_thu, don_hang = st.columns(2)

with doanh_thu:
    lst_doanh_thu = [6,14,5,15,10]
    st.header("Doanh thu 5 ngày gần nhất")
    st.line_chart(lst_doanh_thu)

with don_hang:
    lst_don_hang = [15,35,50,16]
    st.header("Số lượng đơn hàng theo trạng thái")
    st.bar_chart(lst_don_hang)
