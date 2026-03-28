# Agentic AI Learning Repository 🤖

Welcome to my personal learning workspace! I created this repository to dive deep into **LangChain** and **LangGraph**, getting hands-on experience with building and orchestrating LLM-powered applications and agents.

## 🎯 Purpose
This project is entirely dedicated to my learning journey. It contains a series of Jupyter notebooks and scripts where I experiment with core concepts, build progressively complex AI workflows, and get familiar with modern agentic architectures.

## 📂 Repository Structure

### Notebooks
The `notebooks/` directory contains my progressive experiments and learning materials:
- `1-langchain_basics.ipynb`: Fundamentals and initial setup using Langchain.
- `2-langchain_tools.ipynb`: Exploring tool calling and giving LLMs external capabilities.
- `3-Multi_tool_ReAct.ipynb`: Building ReAct (Reasoning and Acting) agents with multiple tools.
- `4-messages.ipynb`: Managing conversational state, message histories, and role prompting.
- `5-StructuredOutput.ipynb`: Enforcing structured data output form LLMs.
- `6-Short_term_memory.ipynb`: Implementing memory mechanisms to retain conversation context.
- `7-Middleware.ipynb`: Experimenting with agent middleware, routing, and advanced flows.

### Environment Management
- `pyproject.toml` & `uv.lock`: Modern Python dependency management.
- `requirements.txt`: Fallback standard dependency list.
- `.env`: (Ignored) Environment variables for API keys (e.g., Groq, OpenAI, etc).

## 🚀 Getting Started

To run these notebooks locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Shivansh-Raj/Agentic_AI.git
   cd Agentic_AI
   ```
2. **Setup virtual environment:**
   Use your preferred tool (e.g., `uv`, `venv`, `conda`) to install dependencies from `requirements.txt` or `pyproject.toml`.
3. **Configure API Keys:**
   Create a `.env` file in the root directory and add your necessary API keys (such as `GROQ_API_KEY`).
4. **Fire up Jupyter:**
   ```bash
   jupyter notebook
   ```

---
*Created by [Shivansh-Raj](https://github.com/Shivansh-Raj) as a playground for LangChain and LangGraph mastery!*
