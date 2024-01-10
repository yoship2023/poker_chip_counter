import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

def poker_chip_counter():
    st.title("チップかぞえチャオ")

    # チップの数とBBの入力フィールド
    bb_value = st.number_input("1BBの点数", value=200, step=100)
    black_chips = st.number_input("100点（⚫️黒いチップ）の数", value=0)
    purple_chips = st.number_input("500点（🟣紫色チップ）の数", value=0)
    blue_chips = st.number_input("1,000点（🔵青いチップ）の数", value=0)
    yellow_chips = st.number_input("5,000点（🟡黄色チップ）の数", value=0)
    red_chips = st.number_input("25,000点（🔴赤いチップ）の数", value=0)
    white_chips = st.number_input("100,000点（⚪️赤いチップ）の数", value=0)
    light_purple_chips = st.number_input("1,000,000点（薄紫チップ）の数", value=0)

    # 計算ボタン
    if st.button("計算"):
        # 合計計算
        total_chips = black_chips * 100 + purple_chips * 500 \
            + blue_chips * 1000 + yellow_chips * 5000 \
            + red_chips * 25000 + white_chips * 100000 + light_purple_chips * 1000000
        # BB表記への変換
        total_bb = total_chips / bb_value
        st.write(f"合計チップ数: {total_chips:,} チップ ({total_bb:,.2f} BB)")

    # 現在時刻の表示
    current_time = datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y-%m-%d %H:%M:%S")
    # メモ欄
    memo_title = "メモ 現在時刻（JST）: " + current_time
    memo = st.text_area(memo_title, "")

if __name__ == "__main__":
    poker_chip_counter()