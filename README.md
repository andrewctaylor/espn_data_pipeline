# ESPN Article Data Pipeline

An end-to-end **ELT data pipeline** that ingests live ESPN API data, loads it into **Snowflake**, transforms it with **dbt**, and orchestrates everything using **Apache Airflow**.

I built this project for two main reasons:
1. **Sports + Data**: As a big sports fan, I discovered ESPN’s public API and noticed that its daily articles endpoint wasn’t widely used in other projects. Since the API returns rich JSON payloads, I wanted to build a clean, queryable database of ESPN articles over time — making this public data more accessible to others.
2. **Learning Modern Data Tools**: I wanted hands-on experience with industry-standard tools like **Snowflake**, **dbt**, and **Apache Airflow**. This project gave me the opportunity to connect them all into a working pipeline.

---

## 🚀 Features
- **Automated ingestion** from ESPN’s public API (Python requests → JSON).
- **Snowflake landing zone** for raw `VARIANT` JSON.
- **dbt models** to normalize and transform JSON into fact/dimension tables.
- **Airflow DAG** for orchestration (extract → load → transform → test).
- **Deduplication** to prevent repeated payloads.
- **Dockerized environment** for reproducibility.

---

## 📂 Repository Structure
```text
.
├── airflow/               # Airflow orchestration
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   ├── dags/
│   │   └── news_pipeline.py
│   └── requirements.txt
│
├── espn_dbt/              # dbt project
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/       # flatten JSON into structured tables
│   │   └── analytics/     # fact/dimension tables
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
│
└── espn_etl/              # Python Extract/Load utilities
    ├── backend/
    │   ├── api_calls.py           # pulls data from ESPN API
    │   └── snowflake_connect.py   # inserts JSON into Snowflake
    └── scripts/
        └── load_videos.py         # CLI entrypoint for local runs

```
## 🏗 Data Pipeline
```
        +-------------+
        |   ESPN API  |
        +------+------+
               |
               v
   +-----------+-----------+
   | Python Extract/Load   |   ← Request data from ESPN API + load to Snowflake
   +-----------+-----------+
               |
               v
   +-----------+-----------+
   |  Snowflake (RAW)      |   ← Store raw JSON (VARIANT column)
   +-----------+-----------+
               |
               v
   +-----------+-----------+
   | dbt (Transformations) |   ← Staging + analytics models
   +-----------+-----------+
               |
               v
   +-----------+-----------+
   | Airflow Orchestration |   ← DAG to run daily (ingest → transform → test)
   +-----------------------+
```
