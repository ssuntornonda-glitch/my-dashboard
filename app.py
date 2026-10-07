import streamlit as st
import pandas as pd
import plotly.express as px

# 1. ตั้งค่าหน้าเพจ
st.set_page_config(page_title="My Personal Dashboard", layout="wide")
st.title("📊 แดชบอร์ดส่วนตัวของ S.PITI")

# 2. เตรียมข้อมูล (สมมติว่าเป็นข้อมูลค่าใช้จ่าย)
data = {
    "หมวดหมู่": ["อาหาร", "เดินทาง", "ช้อปปิ้ง", "ที่อยู่อาศัย", "ความบันเทิง"],
    "จำนวนเงิน": [4500, 1200, 1500, 8000, 1000]
}
df = pd.DataFrame(data)

# 3. สร้างตัวกรอง (Sidebar)
st.sidebar.header("ตัวกรองข้อมูล")
selected_category = st.sidebar.multiselect(
    "เลือกหมวดหมู่ที่ต้องการดู:",
    options=df["หมวดหมู่"].unique(),
    default=df["หมวดหมู่"].unique()
)

# กรองข้อมูลตามที่เลือก
df_filtered = df[df["หมวดหมู่"].isin(selected_category)]

# 4. แสดงผลตัวเลขสำคัญ (Metrics)
col1, col2 = st.columns(2)
with col1:
    st.metric(label="งบประมาณทั้งหมด", value="20,000 บาท")
with col2:
    total_spent = df_filtered["จำนวนเงิน"].sum()
    st.metric(label="ยอดใช้จ่ายรวม (ที่เลือก)", value=f"{total_spent:,} บาท")

# 5. สร้างและแสดงกราฟ
st.subheader("วิเคราะห์สัดส่วนค่าใช้จ่าย")
fig = px.pie(df_filtered, values="จำนวนเงิน", names="หมวดหมู่", hole=0.4)
st.plotly_chart(fig, use_container_width=True)

# 6. แสดงตารางข้อมูล
st.subheader("ตารางข้อมูลดิบ")
st.dataframe(df_filtered)

