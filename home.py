import streamlit as st
import 残高試算表
import 変換
import 仕訳インポート

# 初期状態では何も表示しないようにセッション状態を設定
if 'current_app' not in st.session_state:
    st.session_state['current_app'] = None

st.title('EG_R4→freee変換_home')

# ボタンが押されたときに実行する関数
def show_app1():
    st.session_state['current_app'] = 'app1'

def show_app2():
    st.session_state['current_app'] = 'app2'

def show_app3():
    st.session_state['current_app'] = 'app3'

# アプリ選択用のボタン
if st.button('残高試算表(txtファイル)'):
    show_app1()

if st.button('R4→仕訳(csvファイル)'):
    show_app2()

# app3のためのボタンを追加します
if st.button('その他→仕訳インポート(xlsxファイル)'):
    show_app3()

# 選択されたアプリを表示
if st.session_state['current_app'] == 'app1':
    残高試算表.app1()
elif st.session_state['current_app'] == 'app2':
    変換.app2()
# app3が選択された時の処理を追加します
elif st.session_state['current_app'] == 'app3':
    app3.app3()
