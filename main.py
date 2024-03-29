import streamlit as st

st.header("          业务方案验证AI助手")

with st.sidebar:
    openai_api_name = st.text_input("请输入你的账号：")
    openai_api_key = st.text_input("请输入你的密码：")
# st.markdown("[获取API密钥](https://platform.openai.com)")

theme = st.text_input("请选择表名")
theme1 = st.text_input("请输入内容")
submit = st.button("生成SQL")

# theme2 = st.text_input("请输入你想查询的内容")
# submit1 = st.button("生成SQL语句并执行")