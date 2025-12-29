import streamlit as st
import google.generativeai as genai

# 1. 網頁基礎設定
st.set_page_config(page_title="綸綸老師專業AI", page_icon="🚀", layout="wide")

# 科技感樣式 CSS
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

# 2. 連接大腦 (直接指定型號，不再自動抓取以避免錯誤)
def init_model():
    if "GEMINI_API_KEY" in st.secrets:
        try:
            genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
            # 直接使用最穩定的 1.5 Flash 大腦
            return genai.GenerativeModel('gemini-1.5-flash')
        except Exception as e:
            st.error(f"❌ 大腦配置出錯：{e}")
            return None
    return None

model = init_model()

# 3. 主界面
video_url = st.text_input("1. 影片網址 (供 AI 參考連結)：")
video_content = st.text_area("2. 影片標題或內容描述 (這是診斷的關鍵！)：", 
                            placeholder="例如：標題是『如何解決人口老化』，裡面講了...。貼上越多資訊，診斷越精準！",
                            height=150)

if st.button("開啟深度診斷"):
    if not video_content:
        st.warning("⚠️ 綸綸老師提醒：請先輸入影片內容或標題，我才能幫你診斷喔！")
    elif not model:
        st.error("❌ 大腦未連線，請檢查 Secrets 中的 API Key 是否正確。")
    else:
        # 強化的九年心法指令
        prompt = f"""
        你現在是擁有九年經驗的短影音品牌戰略總監『綸綸老師』。
        
        【待診斷影片資訊】
        - 連結：{video_url}
        - 內容描述：{video_content}
        
        請根據這份內容，運用你的專業心法產出深度拆解報告：
        
        ### 📊 綸綸老師專業診斷報告
        
        #### 1. 【0-3s Hook 開場分析】
        針對其開場邏輯，分析是否具備足夠的衝突感來止住滑動。
        
        #### 2. 【4-45s 中段結構拆解】
        分析信息密度與視覺節奏，是否能觸發觀眾的『收藏與重複觀看』。
        
        #### 3. 【45-60s 尾部轉化建議】
        分析其結尾是否有強大的 CTA (行動引導)。
        
        #### 4. 【爆款標題改寫】
        請幫這部片改寫 3 組更有攻擊力的『懲罰式反差標題』。
        
        語氣要求：犀利、專業、直接點出失敗或成功的關鍵點。
        """
        
        with st.spinner("🧠 正在讀取九年心法，大腦運算中..."):
            try:
                # 執行生成
                response = model.generate_content(prompt)
                
                # 顯示報告
                st.markdown("<div class='report-box'>", unsafe_allow_html=True)
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
                
            except Exception as e:
                st.error(f"分析時發生技術錯誤：{e}")
                st.info("建議：請檢查 Google AI Studio 的 API Key 是否有效，或嘗試稍後再試。")
