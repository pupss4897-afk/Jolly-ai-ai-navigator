import streamlit as st
import google.generativeai as genai

# 1. 網頁基礎設定
st.set_page_config(page_title="綸綸老師專業AI", page_icon="🚀", layout="wide")

# 科技感樣式
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #00f3ff; }
    h1 { color: #00f3ff; text-shadow: 0 0 10px #00f3ff; text-align: center; font-size: 3em; }
    .stTextInput>div>div>input { background-color: #1a1c23; color: white; border: 1px solid #00f3ff; }
    .stButton>button { background-color: #00f3ff; color: black; font-weight: bold; border-radius: 10px; width: 100%; height: 3em; }
    .report-box { background: #1a1c23; padding: 25px; border-radius: 15px; border-left: 5px solid #00f3ff; line-height: 1.8; color: #eee; }
    .status-text { color: #00f3ff; font-size: 0.9em; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 綸綸老師專業AI：短影音成功導航儀")
st.write("<p style='text-align: center; color: #888;'>全市場最強分析師：由 9 年實戰戰略驅動</p>", unsafe_allow_html=True)

# 2. 自動偵測並連接最強大腦
@st.cache_resource
def get_best_model(api_key):
    try:
        genai.configure(api_key=api_key.strip())
        # 掃描此 Key 支援的所有型號
        available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        
        # 優先順序：1.5-flash > 1.5-pro > gemini-pro
        if any("gemini-1.5-flash" in m for m in available_models):
            return "gemini-1.5-flash", "Gemini 1.5 Flash (最新高速大腦)"
        elif any("gemini-1.5-pro" in m for m in available_models):
            return "gemini-1.5-pro", "Gemini 1.5 Pro (旗艦大腦)"
        else:
            return "gemini-pro", "Gemini 1.0 Pro (穩定型大腦)"
    except Exception as e:
        return None, str(e)

# 讀取保險箱中的 Key
if "GEMINI_API_KEY" in st.secrets:
    api_key = st.secrets["GEMINI_API_KEY"]
    model_id, model_info = get_best_model(api_key)
    
    if model_id:
        st.sidebar.success(f"✅ 大腦連接成功：{model_info}")
        model = genai.GenerativeModel(model_id)
    else:
        st.error(f"❌ 大腦連接失敗：{model_info}")
        st.stop()
else:
    st.error("❌ 找不到 API Key。請在 Streamlit Secrets 中設定 GEMINI_API_KEY")
    st.stop()

# 3. 主界面
video_url = st.text_input("請貼上影片網址 (IG / 抖音 / 小紅書)：", placeholder="在此輸入連結...")

if st.button("開啟深度診斷"):
    if not video_url:
        st.warning("⚠️ 請貼入影片網址！")
    else:
        # 你的九年心法指令
        prompt = f"""
        你現在是擁有九年經驗的短影音專家『綸綸老師』。
        請針對這部影片進行深度戰略拆解：{video_url}
        
        請嚴格遵守以下格式產出報告（使用 Markdown 格式）：
        ### 📊 綸綸老師專業診斷報告
        
        #### 1. 【0-3s Hook 開場分析】
        分析視覺與標題是否具備止住滑動的『衝突感』。
        
        #### 2. 【4-45s 中段結構拆解】
        分析信息密度、視覺節奏是否能觸發『收藏與重複觀看』。
        
        #### 3. 【45-60s 尾部轉化建議】
        分析其 CTA 是否精準，是否能建立信任並導流。
        
        #### 4. 【爆款標題改寫】
        給出 3 組更有攻擊力的『懲罰式反差標題』。
        
        語氣要求：專業、犀利、直接點出病灶，說話要像一位資深戰略總監。
        """
        
        with st.spinner("🧠 正在讀取九年心法，大腦運算中..."):
            try:
                response = model.generate_content(prompt)
                st.markdown("<div class='report-box'>", unsafe_allow_html=True)
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"分析時發生錯誤：{e}")
