# 🚀 Mini AIOps Platform
---
A lightweight AIOps system that processes logs, generates metrics, detects incidents (spikes), performs root cause analysis, and produces summarized operational insights based on the sample log.

---

````
Sample log
2026-04-30 10:00:01 INFO server1 Request processed in 110ms
2026-04-30 10:00:02 INFO server2 Request processed in 95ms
2026-04-30 10:00:03 INFO server3 Request processed in 130ms
2026-04-30 10:00:04 ERROR server1 Database timeout
2026-04-30 10:00:05 INFO server2 Request processed in 102ms
2026-04-30 10:00:06 INFO server3 Request processed in 98ms
2026-04-30 10:00:07 INFO server1 Request processed in 115ms
2026-04-30 10:00:08 CRITICAL server2 Service crashed
2026-04-30 10:00:09 INFO server3 Request processed in 120ms
2026-04-30 10:00:10 INFO server1 Request processed in 140ms
2026-04-30 10:00:11 ERROR server3 Cache miss storm
2026-04-30 10:00:12 INFO server2 Request processed in 90ms
2026-04-30 10:00:13 INFO server1 Request processed in 105ms
2026-04-30 10:00:14 INFO server3 Request processed in 100ms
2026-04-30 10:00:15 INFO server2 Request processed in 92ms
2026-04-30 10:00:16 ERROR server1 Connection reset
2026-04-30 10:00:17 INFO server3 Request processed in 135ms
2026-04-30 10:00:18 INFO server2 Request processed in 101ms
2026-04-30 10:00:19 INFO server1 Request processed in 108ms
2026-04-30 10:00:20 INFO server3 Request processed in 125ms
```

---

## 📌 System Overview

This project simulates a real-world observability pipeline:

```
Logs → Parsing → Metrics → Alerts → Spike Detection → Root Cause Analysis → Summary Intelligence
```

---

## ✨ Features

### ✅ Core (v1.0)

* Log ingestion system
* Log parsing engine
* Metrics computation (error rate, latency)
* Rule-based alerting

---

### 🔥 Incident Detection (v1.1)

* Spike detection using sliding window logic
* Detection of error bursts in logs

---

### 🧠 RCA Layer (v1.3)

* Root cause extraction from logs
* Server-level failure mapping
* Error categorization (timeout, connection, lock issues)

---

### 📊 Intelligence Layer (v1.4)

* Root cause normalization
* Dominant issue aggregation
* System-level failure summary

---
### 🤖 LLM Incident Reporting (v1.5)

This version introduces an AI-style incident reporting layer.

🧠 LLM Mode
* Default mode: Fallback / Mock LLM
* No external API required
* Deterministic structured output for testing

🔄 Optional Real LLM Support
* OpenAI / GPT integration supported
* Requires API key in .env
* Currently disabled for safe execution

📊 LLM Output Includes
* What happened
* Root cause
* Impact
* Recommendation
* Incident brief (clean paragraph format)

## 🏗️ Project Structure

```
aiops-mini-project/
│
├── ingestion/
│   └── log_reader.py
│
├── processing/
│   ├── parser.py
│   ├── metrics.py
│   ├── spike_detection.py
│
├── analysis/
│   ├── root_cause.py
│   └── llm_insight.py
│
├── alerting/
│   └── alerts.py
│
├── api/
│   └── app.py
│
├── data/
│   └── logs.txt
│
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone repository

```bash
git clone https://github.com/<your-username>/aiops-mini-project.git
cd aiops-mini-project
```

---

### 2. Create environment (recommended)

```bash
conda create -n aiops python=3.10
conda activate aiops
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the project

### CLI mode

```bash
python main.py
```

---

### API mode

```bash
python -m uvicorn api.app:app --reload
```

Open:

```
http://127.0.0.1:8000/analyze
```

---

## 📊 Sample Output

```json
{
  "metrics": {
    "total_logs": 100,
    "error_rate": 20,
    "avg_latency": 115.21
  },
  "alerts": [
    "⚠️ Moderate error rate",
    "🚨 High error rate"
  ],
  "spikes": [
    {
      "start": "2026-04-30 10:00:04",
      "end": "2026-04-30 10:00:12",
      "error_rate": 40
    }
  ],
  "root_cause": [
    {
      "root_cause": "DB timeout",
      "affected_server": "server1"
    }
  ],
  "summary": {
    "dominant_issue": "DB Timeout",
    "occurrences": 3
  },
  "llm_report": {
    "what_happened": "Database failures caused repeated spikes",
    "root_cause": "Database instability",
    "impact": "Increased latency and error rate",
    "recommendation": "Scale DB and optimize queries",
    "brief": "Between 10:00 and 10:04, multiple error spikes were observed across server1, server2, and server3. The majority of failures were related to database timeouts."
  }
}
```

---

## 🧠 Key Concepts Learned

* Log ingestion pipelines
* Observability metrics
* Sliding window anomaly detection
* Root cause analysis (RCA)
* Data aggregation & summarization
* AI-powered incident reporting (LLM layer)

---

## 📈 Version History

* v1.0 → Metrics + Alerts
* v1.1 → Spike detection
* v1.2 → Spike deduplication
* v1.3 → Root cause analysis
* v1.4 → RCA normalization + summary intelligence
* v1.5 → LLM incident reporting (fallback mode + optional real LLM support)

---

## 🔮 Future Improvements

* Context-aware LLM reasoning engine
* Auto-remediation system
* Real-time streaming ingestion
* Incident prediction layer
* Dashboard (Streamlit / React)

---

## 👨‍💻 Author

Built as a learning AIOps system for observability engineering practice.
