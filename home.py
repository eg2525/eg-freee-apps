import streamlit as st
import 残高試算表
import 変換

st.title('EG_R4→freee変換_home')

# アプリ選択用のボタン
if st.button('残高試算表'):
    残高試算表.app1()
elif st.button('仕訳'):
    app2.run()
