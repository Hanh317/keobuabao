import streamlit as st
import random
import time

st.set_page_config(page_title="Võ Lâm Tranh Đấu", page_icon="⚔️", layout="centered")

# --- PHẦN GIAO DIỆN ---
st.title("⚔️ Võ Lâm Tranh Đấu")
st.markdown("Chào mừng đến với trò chơi Kéo – Búa – Bao phiên bản Web!")

# --- PHÁT NHẠC NỀN ---
with open("vo_lam_theme.mp3", "rb") as f:
    st.audio(f.read(), format="audio/mp3", start_time=0)

# --- NHẬP TÊN NGƯỜI CHƠI ---
player_name = st.text_input("🎮 Nhập tên người chơi:", "Khách")

# --- NÚT BẮT ĐẦU ---
if st.button("BẮT ĐẦU TRẬN ĐẤU"):
    st.success(f"Chúc {player_name} may mắn!")

    options = ["Kéo", "Búa", "Bao"]
    user_choice = st.radio("Bạn chọn:", options, horizontal=True)

    if st.button("👊 RA CHIÊU!"):
        start_time = time.time()

        bot_choice = random.choice(options)
        st.write(f"🤖 Máy chọn: {bot_choice}")

        if user_choice == bot_choice:
            st.info("🤝 Hòa nhau rồi!")
        elif (user_choice == "Kéo" and bot_choice == "Bao") or \
             (user_choice == "Búa" and bot_choice == "Kéo") or \
             (user_choice == "Bao" and bot_choice == "Búa"):
            st.success(f"🎉 {player_name} chiến thắng!")
        else:
            st.error("😢 Bạn thua rồi!")

        elapsed = round(time.time() - start_time, 2)
        st.caption(f"🕒 Thời gian phản ứng: {elapsed} giây")

    st.experimental_rerun()
