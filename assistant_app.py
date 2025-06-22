import streamlit as st
import openai
import re # Metin işleme için bu kütüphaneyi ekliyoruz
openai.api_key = st.secrets["OPENAI_API_KEY"]

# --- Sayfa Konfigürasyonu ---
st.set_page_config(
    page_title="AI Proposal Assistant",
    page_icon="🤖",
    layout="wide"
)

# --- API Anahtarı Kurulumu ---
st.sidebar.header("Configuration")


# --- Ana Uygulama Arayüzü ---
st.title("🤖 AI Upwork Proposal Assistant")
st.write("This tool provides a strategic analysis of an Upwork job post based on your specific profile and portfolio.")

user_skills = st.text_input("Enter your core skills (comma-separated):", "Python, Pandas, Scikit-learn, Classification, FastAPI")

job_post_text = st.text_area("Paste the full job description here:", height=250)

# --- Yapay Zeka Beyni (Fonksiyon Olarak) ---
def get_ai_analysis(job_post: str, skills: str):
    system_prompt = "You are an expert freelance career coach for AI engineers. Your job is to analyze Upwork job posts based on a predefined checklist and provide a strategic recommendation in a structured format."
    user_prompt = f"""
    Analyze the job post below for my profile. My core skills are: {skills}. My main portfolio project is a Customer Churn Prediction model.

    Job Post to Analyze:
    ---
    {job_post}
    ---

    Provide your analysis in this format, using markdown for bolding:
    **1. Skill Fit (1-10):** [Score here] - [Brief justification]
    **2. Budget Quality (1-10):** [Score here] - [Brief justification]
    **3. Red Flags:** [List any red flags here, or write 'None' if there are none]
    **4. Final Recommendation:** [Go for it! / Stay Away!] - [One-sentence justification]
    """
    
    try:
        response = openai.chat.completions.create(
          model="gpt-4o-mini",
          messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
          ]
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"An API error occurred: {e}")
        return None

# --- Buton ve Çalıştırma Mantığı (NİHAİ VERSİYON) ---
if st.button("Analyze Job Post"):
    if not job_post_text:
        st.warning("Please paste a job description first.")
    else:
        with st.spinner("AI Assistant is analyzing the job post... Please wait."):
            analysis_result = get_ai_analysis(job_post_text, user_skills)
            if analysis_result:
                st.subheader("--- AI Analysis Result ---")

                # --- YENİ VE EN SAĞLAM PARÇALAMA MANTIĞI ---
                try:
                    # Cevabı bölümlere ayırmak için anahtar başlıkları kullanıyoruz
                    skill_fit_part = analysis_result.split("1. Skill Fit")[1].split("2. Budget Quality")[0]
                    budget_part = analysis_result.split("2. Budget Quality")[1].split("3. Red Flags")[0]
                    flags_part = analysis_result.split("3. Red Flags")[1].split("4. Final Recommendation")[0]
                    rec_part = analysis_result.split("4. Final Recommendation")[1]

                    # Her bölümden skoru ve metni ayıralım
                    skill_score = skill_fit_part.split("(1-10):**")[1].split("-")[0].strip().replace('*','')
                    skill_details = skill_fit_part.split("-", 1)[1].strip()

                    budget_score = budget_part.split("(1-10):**")[1].split("-")[0].strip().replace('*','')
                    budget_details = budget_part.split("-", 1)[1].strip()

                    red_flags = flags_part.split(":**")[1].strip()
                    recommendation = rec_part.split(":**")[1].strip()
                    
                    # Kolonlar oluşturalım
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Skill Fit Score", skill_score)
                    with col2:
                        st.metric("Budget Quality Score", budget_score)

                    # Tavsiyeyi renkli kutuda gösterelim
                    if "Go for it!" in recommendation:
                        st.success(f"**Recommendation:** {recommendation}")
                    else:
                        st.error(f"**Recommendation:** {recommendation}")

                    # Kalan detayları bir expander içine koyalım
                    with st.expander("See Detailed Analysis"):
                        st.markdown(f"**Skill Fit Details:**\n{skill_details}")
                        st.markdown(f"**Budget Quality Details:**\n{budget_details}")
                        st.markdown(f"**Red Flags:**\n{red_flags}")
                
                except Exception as e:
                    # Eğer format yine de bozuk gelirse, tamamını normal şekilde yazdır
                    st.warning("Could not parse the AI's formatted response. Displaying raw text:")
                    st.markdown(analysis_result)