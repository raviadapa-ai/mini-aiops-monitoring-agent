# 🚀 Mini AIOps Platform

A lightweight AIOps system that processes logs, generates metrics, detects incidents (spikes), performs root cause analysis, and produces summarized operational insights.

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
│   └── root_cause.py
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

---

## 📈 Version History

* v1.0 → Metrics + Alerts
* v1.1 → Spike detection
* v1.2 → Spike deduplication
* v1.3 → Root cause analysis
* v1.4 → RCA normalization + summary intelligence

---

## 🔮 Future Improvements

* AI-based root cause classification (LLM)
* Predictive anomaly detection
* Auto-remediation system
* Real-time streaming (Kafka-style ingestion)
* Dashboard (Streamlit / React)

---

## 👨‍💻 Author

Built as a learning AIOps system for observability engineering practice.
