# 🎓 StudyMate AI

**An AI-Powered Learning Assistant**

StudyMate AI is an AI-powered learning assistant built using Python and Streamlit. It aims to make studying easier, smarter, and more efficient through Generative AI.

## 🚀 Features

- **Note Summarizer:** Convert lengthy study materials into concise summaries.
- **AI Quiz Generator:** Generate quizzes from study materials to practice and test knowledge.
- **Concept Explainer:** Understand complex topics through simple AI-generated explanations.

## 🛠️ Tech Stack

- Python
- Streamlit
- OpenAI API
- Generative AI

## 📁 Project Structure

```text
StudyMate-AI/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the project folder

```bash
cd StudyMate-AI
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**
```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure the API key

Create a `.env` file using `.env.example` as a template.

Add your OpenAI API credentials:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_MODEL=gpt-5.5
```

**Note:** A valid OpenAI API key is required to use the AI-powered features.

### 7. Run the application

```bash
streamlit run app.py
```

## 🔐 Security

- Never upload your actual `.env` file.
- Never share your OpenAI API key publicly.
- Use `.gitignore` to exclude sensitive files.

## 🎯 Project Goal

The goal of StudyMate AI is to make learning more accessible and effective by using Artificial Intelligence to simplify study materials, encourage practice, and improve conceptual understanding.

## 👨‍💻 Author

Developed as an AI learning project.

---

⭐ If you find this project interesting, consider giving the repository a star!