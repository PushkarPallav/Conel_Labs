# CloudDocs Log Anomaly Detection

## Overview

This project is a simple anomaly detection system built on top of application logs. The idea was to take raw log data (in JSONL format), process it, and identify patterns that could indicate suspicious or abnormal behavior.

Instead of just generating results, I also built an interactive dashboard where users can upload a log file and instantly see detected anomalies.

---

## What this project does

* Reads JSONL log files
* Cleans and preprocesses the data
* Detects suspicious patterns like:

  * Too many failed login attempts
  * Unusually high activity from a user
  * Access from multiple IP addresses
* Classifies anomalies into:

  * `critical`
  * `warning`
  * `info`
* Displays results in a Streamlit dashboard with filters and charts

---

## How I approached the problem

I started by exploring the dataset to understand what “normal” activity looks like. Based on that, I implemented a few rule-based checks:

* If a user has many failed logins → possible brute force attempt
* If a user performs too many actions → unusual behavior
* If a user logs in from many IPs → possible account compromise

The focus was to keep the system simple, understandable, and extendable.

---

## How to run the project

1. Clone the repository

```
git clone https://github.com/PushkarPallav/Conel_Labs.git
cd Conel_Labs
```

2. Create a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the dashboard

```
streamlit run dashboard/finalapp.py
```

5. Upload a `.jsonl` file and view results

---

## Project structure

```
data/          → input log file  
src/           → data processing and detection logic  
dashboard/     → Streamlit UI  
```

---

## Assumptions

* Thresholds are fixed and based on observation
* Multiple IP usage is treated as suspicious
* Missing values are handled conservatively

---

## What can be improved

* Replace rule-based detection with ML models
* Add geo-location based anomaly detection
* Improve visualization and drill-down analysis
* Handle real-time streaming data

---

## Final thoughts

This project was mainly about building an end-to-end pipeline — from raw logs to actionable insights — while keeping the system simple and practical.

---

👤 Pushkar Pallav
