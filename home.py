import streamlit as st
import 残高試算表
import 変換

# 初期化（初めて実行するときに、これらのキーがセッション状態に追加される）
if 'show_app1' not in st.session_state:
    st.session_state.show_app1 = True  # 残高試算表アプリを表示するかどうか
if 'show_app2' not in st.session_state:
    st.session_state.show_app2 = True  # 変換アプリを表示するかどうか

st.title('EG_R4→freee変換_home')

# アプリ選択用のボタン
if st.button('残高試算表'):
    st.session_state.show_app1 = True
    st.session_state.show_app2 = False
if st.button('仕訳'):
    st.session_state.show_app1 = False
    st.session_state.show_app2 = True

# 選択されたアプリを表示
if st.session_state.show_app1:
    残高試算表.app1()
if st.session_state.show_app2:
    変換.app2()
