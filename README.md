# 🚀 DeepSeek AI Chatbot & Document Assistant

Welcome to **DeepSeek AI Chatbot & Document Assistant**! 🧠✨ This project brings together cutting-edge **Retrieval-Augmented Generation (RAG)** with **LangChain** and **DeepSeek models** to create two powerful tools:

1. **DeepSeek Code Companion** 🐍💻 – An AI-powered pair programmer that helps debug, document, and enhance your code.
2. **DocuMind AI** 📘🤖 – A smart document assistant that understands and retrieves answers from uploaded PDFs.

Built with **LM Studio** for running DeepSeek locally, **Streamlit** for an interactive UI, and **LangChain** for seamless integrations.

---

## ✨ Features

- **DeepSeek Code Companion** 🔥
  - 💡 AI-powered coding assistant
  - 🐞 Debugging & troubleshooting
  - 📝 Code documentation and solution design
  - 🚀 Built with **LM Studio** to run DeepSeek locally

- **DocuMind AI** 📚
  - 📄 Upload research documents (PDF)
  - 🔍 Perform semantic search using **Vector Stores**
  - 🧠 Retrieve context-aware answers
  - ⚡ Uses Hugging Face embeddings for efficient retrieval

---

## 🛠️ Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/deepseek-chatbot.git
cd deepseek-chatbot
```

### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Alternatively, install dependencies manually:
```bash
pip install -r pyproject.toml
```

---

## 🚀 Running the Applications

### 🧠 Run **DeepSeek Code Companion**
```bash
streamlit run deepseek_app.py
```
💻 Visit: `http://localhost:8501`

---

### 📘 Run **DocuMind AI (Document Assistant)**
```bash
streamlit run deepseek_document_assistant.py
```
📜 Upload PDFs and start querying!

---

## 🔧 Configuration

- The app is configured in `config.py`:
  - **Embedding Model**: `all-MiniLM-L6-v2`
  - **Vector Database**: `InMemoryVectorStore`
  - **Language Model**: `deepseek-r1-distill-qwen-7b`
  - **Custom Prompt Template**

- Uses **LM Studio** to deploy **DeepSeek** locally:
  - Make sure **LM Studio** is running on `http://localhost:1234`
  - Modify `deepseek_utils.py` if necessary

---

## 🎯 How It Works

### 🧩 DeepSeek Code Companion
1. The user types a query (e.g., "How do I fix this Python bug?")
2. The AI retrieves past interactions & builds a relevant response
3. The answer is generated using the locally deployed **DeepSeek model**
4. The chat history is maintained for context-aware responses

### 📜 DocuMind AI (Document Assistant)
1. User uploads a **PDF document**
2. The system **loads & processes** the document
3. The document is **chunked** and stored in a **Vector Database**
4. User asks a question → **Relevant document sections** are retrieved
5. AI **generates a concise answer** using the retrieved context

---

## 🎯 Technologies Used

- 🏗 **LangChain** - Orchestrates retrieval and response generation
- 💾 **Vector Stores** - Enables semantic search on documents
- 🤗 **Hugging Face Embeddings** - Efficient text representation
- ⚡ **Streamlit** - Interactive UI for chat & document search
- 🔥 **LM Studio** - Runs **DeepSeek AI** models locally

---

## 🌍 Contributing

1. Fork the repo 🍴
2. Create a new branch (`feature-xyz`)
3. Make changes and commit (`git commit -m "Added cool feature 🚀"`)
4. Push to your branch (`git push origin feature-xyz`)
5. Open a **Pull Request**

---

## 🚀 Future Enhancements

- 🏗 **Persistent Vector Storage (e.g., ChromaDB)**
- 🛠 **Custom DeepSeek model fine-tuning**
- 📂 **Multi-document support in DocuMind AI**
- 🌍 **Support for multiple languages**

---

## 🤝 Acknowledgments

Big thanks to:
- **LangChain** for making AI integrations seamless
- **DeepSeek AI** for powerful local LLMs
- **Streamlit** for the sleek and interactive UI
- **LM Studio** for running models offline 🚀

---

## 💡 Have Fun!

Enjoy using **DeepSeek AI Chatbot & Document Assistant**! 🤖✨ If you have any questions, **open an issue** or reach out. 🚀 Happy coding!
