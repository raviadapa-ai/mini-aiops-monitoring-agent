# 🚀 Mini AIOps Platform

A simple AIOps system that ingests logs, computes metrics, detects anomalies, and exposes results via API.

---

## 📌 Features

### ✅ v1.0 (Initial Release)

* Log ingestion
* Log parsing
* Metrics computation
* Alert generation

### 🔥 v1.1 (Upgrade)

* Spike detection (window-based anomaly detection)

---

## 🏗️ Project Structure

```
aiops-mini-project/
│
├── ingestion/
│   └── log_reader.py
├── processing/
│   ├── parser.py
│   ├── metrics.py
│   └── spike_detection.py
├── alerting/
│   └── alerts.py
├── api/
│   └── app.py
├── data/
│   └── logs.txt
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup

### 1. Clone repo

```
git clone https://github.com/<your-username>/aiops-mini-platform.git
cd aiops-mini-platform
```

---

### 2. Create environment (recommended)

Using Anaconda:

```
conda create -n aiops python=3.10
conda activate aiops
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run Application

### CLI mode

```
python main.py
```

---

### API mode

```
python -m uvicorn api.app:app --reload
```

Open:

```
http://127.0.0.1:8000/analyze
```

---

## 📊 Example Output

```
{
  "metrics": {
    "total_logs": 100,
    "error_rate": 20.0,
    "avg_latency": 115.2
  },
  "alerts": [
    "⚠️ Moderate error rate",
    "🚨 High error rate"
  ],
  "spikes": [
    {
      "start": "2026-04-30 10:05:01",
      "end": "2026-04-30 10:05:10",
      "error_rate": 80.0
    }
  ]
}
```

---

## 🧠 Concepts Covered

* Log ingestion & parsing
* Observability metrics
* Alerting systems
* Sliding window anomaly detection

---

## 🚀 Future Improvements

* Time-based spike detection
* AI root cause analysis
* Real-time streaming (Kafka-style)
* Dashboard (Streamlit)

---

## 🏷️ Versioning

* v1.0 → Basic AIOps pipeline
* v1.1 → Spike detection added

---

## 📌 Author

Ravindra Adapa
