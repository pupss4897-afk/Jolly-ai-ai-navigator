import streamlit as st
import google.generativeai as genai

# 1. 網頁基礎設定
st.set_page_config(page_title="綸綸老師專業AI", page_icon="🚀", layout="wide")

# 科技感樣式
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00f3ff; }
    h1 { color: #00f3ff; text-shadow: 0 0 10px #00f3ff; text-align: center; font-size: 3em; }
    .stTextInput>div>div>input, .stTextArea>div>div>textarea { background-color: #1a1c23; color: white; border: 1px solid #00f3ff; }
    .stButton>button { background-color: #00f3ff; color: black; font-weight: bold; border-radius: 10px; width: 100%; height: 3em; }
    .report-box { background: #1a1c23; padding: 25px; border-radius: 15px; border-left: 5px solid #00f3ff; color: #eee; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 綸綸老師專業AI：短影音成功導航儀")

# 2. 自動連接模型
@st.cache_resource
def load_brain():
    if "GEMINI_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
        # 遍歷可用模型
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                if '1.5-flash' in m.name: return genai.GenerativeModel(m.name)
        return genai.GenerativeModel('gemini-pro')
    return None

model = load_brain()

# 3. 主界面
video_url = st.text_input("1. 影片網址 (供 AI 參考連結架構)：")
video_content = st.text_area("2. 影片標題或內容描述 (貼上內容 AI 才能精準診斷)：", placeholder="例如：這是一個關於『如何解決人口老化』的搞笑反差影片，標題是...，裡面大概講了...")

if st.button("開啟深度診斷"):
    if not video_content:
        st.warning("⚠️ 請至少輸入一些影片的內容描述，AI 才能進行精準診斷喔！")
    elif not model:
        st.error("❌ 大腦未連線，請檢查 API Key")
    else:
        prompt = f"""
        你現在是擁有九年經驗的短影音專家『綸綸老師』。
        
        【待診斷影片資訊】
        網址：{video_url}
        內容內容：{video_content}
        
        請根據這份內容，嚴格遵守『九年心法』產出報告：
        ### 📊 綸綸老師專業診斷報告
        
        #### 1. 【0-3s Hook 開場分析】
        針對標題『{video_content[:20]}...』與開場邏輯，分析是否具備衝突感。
        
        #### 2. 【4-45s 中段結構拆解】
        分析其內容節奏，是否能讓觀眾產生收藏欲望。
        
        #### 3. 【45-60s 尾部轉化建議】
        分析其結尾是否有強大的 CTA。
        
        #### 4. 【爆款標題改寫】
        給出 3 組更有攻擊力的『懲罰式反差標題』。
        
        語氣：專業、犀利、直接點出病灶。
        """
        
        with st.spinner("🧠 正在對照九年心法..."):
            response = model.generate_content(prompt)
            st.markdown("<div class='report-box'>", unsafe_allow_html=True)
            st.markdown(response.text)
            st.markdown("</div>", unsafe_allow_html=True)
