# 🔧 Project Overview

## 1. Web Scraper (FAQ Extractor)

Using **Selenium** and **BeautifulSoup**, I created a scraper that:
- Visits [starzplay.com/en/faq](https://starzplay.com/en/faq)
- Extracts questions and answers from each FAQ tab
- Saves the data into:
  - `starzplay_faq.csv`
  - `starzplay_faq.txt`

**Technologies Used:**
- Python (Colab)
- Selenium (headless Chrome)
- BeautifulSoup
- Pandas

---

## 2. RAG Chatbot (Retrieval-Augmented Generation)

I implemented a **chatbot** that:
- Loads the `starzplay_faq.csv` from **Google Drive**
- Uses **SentenceTransformer** to create local embeddings
- Stores embeddings in **Pinecone Vector Database**
- On query, retrieves relevant answers and uses **OpenAI GPT-4.1-nano** to generate a helpful, focused response

**Tech Stack:**
- LangChain
- SentenceTransformers
- Pinecone
- OpenAI Chat API (via environment variable only — no hardcoded keys)
- Google Colab + Google Drive

---

## n8n Workflows

I also built automated workflows using [**n8n**](https://n8n.io/) to support and scale this system:

### Workflow 1: FAQ Knowledge Base Uploader
Automatically detects when a new FAQ file is uploaded to **Google Drive** and embeds it into **Pinecone Vector Store**.



[View the Workflow](#) *(https://khadija-17.app.n8n.cloud/workflow/45UZ0h9PVEd8pDDu)*

---

### Workflow 2: Chatbot Q&A Engine
Handles incoming user queries via chat, performs semantic search using OpenAI embeddings, retrieves matching answers from Pinecone, and responds via OpenAI chat model.



[View the Workflow](#) *(https://khadija-17.app.n8n.cloud/workflow/zJNuokUjgYB97k3b)*

---

## Files

- `faq_scraper.py` – Colab-compatible scraper code for collecting FAQ data
- `rag_chatbot.py` – Colab-compatible chatbot with embedded FAQ knowledge
- `starzplay_faq.csv` – Output file from the scraper containing structured Q&A
- `starzplay_faq.txt` – Text-based version for readability

---
