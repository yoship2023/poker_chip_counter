import streamlit as st

def poker_chip_counter():
    st.title("チップかぞえチャオ")

    # チップの数とBBの入力フィールド
    bb_value = st.number_input("1BBのチップ数", value=200)
    black_chips = st.number_input("100点（黒いチップ）の数", value=0)
    purple_chips = st.number_input("500点（紫色のチップ）の数", value=0)
    blue_chips = st.number_input("1000点（青いチップ）の数", value=0)
    yellow_chips = st.number_input("5000点（黄色のチップ）の数", value=0)
    red_chips = st.number_input("25000点（赤いチップ）の数", value=0)

    # 計算ボタン
    if st.button("計算"):
        # 合計計算
        total_chips = black_chips * 100 + purple_chips * 500 + blue_chips * 1000  + yellow_chips * 5000  + red_chips * 25000
        # BB表記への変換
        total_bb = total_chips / bb_value
        st.write(f"合計チップ数: {total_chips} チップ ({total_bb} BB)")

if __name__ == "__main__":
    poker_chip_counter()