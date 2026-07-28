# Dynamic_AI_Chatbot
An intelligent AI-powered chatbot built with **Python**, **Flask**, and **Ollama (Llama 3.2)**. This chatbot combines **rule-based intent recognition** with **AI-generated responses**, allowing it to answer predefined questions instantly while generating intelligent responses for open-ended queries using a local Large Language Model (LLM).

> ⚡ No OpenAI API key required. Everything runs locally using Ollama.

---

## 📌 Project Overview

The Dynamic AI Chatbot is a hybrid chatbot that first checks whether the user's message matches any predefined intents stored in `intents.json`. If no matching intent is found, it forwards the conversation to the **Llama 3.2** model running locally with **Ollama** to generate an intelligent response.

The project includes:

- Flask Backend
- HTML/CSS/JavaScript Frontend
- Rule-Based Chatbot
- AI Chatbot using Ollama
- Conversation Memory
- Easy-to-extend Intent System

---

# 🚀 Features

- 🤖 AI-powered chatbot using Llama 3.2
- 💬 Dynamic conversation generation
- 📚 Predefined intent recognition
- 🧠 Conversation memory
- 🌐 Flask Web Application
- ⚡ Fast response generation
- 💻 Simple and clean user interface
- 🔧 Easy customization
- 🆓 Completely free (Runs locally)

---

# 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Flask | Web Framework |
| Ollama | Local AI Model |
| Llama 3.2 | Large Language Model |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Client-side Logic |
| JSON | Intent Storage |

---

# 📂 Project Structure

```
Dynamic_AI_Chatbot/
│
├── app.py
├── chatbot.py
├── intents.json
├── chatbot.db
├── AI_Chatbot.ipynb
├── requirements.txt
├── README.md
│
├── templates/
│     └── index.html
│
├── static/
│     ├── style.css
│     └── script.js
│
└── screenshots/
      ├── home.png
      └── chatbot.png
```

---

# ⚙️ How It Works

```
User
   │
   ▼
Web Interface
(HTML/CSS/JS)
   │
   ▼
Flask Backend
(app.py)
   │
   ▼
Check Intents
(intents.json)
   │
   ├──────────────► Match Found
   │                     │
   │                     ▼
   │             Return Response
   │
   ▼
No Match
   │
   ▼
Ollama
(Llama 3.2)
   │
   ▼
Generate AI Response
   │
   ▼
Display to User
```


# 💻 Installation

## 1. Clone Repository

```bash
git clone https://github.com/YourUsername/Dynamic_AI_Chatbot.git

cd Dynamic_AI_Chatbot
```

---

## 2. Create Virtual Environment (Optional)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama

https://ollama.com/download

---

## 5. Pull the Llama 3.2 Model

```bash
ollama pull llama3.2
```

---

## 6. Start Ollama

```bash
ollama serve
```

---

## 7. Run the Flask Application

```bash
python app.py
```

---

## 8. Open Browser

```
http://127.0.0.1:5000
```

---


## 🎯 Project Highlights

✔ Flask Web Application

✔ AI Chatbot using Ollama

✔ Llama 3.2 Integration

✔ Rule-Based Intent Recognition

✔ Dynamic AI Responses

✔ Local LLM (No API Cost)

✔ Interactive Chat Interface

✔ Easy to Customize

✔ Beginner-Friendly Project

✔ Open Source
