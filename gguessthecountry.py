import time
import streamlit as st

st.title("⏱️ เกมทายประเทศ")

# 1. กำหนดค่าเริ่มต้นใน session_state ถ้ายังไม่มี
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""
if "ans6_val" not in st.session_state:
    st.session_state.ans6_val = ""
if "ans7_val" not in st.session_state:
    st.session_state.ans7_val = ""
if "ans8_val" not in st.session_state:
    st.session_state.ans8_val = ""
if "ans9_val" not in st.session_state:
    st.session_state.ans9_val = ""
if "ans10_val" not in st.session_state:
    st.session_state.ans10_val = ""

# 📌 ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
def reset_game():
    st.session_state.start = time.time()  # เริ่มเวลาใหม่
    st.session_state.is_ended = False  # ปิด Dialog


# ----------------------------------------------------
# 📌 ฟังก์ชัน MessageBox (Dialog)
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10):
    st.balloons()
    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()
    u_ans6 = ans6.strip().lower()
    u_ans7 = ans7.strip().lower()
    u_ans8 = ans8.strip().lower()
    u_ans9 = ans9.strip().lower()
    u_ans10 = ans10.strip().lower()

    if u_ans1.strip().lower() in ["mexico", "แม็กซิโก"]:
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")
             
    if u_ans2.strip().lower() in ["egypt", "อียิปต์", "อียิป"]:
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")
    
    if u_ans3.strip().lower() in ["japan", "ญี่ปุ่น"]:
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")
    
    if u_ans4.strip().lower() in ["south korea", "เกาหลีใต้"]:
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")
             
    if u_ans5.strip().lower() in ["columbia", "โคลัมเบีย"]:
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")
    
    if u_ans6.strip().lower() in ["portugal", "โปรตุเกต", "โปรตุเกส", "โปรตุเกด"]:
        st.success("✅ ข้อ 6: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 6: ยังไม่ถูกต้อง (คุณตอบ '{u_ans6}')")
    if u_ans7.strip().lower() in ["france", "ฝรั่งเศส", "ฝรั่งเศด"]:
        st.success("✅ ข้อ 7: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 7: ยังไม่ถูกต้อง (คุณตอบ '{u_ans7}')")
    
    if u_ans8.strip().lower() in ["germany", "เยอรมนี"]:
        st.success("✅ ข้อ 8: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 8: ยังไม่ถูกต้อง (คุณตอบ '{u_ans8}')")
             
    if u_ans9.strip().lower() in ["argentina", "อาร์เจนตินา", "อาเจนตินา"]:
        st.success("✅ ข้อ 9: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 9: ยังไม่ถูกต้อง (คุณตอบ '{u_ans9}')")
    
    if u_ans10.strip().lower() in ["south africa", "แอฟริกาใต้"]:
        st.success("✅ ข้อ 10: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 10: ยังไม่ถูกต้อง (คุณตอบ '{u_ans10}')")

    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 10:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# 1. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

# 2. แถบแสดงเวลานับถอยหลัง
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    time_left = int(90 - (time.time() - st.session_state.start))

    if time_left > 0:
        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")
    else:
        st.session_state.is_ended = True
        st.rerun()

st.divider()

# 3. ช่องรับคำตอบ ใช้รูปภาพธงชาติผ่าน HTML
st.markdown("### ข้อ 1 <img src='https://flagcdn.com/w40/mx.png' width='30'>", unsafe_allow_html=True)
ans1 = st.text_input("ข้อ 1", value=st.session_state.ans1_val, label_visibility="collapsed")

st.markdown("### ข้อ 2 <img src='https://flagcdn.com/w40/eg.png' width='30'>", unsafe_allow_html=True)
ans2 = st.text_input("ข้อ 2", value=st.session_state.ans2_val, label_visibility="collapsed")

st.markdown("### ข้อ 3 <img src='https://flagcdn.com/w40/jp.png' width='30'>", unsafe_allow_html=True)
ans3 = st.text_input("ข้อ 3", value=st.session_state.ans3_val, label_visibility="collapsed")

st.markdown("### ข้อ 4 <img src='https://flagcdn.com/w40/kr.png' width='30'>", unsafe_allow_html=True)
ans4 = st.text_input("ข้อ 4", value=st.session_state.ans4_val, label_visibility="collapsed")

st.markdown("### ข้อ 5 <img src='https://flagcdn.com/w40/co.png' width='30'>", unsafe_allow_html=True)
ans5 = st.text_input("ข้อ 5", value=st.session_state.ans5_val, label_visibility="collapsed")

st.markdown("### ข้อ 6 <img src='https://flagcdn.com/w40/pt.png' width='30'>", unsafe_allow_html=True)
ans6 = st.text_input("ข้อ 6", value=st.session_state.ans6_val, label_visibility="collapsed")

st.markdown("### ข้อ 7 <img src='https://flagcdn.com/w40/fr.png' width='30'>", unsafe_allow_html=True)
ans7 = st.text_input("ข้อ 7", value=st.session_state.ans7_val, label_visibility="collapsed")

st.markdown("### ข้อ 8 <img src='https://flagcdn.com/w40/de.png' width='30'>", unsafe_allow_html=True)
ans8 = st.text_input("ข้อ 8", value=st.session_state.ans8_val, label_visibility="collapsed")

st.markdown("### ข้อ 9 <img src='https://flagcdn.com/w40/ar.png' width='30'>", unsafe_allow_html=True)
ans9 = st.text_input("ข้อ 9", value=st.session_state.ans9_val, label_visibility="collapsed")

st.markdown("### ข้อ 10 <img src='https://flagcdn.com/w40/za.png' width='30'>", unsafe_allow_html=True)
ans10 = st.text_input("ข้อ 10", value=st.session_state.ans10_val, label_visibility="collapsed")

# อัปเดตค่าล่าสุดเข้าตัวแปร
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5
st.session_state.ans6_val = ans6
st.session_state.ans7_val = ans7
st.session_state.ans8_val = ans8
st.session_state.ans9_val = ans9
st.session_state.ans10_val = ans10


# 4. ปุ่มส่งคำตอบ
if "start" in st.session_state and not st.session_state.get("is_ended", False):
    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()

    time.sleep(1)
    st.rerun()

# 5. แสดง Dialog ผลลัพธ์
if st.session_state.get("is_ended", False):
    show_result_dialog(ans1, ans2, ans3, ans4, ans5, ans6, ans7, ans8, ans9, ans10)

st.divider()
st.write("นาย ศุภกร ประสมสวย 45,
น.ส.ณัฎฐวี คำลือ 14,
น.ส.เกณิกา พูลทะจักร์ 21,
น.ส.ฟ้าเวียงพิงค์ จันทร์กระจ่าง 28
มัธยมศึกษาปีที่ 4/7")
