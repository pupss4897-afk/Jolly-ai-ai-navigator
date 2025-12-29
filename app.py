import streamlit as st
import google.generativeai as genai

# 網頁基礎設定
st.set_page_config(page_title="綸綸老師專業AI", page_icon="🚀", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00f3ff; }
    h1 { color: #00f3ff; text-shadow: 0 0 10px #00f3ff; text-align: center; font-size: 3em; }
    .stTextInput>div>div>input { background-color: #1a1c23; color: white; border: 1px solid #00f3ff; }
    .stButton>button { background-color: #00f3ff; color: black; font-weight: bold; border-radius: 10px; width: 100%; height: 3em; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 綸綸老師專業AI：短影音成功導航儀")

with st.sidebar:
    st.header("⚙️ 系統設定")
    api_key = st.text_input("輸入 Gemini API Key", type="password")

video_url = st.text_input("請貼上影片網址 (IG / 抖音 / 小紅書)：")

if st.button("開啟深度診斷"):
    if not api_key:
        st.error("❌ 請先輸入 API Key！")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-1.5-pro')
            prompt = f"你現在是擁有九年經驗的短影音專家綸綸老師，請分析這部影片：{video_url}。請從開頭Hook、中段信息量、尾部CTA進行專業拆解並給出3個優化標題。"
            with st.spinner("診斷中..."):
                response = model.generate_content(prompt)
                st.subheader("📊 專業診斷報告")
                st.write(response.text)
        except Exception as e:
            st.error(f"出錯了：{e}")
