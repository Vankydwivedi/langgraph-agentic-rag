<h2 align="center">🧠 LangGraph Agentic AI News Generator</h2>

<p align="center">
An agentic AI system built using LangGraph and Groq LLMs that autonomously researches, processes, and generates high-quality news content from user input.
</p>

---

## 🚀 Overview

This project demonstrates an **Agentic AI system** where multiple intelligent components work together using a state-based graph architecture to:

✅ Accept user-provided topics  
✅ Retrieve and reason about information  
✅ Generate structured, high-quality news articles  
✅ Run using ultra-fast inference via Groq LLMs  
✅ Provide an interactive Streamlit interface  

The system is designed to be **scalable, modular, and production-ready**.

---

## ✨ Features

- ✅ LangGraph-based agent workflow  
- ✅ Groq LLM integration for fast inference  
- ✅ Agent-based decision routing  
- ✅ Streamlit UI  
- ✅ Hugging Face Spaces deployment  
- ✅ Environment-based secret management  
- ✅ Clean modular architecture  

---

## 🏗️ Architecture

User Input
↓
Streamlit UI
↓
LangGraph Orchestrator
↓
Agent Nodes (Reasoning, Tools, Chat)
↓
Groq LLM
↓
Final Generated News Output

yaml
Copy code

---

## 📁 Project Structure

src/
│
├── langgraphagenticai/
│ ├── LLMs/
│ │ └── groqllm.py
│ │
│ ├── nodes/
│ │ ├── ai_news_node.py
│ │ ├── basic_chatbot_node.py
│ │ └── chatbot_with_tool_node.py
│ │
│ ├── state/
│ │
│ ├── tools/
│
├── ui/
│ ├── streamlitui/
│ │ ├── display_result.py
│ │ ├── loadui.py
│
├── main.py # LangGraph entry
├── app.py # Streamlit entry
├── uiconfig.ini # UI configuration
├── requirements.txt # Dependencies

yaml
Copy code

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Vankydwivedi/langgraph-agentic-rag.git
cd langgraph-agentic-rag
2️⃣ Create a virtual environment
bash
Copy code
python -m venv venv
Activate:

Windows

bash
Copy code
venv\Scripts\activate
Mac / Linux

bash
Copy code
source venv/bin/activate
3️⃣ Install dependencies
bash
Copy code
pip install -r requirements.txt
🔐 Environment Variables
Create a .env file (or add secrets on Hugging Face):

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
▶️ Run Locally
bash
Copy code
streamlit run app.py
Open in browser:

arduino
Copy code
http://localhost:8501
🌍 Deployment (Hugging Face Spaces)
Create Space → Streamlit app

Connect GitHub repo

Add secret:

env
Copy code
GROQ_API_KEY=your_groq_api_key_here
Deploy ✅

🛠 Tech Stack
Layer	Technology
UI	Streamlit
LLM	Groq
Orchestration	LangGraph
Language	Python
Deployment	Hugging Face Spaces

🔮 Future Enhancements
Multi-agent collaboration

Live web data ingestion

News summarization mode

Category classification

Memory persistence

