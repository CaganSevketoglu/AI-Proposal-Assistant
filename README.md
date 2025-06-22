# 🤖 AI-Powered Upwork Proposal Assistant

This is an interactive web application built with Streamlit and powered by OpenAI's GPT models. It provides a strategic analysis of Upwork job postings to help freelancers save time and make smarter decisions by automatically evaluating job descriptions against their unique skills and portfolio.

---

## 🚀 Live Demo

**You can try the live application here:** (This link will be added after we deploy to Streamlit Cloud)
*(Not: Bu linki, bir sonraki adımımız olan uygulamayı canlıya aldıktan sonra ekleyeceğiz.)*

---

## Features

- **Strategic Job Analysis:** Instead of just summarizing, the AI acts as a personal career coach, analyzing job posts based on key freelance success criteria.
- **Skill Fit Scoring:** Rates how well a job post matches a freelancer's predefined skill set.
- **Budget Quality Analysis:** Assesses if the budget is appropriate for the complexity of the task.
- **Red Flag Detection:** Automatically identifies potentially problematic words or phrases in a job post (e.g., "urgent," vague scope).
- **Personalized Recommendations:** Provides a clear "Go for it!" or "Stay Away!" recommendation with a justification based on the analysis.

---

## Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **AI/LLM:** OpenAI API (GPT-4o-mini)
- **Core Libraries:** Pandas

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
