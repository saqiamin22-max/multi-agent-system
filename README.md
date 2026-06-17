# 🔬 ResearchMind: Autonomous Sequential Multi-Agent Research Engine

ResearchMind is an advanced AI-powered content research and analysis application built using **LangChain Expression Language (LCEL)**, **Mistral AI (`mistral-large-2512`)**, and **Streamlit**. 

The system connects four specialized agents and chains into a linear pipeline (Sequential Hand-off framework) that automates the entire process—from processing raw user queries to generating structured, verified research reports.

---

## 🏗️ System Architecture & Agent Workflow

The application’s multi-agent architecture operates on decoupled design principles, where the output of each stage serves as the direct operational context for the next stage:
