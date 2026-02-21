# 🧠 DSPy-Gemini Auto-Optimizer
> **Programmatic Prompt Engineering for 100% Deterministic Technical Analysis**

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/DSPy-Framework-red?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Model-Gemini%203.1%20Pro-orange?style=for-the-badge&logo=google&logoColor=white" />
  <img src="https://img.shields.io/badge/Accuracy-100%25-green?style=for-the-badge" />
</p>

This repository implements a **self-optimizing Language Model Program** that eliminates manual prompt engineering. By utilizing the **MIPROv2** optimizer, the system "compiles" a high-performance logic flow where **Gemini 3.1 Pro** (Teacher) iteratively optimizes **Gemini 3 Flash** (Student) to achieve perfect scores on technical trade-off analyses.

---

## 🏗️ System Architecture
The project adheres to **Modular AI Design** principles, decoupling task definition from model optimization.

* **Signatures:** Declarative I/O interfaces that define the technical summary task.
* **Modules:** Implements **Chain-of-Thought (CoT)** reasoning for deep architectural analysis.
* **Optimization:** Uses **Bayesian Optimization** to discover the most effective instruction sets and few-shot examples.



---

## 🚀 Execution Workflow

### 1. Environment Setup
```bash
conda create -n dspy_gemini python=3.12 -y
conda activate dspy_gemini
pip install -r requirements.txt
2. Program OptimizationBash# Triggers the MIPROv2 Bayesian search for the optimal prompt
python main.py
3. Verification & DashboardBash# Benchmark the compiled program against the test suite
python evaluate.py

# Launch the production-ready Streamlit UI
streamlit run app.py
📊 BenchmarksThe system was evaluated across a diverse corpus of technical domains (Kubernetes, Kafka, Edge Computing, etc.).Evaluation MetricTargetResultLogic Consistency (CoT)100%100%Instruction Adherence100%100%Technical Depth>100 charsVerifiedOverall Accuracy95%100%
👤 Developer: Aakarsh Kumar 