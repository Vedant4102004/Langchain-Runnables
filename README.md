LangChain LCEL & Runnable Patterns
This repository is a deep dive into LangChain Expression Language (LCEL) and the various Runnable primitives. It demonstrates how to build modular, readable, and efficient AI chains using the pipe (|) operator.

🧩 Core Concepts Covered
The project explores the following Runnable types and their specific roles in the LangChain ecosystem:

1. RunnableSequence
The backbone of LCEL. It allows you to pipe the output of one component directly into the next.

Pattern: Input -> Prompt -> LLM -> OutputParser

Syntax: chain = prompt | model | parser

2. RunnableParallel
Used to execute multiple tasks simultaneously. It’s perfect for preparing a dictionary of inputs where different keys require different processing.

Example: Fetching a document from a database while keeping the original question in a separate key.

3. RunnablePassthrough
A utility to pass data through a step unchanged or to add new keys to the data flow without losing the existing ones.

Example: {"context": retriever, "question": RunnablePassthrough()}

4. RunnableBranch
The "If-Else" of LangChain. It allows the chain to dynamically choose a path based on the input content.

Use Case: Routing a query to a specific specialized prompt (e.g., "Math" vs "General") based on a classification step.

🛠 Project Structure
Each folder contains a specific implementation of the LangChain primitives:

/sequence: Linear chains using the | operator.

/parallel: Multi-tasking chains for data preparation.

/passthrough: Examples of state management and data forwarding.

/branch: Conditional routing and decision-making logic.

🚀 Quick Start
Clone the Repo:

Bash
git clone https://github.com/Vedant4102004/Langchain-Runnables.git
cd Langchain-Runnables
Install Dependencies:

Bash
pip install langchain langchain-openai
Set Environment Variables:

Bash
export OPENAI_API_KEY='your-key-here'
Run an Example:
In this files we used open source LLM's


Bash
python sequence/basic_chain.py
💡 Why use Runnables?
Async Support: All Runnables come with built-in ainvoke and astream methods.

Batching: Easily process multiple inputs in parallel with batch.

Observability: Seamless integration with LangSmith for debugging complex flows.
