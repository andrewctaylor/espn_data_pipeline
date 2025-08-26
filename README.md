# ESPN Data Pipeline

An end-to-end **ELT data pipeline** that ingests live ESPN API data, loads it into **Snowflake**, transforms it with **dbt**, and orchestrates everything using **Apache Airflow**.

> Built as a demonstration of modern data engineering practices: containerized orchestration, cloud warehouse modeling, and reproducible transformations.

---

## 🚀 Features
- **Automated ingestion** from ESPN API (Python requests → JSON).
- **Snowflake landing zone** for raw VARIANT data.
- **dbt models** to transform and normalize JSON into fact/dimension tables.
- **Airflow DAG** for orchestration (extract → load → transform → test).
- **Deduplication** strategy to handle repeated API payloads.
- **Dockerized environment** for reproducibility.

---

## 📂 Repository Structure
```
.
├── airflow/               # Airflow orchestration
│   ├── docker-compose.yaml
│   ├── Dockerfile
│   ├── dags/
│   │   └── news_pipeline.py
│   └── requirements.txt
│
├── espn_dbt/              # dbt models
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/
│   │   └── analytics/
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
│
└── espn_etl/              # Python Extract/Load + Snowflake Setup
    ├── backend/
    │   ├── api_calls.py
    │   └── snowflake_connect.py
    └── scripts/
        └── load_videos.py
```
---

## 🏗 Architecture

         +-------------+
         |  ESPN API   | 
         +------+------+ 
                |
                v
         +------+------------------+
         |   Python Extract/Load   |   ← Request data from ESPN's public API
         +-------+-----------------+
                 |
                 v
         +-------+------------+
         | Snowflake (RAW)    |   ← Insert raw json objects into Snowflake database
         +----------+---------+
                    |
                    v
         +----------+--------------------+
         | dbt (Staging/Transformation)  |   ← Apply dbt transformations to create various tables inside Snowflake
         +-----------+-------------------+
                     |
                     v
         +-----------+----------+
         | Airflow Orchestration|   ← Automate the entire pipeline to run daily
         +----------------------+
