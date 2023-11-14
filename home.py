import streamlit as st
import 残高試算表
import 変換

# 初期状態では何も表示しないようにセッション状態を設定
if 'current_app' not in st.session_state:
    st.session_state['current_app'] = None

st.title('EG_R4→freee変換_home')

# ボタンが押されたときに実行する関数
def show_app1():
    st.session_state['current_app'] = 'app1'

def show_app2():
    st.session_state['current_app'] = 'app2'

# アプリ選択用のボタン
if st.button('残高試算表(txtファイル)'):
    show_app1()

if st.button('仕訳(csvファイル)'):
    show_app2()

# 選択されたアプリを表示
if st.session_state['current_app'] == 'app1':
    残高試算表.app1()
elif st.session_state['current_app'] == 'app2':
    変換.app2()
