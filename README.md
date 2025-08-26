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


---

## 🏗 Architecture

         +-------------+
         |   ESPN API  |
         +------+------+ 
                |
                v
        +-------+--------+
        |   Python ETL   |   ← requests, pandas
        +-------+--------+
                |
                v
      +---------+----------+
      | Snowflake (RAW)    |   ← json_blob (VARIANT)
      +---------+----------+
                |
                v
     +----------+----------+
     | dbt (Staging/Core)  |   ← normalized tables
     +----------+----------+
                |
                v
     +----------+----------+
     | Airflow Orchestration|
     +----------------------+
