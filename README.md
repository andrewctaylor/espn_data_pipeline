# ESPN Article Data Pipeline



An end-to-end **ELT data pipeline** that ingests live ESPN API data, loads it into **Snowflake**, transforms it with **dbt**, and orchestrates everything using **Apache Airflow**.

I built this project for two reasons:
    > I'm a big sports fan and discovered ESPN's public API a while ago. I particularly thought the API for ESPN's daily articles had potential for a fun project, and I noticed that this API wasn't being utilized by         many other projects. The data takes form as a decently-sized json object, so my goal was to build up a clean database overtime so that others may conviently use this public data.
    > I've been looking for an excuse to learn many of the industry standard tools like Snowflake, dbt, and Apache Airflow, and this gave me the oppurtunity to do so.

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
