# 🔬 ResearchMind: Autonomous Sequential Multi-Agent Research Engine

ResearchMind aik advanced AI-powered content research aur analysis application hai jise **LangChain Expression Language (LCEL)**, **Mistral AI (`mistral-large-2512`)**, aur **Streamlit** ke saath design kiya gaya hai. 

Yeh system four specialized agents aur chains ko aik linear pipeline (Sequential Hand-off framework) me connect karta hai jo raw user queries se lekar structured, verified research reports generate karne ka kaam automate karta hai.

---

## 🏗️ System Architecture & Agent Workflow

Application ka multi-agent architecture decoupled design principles par chalta hai, jahan har stage ka output agle stage ke liye context banta hai:
