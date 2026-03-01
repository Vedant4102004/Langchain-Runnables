Markdown
# 🦜 Mastering LangChain: Open Source LCEL & Runnables

This repository is a comprehensive engineering suite for building modular AI workflows using **LangChain Expression Language (LCEL)**. Unlike standard tutorials, this project is built for **Open Source LLMs** (Llama 3, Mistral, etc.), focusing on local inference and high-performance data orchestration.

---

## 🏗️ The Four Pillars of Runnables

This project provides deep-dive implementations of the core LangChain primitives. Each one is designed to handle a specific part of the LLM lifecycle.

### 1. 🔗 RunnableSequence
The "Pipe" operator (`|`). It chains components where the output of the prompt feeds the LLM, and the LLM output feeds the parser.
* **Pattern:** `Input -> Prompt -> Local LLM -> OutputParser`

### 2. 🔀 RunnableParallel
Allows for **concurrent execution**. It is essential for RAG pipelines where you need to fetch context from a vector store while simultaneously passing the user's original question.
* **Pattern:** `{ "context": retriever, "question": RunnablePassthrough() }`

### 3. 🛡️ RunnablePassthrough
A utility to forward data unchanged. It ensures that variables (like metadata or history) are preserved throughout the chain without being lost during transformations.

### 4. 🚦 RunnableBranch
The routing engine. It acts as an "If-Else" statement, allowing the chain to dynamically choose a path based on the user's input.
* **Use Case:** Routing "Coding" questions to a Code-Llama model and "General" queries to a Mistral model.



---

## 🛠️ Complete Setup & Installation

Follow these steps to get the environment running locally with Open Source models.

### 1. Clone & Environment
```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
2. Install All Dependencies
Bash
pip install langchain langchain-community langchain-core langchain-ollama
3. Local LLM Setup (Ollama)
We use Ollama for local inference to keep data private and costs at zero.

Download Ollama from ollama.com.

Pull your preferred models:

Bash
ollama pull llama3
ollama pull mistral
📂 Project Structure
/sequence: Linear chains and basic piping.

/parallel: Multi-tasking and dictionary mapping.

/passthrough: State management and data forwarding.

/branch: Conditional routing and decision-making logic.

.gitignore: Pre-configured to keep your environment clean.

🚀 Quick Code Example (Parallel + Passthrough)
Python
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from langchain_ollama import OllamaLLM

model = OllamaLLM(model="llama3")
chain = RunnableParallel(
    original_input=RunnablePassthrough(),
    transformation=model
)

# This runs both the model and the passthrough at the same time!
result = chain.invoke("Explain Quantum Physics in one sentence.")
print(result)
💡 Key Features
Local-First: No API keys required; runs entirely on your hardware.

Async Ready: All chains support .ainvoke() and .astream().

Streaming: Real-time token generation is enabled by default.

Developed for the Open Source AI Community.
