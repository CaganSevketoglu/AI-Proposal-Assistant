# 🤖 AI-Powered Upwork Proposal Assistant

This is an interactive web application built with Streamlit and powered by OpenAI's GPT models. It acts as a personal career coach, providing a strategic analysis of Upwork job postings to help freelancers save time and make smarter decisions.

---

## 🚀 Live Demo

**You can try the live application here: https://ai-proposal-assistant-9uvgqytihoacnchfaipps5.streamlit.app/
---

## 📸 Application Preview


![App Screenshot](https://github.com/CaganSevketoglu/AI-Proposal-Assistant/blob/main/Ekran%20Resmi%202025-06-22%2014.10.15.jpg?raw=true) 
*(Not: Bu satırı şimdilik bıraktım, GitHub'a yüklediğin bir ekran görüntüsünün linki ile değiştirebilirsin.)*


---

## Core Features

This tool analyzes a job post and provides a structured report based on key strategic criteria:

-   **📊 Skill Fit Analysis:** Rates how well the job requirements match your specific skills and portfolio projects (score out of 10).
-   **💰 Budget Quality Assessment:** Evaluates if the client's budget is appropriate for the scope and complexity of the work.
-   **🚩 Red Flag Detection:** Automatically identifies potentially problematic words or phrases in a job post (e.g., "urgent," vague scope).
-   **⭐ Final Recommendation:** Gives a clear, justified "Go for it!" or "Stay Away!" verdict to guide your application decision.

---

## Tech Stack

-   **Language:** Python
-   **Web Framework:** Streamlit
-   **AI/LLM:** OpenAI API (GPT-4o-mini)
-   **Core Libraries:** Pandas

---

## How to Run Locally

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/CaganSevketoglu/AI-Proposal-Assistant.git](https://github.com/CaganSevketoglu/AI-Proposal-Assistant.git)
    cd AI-Proposal-Assistant
    ```

2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Create Your Secrets File:**
    -   In the project's root directory, create a folder named `.streamlit`.
    -   Inside the `.streamlit` folder, create a file named `secrets.toml`.
    -   Add your OpenAI API key to the `secrets.toml` file:
        ```toml
        OPENAI_API_KEY = "sk-..."
        ```

4.  **Run the App:**
    ```bash
    streamlit run assistant_app.py
    ```
