# 🤖 Miranda AI Assistant

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Architecture](https://img.shields.io/badge/Architecture-Clean_Architecture-success.svg)
![Status](https://img.shields.io/badge/Status-En_Desarrollo_(Fase_1)-orange.svg)

**Miranda** es un asistente de inteligencia artificial modular, multiplataforma y escalable, diseñado para uso personal, académico y profesional. Inspirado en asistentes avanzados como Jarvis, Miranda es capaz de procesar lenguaje natural, gestionar memoria a corto y largo plazo, y ejecutar automatizaciones directamente en el sistema operativo.

El proyecto está diseñado bajo estrictos estándares de ingeniería de software, aplicando **principios SOLID**, **Clean Architecture** e **Inyección de Dependencias**, lo que permite escalar el sistema a más de 100 módulos en el futuro sin comprometer su núcleo.

---

## 🏗️ Estado Actual del Proyecto: ¿Qué estamos haciendo?

Actualmente, el proyecto se encuentra en la **Fase 1: Cimientos y Arquitectura Base**. 
Se ha establecido el "esqueleto" del sistema para asegurar que sea robusto antes de integrar capacidades avanzadas.

**Logros actuales:**
- [x] Diseño de Clean Architecture (Capa Core, Adaptadores, Casos de Uso).
- [x] Configuración del entorno virtual y dependencias estrictas (`requirements.txt`).
- [x] Implementación de interfaces (Contratos) para Inyección de Dependencias.
- [x] Sistema de configuración segura mediante variables de entorno y `Pydantic`.
- [x] Sistema de Logging centralizado.
- [x] Integración Continua (CI) básica con GitHub Actions y Pytest.
- [x] Soporte base para el cambio de contexto entre Modelos Cloud (OpenAI) y Locales (Ollama).

---

## 🚀 Roadmap: ¿Qué se hará a futuro?

El desarrollo de la versión Beta funcional está dividido en las siguientes fases:

### Fase 2: Cerebro y Memoria (Próximo paso)
- Integración de SQLite mediante SQLAlchemy.
- Desarrollo de Memoria a Corto Plazo (Contexto de conversación actual).
- Desarrollo de Memoria a Largo Plazo (Almacenamiento de preferencias y datos del usuario usando RAG con LlamaIndex).

### Fase 3: Sentidos y Acciones
- **Oído (STT):** Integración de Whisper y detección de Wake Word ("Hola Miranda").
- **Voz (TTS):** Síntesis de voz rápida usando Piper/Coqui TTS.
- **Manos (Automatización):** Ejecución segura de comandos en el SO, apertura de aplicaciones y navegación web básica con Selenium/Playwright.

### Fase 4: Interfaz de Usuario
- Creación de una GUI moderna, minimalista y asíncrona utilizando **PySide6**.
- Integración de hilos (QThreads) para evitar que la interfaz se congele durante el procesamiento de la IA.

### Fase 5+: Expansión (Post-Beta)
- Integración con APIs de terceros (WhatsApp, Discord, GitHub).
- Soporte para Visión por Computadora.
- Agentes autónomos para resolución de problemas complejos.
- Despliegue en dispositivos móviles (Android/iOS).

---

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.12
* **Frameworks/Librerías Core:** FastAPI, PySide6, Pydantic
* **IA y Modelos:** OpenAI API, Ollama (Modelos Locales), LangChain, LlamaIndex
* **Automatización:** PyAutoGUI, Selenium
* **Base de Datos:** SQLite (Fase Beta) -> PostgreSQL (Fase Avanzada)
* **Testing:** Pytest

---

## ⚙️ Instalación y Uso (Modo Desarrollo)

1. **Clonar el repositorio:**
   `git clone [https://github.com/TuUsuario/miranda-ai.git](https://github.com/TuUsuario/miranda-ai.git)
   cd miranda-ai`
2. **Crear y activar el entorno virtual:**

`python -m venv venv`
#### En Windows:
`venv\Scripts\activate`
#### En Linux/macOS:
`source venv/bin/activate`

3. **Instalar dependencias:**

`pip install -r requirements.txt`

4. **Configurar el entorno:**

Crea un archivo .env en la raíz del proyecto basándote en el archivo de configuración. Añade tus API Keys (Nota: El archivo `.env` está en el `.gitignore` por seguridad).

5. **Ejecutar pruebas:**
`pytest tests/`

---

## 👨‍💻 Autor
Alexis Texis.

Estudiante de Ingeniería en Ciencias de la Computación en la Benemérita Universidad Autónoma de Puebla (BUAP).
Apasionado por el desarrollo de software, la arquitectura de sistemas y la inteligencia artificial.

Este proyecto es de código abierto, diseñado originalmente como una herramienta integral de apoyo académico y profesional.
   
   
   
