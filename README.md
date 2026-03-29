# 📊 End-to-End Real-Time Data Pipeline with Kafka for User Interaction Analytics

## 📌 Overview
This project implements a **real-time data pipeline** that simulates user interaction events, processes them using a streaming architecture, and visualizes live metrics via a dashboard.

It demonstrates **production-level data engineering practices**, including event streaming, stateful aggregation, alerting, and containerized deployment.

---

## 🏗️ Architecture
Producer → Kafka → Aggregator → JSON Store → Streamlit Dashboard

### Components
- **Producer (`producer.py`)**: Simulates user events (`click`, `view`, `purchase`) and publishes them to Kafka.  
- **Kafka**: Distributed event streaming platform that decouples producers and consumers.  
- **Aggregator (`aggregator.py`)**: Consumes Kafka events, aggregates data by user/item, writes results to `aggregated_data.json`, and triggers threshold-based alerts.  
- **Dashboard (`dashboard.py`)**: Live visualization of aggregated metrics using Streamlit.  

---

## ⚙️ Tech Stack
- **Streaming**: Apache Kafka  
- **Processing**: Python  
- **Visualization**: Streamlit  
- **Infrastructure**: Docker & Docker Compose  
- **Storage**: JSON (lightweight)  

---

## 🚀 Features
- Real-time ingestion of user interaction events  
- Continuous aggregation per user/item  
- Threshold-based alerting system  
- Live dashboard displaying:
  - Top users and items
  - Event type distribution
  - Real-time alerts  
- Dockerized setup for quick deployment  

---

## 📊 Data Flow
1. `producer.py` generates simulated events.  
2. Events are published to Kafka topic `user_interactions`.  
3. `aggregator.py` consumes events and:
   - Maintains in-memory aggregations  
   - Writes results to `aggregated_data.json`  
   - Triggers alerts if thresholds are exceeded  
4. `dashboard.py` reads the aggregated data and updates visuals in real time.  

---

## 🚀 Setup & Execution

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Kafka & Zookeeper

```bash
docker-compose up -d
docker ps
```

Verify that services are running:

* **Kafka** → `localhost:9092`
* **Zookeeper** → `localhost:2181`

---

## ▶️ Run the Pipeline

Open three separate terminals:

### Terminal 1 – Producer

```bash
python producer.py
```

### Terminal 2 – Aggregator

```bash
python aggregator.py
```

### Terminal 3 – Dashboard

```bash
streamlit run dashboard.py
```

Open the dashboard in your browser:

```
http://localhost:8501
```

---

## 📊 Streamlit Dashboard

Below are example snapshots of the live dashboard:

<p float="left">
  <img src="output_images/dashboard_screenshot1.png" width="300" />
  <img src="output_images/dashboard_screenshot2.png" width="300" />
  <img src="output_images/dashboard_screenshot3.png" width="300" />
</p>

---

## 📈 Metrics & Insights

The dashboard provides real-time visibility into:

* Interactions per user
* Interactions per item
* Event type distribution
* Real-time threshold alerts

---

## ⚠️ Alerting

* Thresholds can be configured in `aggregator.py`
* Alerts are triggered when user or item activity exceeds defined limits
* Alerts are logged in real time in the aggregator console

---

## 🧠 Design Considerations

### Scalability

* Kafka partitions enable horizontal scaling
* Multiple consumers can process data in parallel

### Fault Tolerance

* Kafka retains messages for replay
* Aggregator can be extended with checkpointing

### Extensibility

Current JSON storage can be replaced with:

* **Redis** (low latency)
* **PostgreSQL** (durable storage)
* **Data warehouse** (analytics workloads)

---

## 🔮 Future Improvements

* Windowed aggregations (tumbling/sliding windows)
* Stateful processing frameworks (Kafka Streams / Faust)
* Persistent state storage (Redis / RocksDB)
* REST API for exposing aggregated metrics
* Kubernetes-based deployment
* Monitoring & alerting (Prometheus + Grafana)

---

## 📚 Skills Demonstrated

* Real-time data streaming
* Event-driven architecture
* Kafka producer/consumer patterns
* Stateful aggregation
* Docker-based deployment
* Data pipeline design and monitoring

---

## 🤝 Acknowledgement

Some parts of this implementation were developed with AI assistance.
All testing, validation, and integration were performed independently.
developed with AI assistance.
All testing and validation were done independently.
