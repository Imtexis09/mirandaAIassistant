# 🤖 Miranda AI Assistant

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean_Architecture-success.svg)
![Status](https://img.shields.io/badge/Status-In_Development_(Phase_1)-orange.svg)

**Miranda** is a modular, cross-platform, and highly scalable AI assistant designed for personal, academic, and professional productivity. Inspired by advanced systems like Jarvis, Miranda is engineered to process natural language, manage short-term and long-term memory, and execute automation tasks directly at the operating system level.

The codebase is built under strict software engineering standards, fully adhering to **SOLID principles**, **Clean Architecture**, and **Dependency Injection**. This architectural choice ensures the system can seamlessly scale to over 100 domain modules in the future without compromising its core engine.

---

## 🏗️ Project Status: Current Milestone

The project is currently in **Phase 1: Foundations & Core Architecture**. 
The underlying system skeleton has been successfully established to guarantee absolute structural robustness before integrating advanced cognitive capabilities.

**Current Achievements:**
- [x] Production-ready Clean Architecture design (Core Layer, Adapters, and Use Cases).
- [x] Strict virtual environment orchestration and explicit dependency isolation (`requirements.txt`).
- [x] Interface-driven design (Contracts) enabling clean Dependency Injection.
- [x] Secure configuration handling using system environment variables and `Pydantic`.
- [x] Centralized asynchronous Logging system.
- [x] Basic Continuous Integration (CI) pipeline powered by GitHub Actions and Pytest.
- [x] Foundational support for dynamic context-switching between Cloud LLMs (OpenAI) and Local Models (Ollama).

---

## 🚀 Roadmap: Future Horizons

The development toward a fully functional Beta version is divided into the following sequential phases:

### Phase 2: Brain & Memory (Next Milestone)
- SQLite implementation utilizing SQLAlchemy ORM.
- Development of Short-Term Memory (handling the immediate conversation context).
- Development of Long-Term Memory (user profile preferences and knowledge indexing leveraging RAG with LlamaIndex).

### Phase 3: Senses & Actions
- **Hearing (STT):** Whisper integration combined with localized Wake Word detection ("Hola Miranda").
- **Voice (TTS):** High-speed, low-latency speech synthesis using Piper/Coqui TTS.
- **Hands (OS Automation):** Secure OS-level command execution, application management, and automated web scraping/navigation via Selenium/Playwright.

### Phase 4: User Interface
- Engineering a sleek, modern, minimalist, and fully asynchronous GUI utilizing **PySide6**.
- Implementation of worker threads (`QThreads`) to offload heavy AI processing inference and guarantee a non-blocking UI experience.

### Phase 5+: Expansion (Post-Beta)
- Third-party API integrations (WhatsApp, Discord, GitHub webhooks).
- Computer Vision capabilities.
- Autonomous multi-agent systems for complex problem-solving.
- Cross-platform mobile deployment compilation (Android/iOS).

---

## 🛠️ Tech Stack

* **Language:** Python 3.12
* **Core Frameworks:** FastAPI, PySide6, Pydantic
* **AI & Intelligence:** OpenAI API, Ollama (Local LLM Execution), LangChain, LlamaIndex
* **Automation:** PyAutoGUI, Selenium
* **Database:** SQLite (Beta phase) -> PostgreSQL (Enterprise production scaling)
* **Testing Suite:** Pytest

---

## ⚙️ Installation & Usage (Development Mode)

### 1. Clone the Repository
```bash
git clone [https://github.com/Imtexis09/miranda-ai.git](https://github.com/Imtexis09/miranda-ai.git)
cd miranda-ai
```

### 2. Initialize and Activate the Virtual Environment
```bash
python -m venv venv
```
#### On Windows:
```bash
venv\Scripts\activate
```
#### On Linux/macOS:
```bash
source venv/bin/activate
```

### 3. Install Project Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Configuration
Create a `.env` file in the root directory of the project based on the configuration template. Populate it with your respective API Keys (Note: The `.env` file is heavily restricted via `.gitignore` for security compliance).

### 5. Execute Test Suites
```bash
pytest tests/
```

---

## 👨‍💻 Author

**Alexis Texis**
*Computer Science Engineering Student at Benemérita Universidad Autónoma de Puebla (BUAP).*
Passionate about software architecture, clean system design, and cutting-edge artificial intelligence.

*This project is open-source, originally conceptualized as an all-in-one assistant to accelerate academic research and professional workflows.*
   
