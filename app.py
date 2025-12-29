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
    .report-box { background: #1a1c23; padding: 25px; border-radius: 15px; border-left: 5px solid #00f3ff; line-height: 1.8; }
    </style>
""", unsafe_allow_html=True)

st.title("🚀 綸綸老師專業AI：短影音成功導航儀")
st.write("<p style='text-align: center; color: #888;'>全市場最強分析師：9年實戰戰略驅動</p>", unsafe_allow_html=True)

# 2. 自動從保險箱讀取 API Key
try:
    api_key = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-pro')
except Exception as e:
    st.error("❌ 保險箱設定錯誤，請檢查 Streamlit Secrets 設定。")
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
        
        請嚴格遵守以下格式產出報告：
        1. 【0-3s Hook 開場】：分析視覺與標題是否具備止住滑動的『衝突感』。
        2. 【4-45s 中段結構】：分析信息密度、視覺節奏是否能觸發『收藏與重複觀看』。
        3. 【45-60s 尾部轉化】：分析其 CTA 是否精準，是否能建立信任並導流。
        4. 【綸綸老師專業建議】：給出 3 組更有攻擊力的『懲罰式反差標題』。
        
        語氣：專業、犀利、充滿實戰高度。
        """
        
        with st.spinner("🧠 正在對照九年心法，大腦運算中..."):
            try:
                response = model.generate_content(prompt)
                st.markdown("<div class='report-box'>", unsafe_allow_html=True)
                st.subheader("📊 專業診斷報告")
                st.markdown(response.text)
                st.markdown("</div>", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"分析出錯了：{e}")
