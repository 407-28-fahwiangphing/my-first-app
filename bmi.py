import streamlit as st
st.markdown("# :blue[แอปพลิเคชันคำนวนดัชนีมวลกายBMI]")
st.write("กรอกข้อมูลน้ำหนักและส่วนสูงของคุณ เพื่อเช็คสุขภาพเบื้องต้น")

weight = st.number_input("กรอกน้ำหนักของคุณ(กิโลกรัม):")
height_cm = st.number_input("กรอกส่วนสูงของคุณ(เซนติเมตร):")

if st.button("คำนวนค่า BMI"):
   # แปลงส่วนสูงจาก cm เป็น m แล้วคำนวน BMI
   height_m = height_cm ** 2
   bmi = weight / (height_m ** 2)

   st.write("---")
   st.header(f"ค่าbmiของคุณคือ: **{bmi:.2f}**")

   if bmi < 18.5:
      st.warning("คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
   elif 18.5 <= bmi < 23.0:
      st.success("คุณมีน้ำหนักอยู่ในเกณฑ์ปกติ (สุขภาพดี)")
   elif 23.0 <= bmi < 25.0:
      st.info("คุณเริ่มมีน้ำหนักเกินเกินฑ์ (ท้วม)")
   else:
      st.eror("คุณอยู่ในเกณฑ์อ้วน ควรระวังเรื่องสุขภาพและออกกำลังกาย")

st.divider()
st.write("นางสาวฟ้าเวียงพิงค์ จันทร์กระจ่าง เลขที่28 ม.4/7")
