# 🛠️ AI Technical Remediation Planner

An AI-powered application that transforms technical audit findings into a structured remediation plan, prioritized Agile backlog, effort estimation, dependency analysis, and implementation roadmap.

Built with **Python**, **Streamlit**, and **Google Gemini AI**.

---

## 📌 Overview

Technical audit reports often contain dozens of findings that must be analyzed, prioritized, and transformed into actionable development tasks.

This project automates that process by combining:

* Deterministic priority calculation
* Large Language Models (LLMs)
* Agile backlog generation

The result is an interactive application capable of converting a raw technical audit report into a structured remediation plan ready for project teams.

---

## 🚀 Features

* 📂 Upload technical audit reports in JSON format
* 🔍 Automatic analysis of audit findings
* 📊 Deterministic priority scoring
* 🤖 AI-generated remediation plan using Gemini
* 📋 Agile backlog generation
* ⏱️ Effort estimation (Man-Days)
* 🔗 Dependency identification
* 🛣️ Suggested implementation roadmap
* 📈 Interactive Streamlit interface

---

## 🏗️ Project Architecture

```
Audit Report (JSON)
          │
          ▼
 Priority Calculation Engine
 (Deterministic Python Logic)
          │
          ▼
      Gemini AI
(Remediation Generation)
          │
          ▼
 Prioritized Agile Backlog
          │
          ▼
 Streamlit Dashboard
```

---

## 📁 Project Structure

```
AI-Technical-Remediation-Planner/
│
├── app.py
├── requirements.txt
├── .gitignore
│
├── core/
│   ├── config.py
│   ├── llm_client.py
│   ├── matrix_calculator.py
│   └── prompt_templates.py
│
└── data/
    ├── audit_report.json
    └── Technical_Audit_Report_Raw.pdf
```

---

## ⚙️ Technologies

* Python
* Streamlit
* Google Gemini API
* JSON
* Prompt Engineering

---

## 🧠 How It Works

### 1. Upload an Audit Report

The application loads a structured technical audit report in JSON format.

### 2. Calculate Priority

A deterministic algorithm calculates a priority score for every finding based on predefined impact and implementation effort values.

```
Priority Score = Impact / Effort
```

The findings are automatically sorted before being sent to the language model.

### 3. AI Analysis

Gemini receives the prioritized findings and generates:

* Technical remediation
* Estimated implementation effort
* Dependencies
* Agile backlog items
* Acceptance criteria

### 4. Dashboard

Results are displayed in an interactive Streamlit interface.

---

## ▶️ Installation

```bash
git clone https://github.com/firdawss-Elhaddouchi/AI-Technical-Remediation-Planner.git

cd AI-Technical-Remediation-Planner

pip install -r requirements.txt
```

Create a `.env` file:

```
GEMINI_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

---

## 📊 Example Output

The application generates:

* Prioritized findings
* Technical remediation plan
* Agile backlog
* Estimated effort
* Dependencies
* Acceptance criteria

---

## 📌 Current Limitations

* Priority weights are predefined.
* Effort estimation relies on AI and should be validated by engineers.
* Supports JSON audit reports.

---

## 💡 Future Improvements

* Support additional audit formats (PDF, SARIF, CSV).
* Export backlog to Jira or Azure DevOps.
* Interactive roadmap visualization.
* Dynamic prioritization using historical project data.
* Multi-model AI support.

---

## 👩‍💻 Author

Developed as an AI-assisted software engineering project demonstrating how deterministic algorithms and Large Language Models can work together to transform technical audit findings into actionable remediation plans.
