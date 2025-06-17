# 📚 Automated Book Publication Workflow

This project automates the process of transforming web-based book chapters into AI-enhanced publish-ready content. It features AI rewriting, review, human-in-the-loop editing, versioning with ChromaDB, and simulated RL-based intelligent search.

---

## 🚀 Features

- 🌐 **Web Scraping & Screenshots**  
  Scrapes chapters from [Wikisource](https://en.wikisource.org) and captures screenshots.

- ✍️ **AI Writer & Reviewer**  
  Uses Gemini (or OpenAI-compatible) API to spin and refine content.

- 🧑‍🏫 **Human-in-the-Loop Editing**  
  Enables manual review before final versioning.

- 🗂️ **Versioning**  
  Stores finalized chapters using ChromaDB with metadata.

- 🧠 **RL-based Search**  
  Retrieves versions based on simulated reinforcement learning ranking.

---

## 🛠️ Tech Stack

- **Python**: Core programming language
- **Playwright**: For web scraping and screenshots
- **Gemini API**: For AI writing and reviewing
- **ChromaDB**: For versioned vector storage
- **RL Algorithm**: Simulated ranking logic
- **FastAPI (optional)**: Could be added for future API interface

---

## 🔐 Setup Instructions

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   playwright install
   ```
---

## 2. Set up your API key:

GEMINI_API_KEY=your_google_gemini_api_key_here

---

## 3.Run the Project:

python main.py

---

## 📁 Project Structure

```
automated_book_workflow/
├── agents/
│   ├── writer_agent.py
│   ├── reviewer_agent.py
│   └── editor_agent.py
├── scraping/
│   ├── scraper.py
│   └── screenshot.py
├── versioning/
│   └── chromadb_store.py
├── retrieval/
│   └── rl_search.py
├── .env
├── .gitignore
├── main.py
└── README.md
```
---

## 📝 Notes
This project is built for evaluation purposes only.

It demonstrates AI-driven content processing in a reproducible pipeline.

API keys and screenshots are excluded via .gitignore.

---

## 👨‍💻 Author
**Umesh Raju**
[GitHub](https://github.com/UmeshRaju) 
[LinkedIn](www.linkedin.com/in/kondiumeshraju)

