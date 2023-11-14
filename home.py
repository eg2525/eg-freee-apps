import streamlit as st
import 残高試算表
import 変換

st.title('EG_R4→freee変換_home')

# セッション状態の初期化
if 'current_app' not in st.session_state:
    st.session_state['current_app'] = None  # 現在表示するアプリを保持する変数

# ボタンが押されたときのアクションを定義する
def show_app1():
    st.session_state['current_app'] = 'app1'

def show_app2():
    st.session_state['current_app'] = 'app2'

# アプリ選択用のボタン
col1, col2 = st.columns(2)
with col1:
    st.button('残高試算表', on_click=show_app1)
with col2:
    st.button('仕訳', on_click=show_app2)

# 選択されたアプリに基づいて表示を変更
if st.session_state['current_app'] == 'app1':
    残高試算表.app1()
elif st.session_state['current_app'] == 'app2':
    変換.app2()
