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
st.sidebar.page_link("pages/bao_cao.py",label="Báo cáo")
st.sidebar.page_link("pages/cai_dat.py",label="Cài đặt")
st.sidebar.page_link("pages/nguoi_dung.py",label="Người dùng")
st.sidebar.page_link("pages/trang_chu.py",label="Trang chủ")
st.sidebar.page_link("pages/bt_menu.py",label="Bài tập menu")

#Dữ liệu của các món ăn {st.session_state.lst_mon_an}
if "lst_mon_an" not in st.session_state:
    st.session_state.lst_mon_an = []


st.title("MENU KFC MINI")

dict_menu_gia = {
    "ga_ran":35_000,
    "bo":45_000,
    "khoai":25_000,
    "pepsi":15_000,
    "kem":40_000
}

dict_menu = {
    "ga_ran":35_000,
    "bo":45_000,
    "khoai":25_000,
    "pepsi":15_000,
    "kem":40_000
}

col_chon_mon_an, col_hoa_don = st.columns(2)

with col_chon_mon_an:
    frm_mon_an = st.form("frm_mon_an")
    with frm_mon_an:
        st.title("Chọn món ăn: ")
        dict_menu["ga_ran"] = st.number_input("Gà rán",min_value=1,max_value=10)
        dict_menu["bo"] = st.number_input("Bò",min_value=1,max_value=10)
        dict_menu["khoai"] = st.number_input("Khoai",min_value=1,max_value=10)
        dict_menu["pepsi"] = st.number_input("pepsi",min_value=1,max_value=10)
        dict_menu["kem"] = st.number_input("kem",min_value=1,max_value=10)
        btn = frm_mon_an.form_submit_button("Đặt món")
    
with col_hoa_don:
    st.title("Hóa đơn của bạn")
    lst_mon_an = []
    for key in dict_menu:
        lst_mon_an.append(
            {
                "Món ăn" : key,
                "Đơn giá": dict_menu_gia[key],
                "Số lượng": dict_menu[key],
                "Thành tiền":dict_menu_gia[key] * dict_menu[key]
            }
        )

    st.table(lst_mon_an)
    tong_tien = 0
    for item in lst_mon_an:
        tong_tien+= item["Thành tiền"]
    st.title(f"Tổng hóa đơn: {tong_tien}")