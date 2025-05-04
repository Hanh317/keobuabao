
import streamlit as st
import random
import time
from datetime import datetime

st.set_page_config(page_title="⚔️ Võ Lâm Tranh Đấu", page_icon="⚔️")

choices = ["Song kiếm trảm", "Long quyền chưởng", "Ngũ đao phi vũ"]
icons = {"Song kiếm trảm": "✌", "Long quyền chưởng": "✊", "Ngũ đao phi vũ": "🖐"}

if "started" not in st.session_state:
    st.session_state.started = False
    st.session_state.name = ""
    st.session_state.score = {"win": 0, "lose": 0, "draw": 0}
    st.session_state.start_time = None

st.title("⚔️ Võ Lâm Tranh Đấu – Bản Tuyệt Kỹ")
if not st.session_state.started:
    st.markdown("### Nhập tên người chơi:")
    st.session_state.name = st.text_input("Tên của ngươi là gì, thiếu hiệp?")
    
    st.markdown("### Bật nhạc nền?")
    music_on = st.checkbox("🎵 Bật nhạc võ lâm", value=True)

    if st.button("🔥 Bắt đầu tỉ thí!"):
        st.session_state.started = True
        st.session_state.start_time = datetime.now()
        if music_on:
            st.audio("https://youtu.be/15Ow9TEkiXY", format="audio/mp3", start_time=0)
        st.experimental_rerun()
    st.stop()

st.markdown(f"### Người chơi: **{st.session_state.name}**")
time_played = datetime.now() - st.session_state.start_time
st.markdown(f"⏳ Thời gian đã chơi: `{str(time_played).split('.')[0]}`")

st.markdown("## Xuất chiêu đi, kẻo bổn tọa nổi giận!")

player_choice = st.radio("Chọn chiêu thức:", choices, format_func=lambda x: f"{icons[x]} {x}")

if st.button("💥 Tỉ thí võ công!"):
    computer_choice = random.choice(choices)

    def get_result(player, computer):
        if player == computer:
            st.session_state.score["draw"] += 1
            return "⚖️ Chiêu này ngang tài ngang sức!"
        elif (player == "Song kiếm trảm" and computer == "Ngũ đao phi vũ") or              (player == "Long quyền chưởng" and computer == "Song kiếm trảm") or              (player == "Ngũ đao phi vũ" and computer == "Long quyền chưởng"):
            st.session_state.score["win"] += 1
            return "🏆 Không thể nào... Ngươi luyện chiêu ở môn phái nào vậy?"
        else:
            st.session_state.score["lose"] += 1
            return "❌ Còn non lắm! Học thêm 10 năm nữa đi!"

    result_text = get_result(player_choice, computer_choice)

    st.markdown(f"**Ngươi ra chiêu:** {icons[player_choice]} {player_choice}")
    st.markdown(f"**Ta ra chiêu:** {icons[computer_choice]} {computer_choice}")
    st.markdown(f"### {result_text}")

    st.success(f"✅ Thắng: {st.session_state.score['win']} | ❌ Bại: {st.session_state.score['lose']} | ⚖️ Hòa: {st.session_state.score['draw']}")

if st.button("🔁 Tái đấu"):
    st.experimental_rerun()

if st.button("📜 Tổng kết võ học"):
    win = st.session_state.score["win"]
    lose = st.session_state.score["lose"]
    draw = st.session_state.score["draw"]

    st.markdown(f"## 📜 Thiếu hiệp {st.session_state.name}, tổng kết võ công:")
    st.markdown(f"✅ Thắng: {win} | ❌ Bại: {lose} | ⚖️ Hòa: {draw}")

    if win > lose:
        st.success("🔥 Tuyệt đỉnh cao thủ, thiên hạ vô song!")
    elif win < lose:
        st.warning("🌪 Võ công còn yếu, cần tu luyện thêm!")
    else:
        st.info("⚖️ Ngang tài ngang sức, tái ngộ sau!")

if st.button("🏁 Kết thúc"):
    st.session_state.started = False
    st.experimental_rerun()
