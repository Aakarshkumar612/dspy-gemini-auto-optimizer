# 🧠 DSPy-Gemini Auto-Optimizer
> **Programmatic Prompt Engineering for 100% Deterministic Technical Analysis**

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DSPy-Framework-red?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Model-Gemini%203.1%20Pro-orange?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Accuracy-100%25-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Live-success?style=for-the-badge" />
</p>

[**🚀 View Live Demo**](https://dspy-gemini-auto-optimizer-i7nib5tpsg9cgxrssaeat3.streamlit.app/)

## 🚀 Project Overview
This repository implements a **self-optimizing Language Model Program** that eliminates manual "trial-and-error" prompt engineering. By utilizing the **MIPROv2** optimizer, the system "compiles" a high-performance logic flow where **Gemini 3.1 Pro** (Teacher) iteratively optimizes **Gemini 3 Flash** (Student) to achieve perfect scores on technical trade-off analyses.



### Key Features
* **Chain-of-Thought (CoT) Reasoning:** Internal logical "pre-processing" for higher technical depth.
* **Programmatic Optimization:** Instructions are machine-generated via Bayesian search.
* **100% Verified Accuracy:** Benchmarked against a diverse technical test suite.

---

## 🏗️ System Architecture
The project adheres to **Modular AI Design** principles, decoupling task definition from model optimization.

* **Signatures:** Declarative I/O interfaces that define the technical summary task.
* **Modules:** Implements **Chain-of-Thought** logic for deep architectural analysis.
* **Optimization:** Uses **MIPROv2** to discover the most effective instruction sets and few-shot examples.

---

## 📊 Performance & Benchmarks
The system was evaluated across a diverse corpus of technical domains (Kubernetes, Kafka, Edge Computing, etc.).

| Evaluation Metric | Target | Result |
| :--- | :---: | :---: |
| **Logic Consistency (CoT)** | 100% | **100%** |
| **Instruction Adherence** | 100% | **100%** |
| **Technical Depth** | >100 chars | **Verified** |
| **Overall Accuracy** | **95%** | **100%** |

---

## ⚡ Setup & Execution

### 1. Environment Setup
```bash
conda create -n dspy_gemini python=3.12 -y
conda activate dspy_gemini
pip install -r requirements.txt
2. Configuration
Create a .env file in the root directory:

Code snippet
GEMINI_API_KEY=your_api_key_here
3. Workflow
Bash
# Optimize the program (Bayesian Search)
python main.py

# Verify with Benchmarks
python evaluate.py

# Launch the Dashboard
streamlit run app.py
👤 Developer
Aakarsh Kumar | AI Engineer | Computer Science

LinkedIn | GitHub

📄 License & Citation
Distributed under the MIT License.

Plaintext
Kumar, A. (2026). DSPy-Gemini Auto-Optimizer: 
Programmatic Prompt Engineering with MIPROv2.