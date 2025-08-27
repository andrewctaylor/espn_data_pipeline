# ESPN Article Data Pipeline

An end-to-end **ELT data pipeline** that ingests live ESPN API data, loads it into **Snowflake**, transforms it with **dbt**, and orchestrates everything using **Apache Airflow**.

I built this project for two main reasons:
1. **Sports + Data**: As a big sports fan, I discovered ESPN’s public API and noticed that its daily articles endpoint wasn’t widely used in other projects. The API returns JSON payloads, so I wanted to build a clean/queryable database of ESPN articles over time. Hopefully this will help make this public data more accessible to others.
2. **Learning Modern Data Tools**: I wanted hands-on experience with industry-standard tools like **Snowflake**, **dbt**, and **Apache Airflow**. This project gave me the opportunity to self-learn them all while building this pipeline.

---

## 🚀 Features
- **Automated ingestion** from ESPN’s public API via Python.
- **Snowflake** to store raw, staging, and analytical data.
- **dbt models** to transform JSON into fact/dimension tables.
- **Airflow DAG** for orchestration.
- **Dockerized environment** for reproducibility.

**Primary tools used:** Snowflake, dbt, Apache Airflow, Docker, Python

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

🗄 Data Model (Snowflake)
All of the data is stored in a singular database called **API_DATA_DB**:

    RAW (schema):
        NEWS_RAW ← Table for inserting raw JSON payloads
            - RAW_JSON.NEWS_RAW
            - id (UUID)
            - json_blob (VARIANT)
            - sport, league
            - created_at
            
    MODELS (schema):
        ARTICLES ← Central Fact Table 
            - article_id (primary key)
            - 12 additional features
        CATEGORIES (Dimension)
            - category_id (primary key)
            - article_id
            - 18 additional features
        IMAGES (Dimension)
            - image_id (primary key)
            - article_id
            - 11 additional features
        LINKS (Dimension)
            - image_id (primary key)
            - article_id
            - 5 additional features
  
STAGING
- STG_NEWS — flatten articles (IDs, headlines, timestamps, authors).
- STG_TEAMS — normalize team metadata.
  
CORE (Analytics)
- ARTICLES — deduplicated fact table of articles.
- TEAMS — team dimension.
ARTICLE_TEAM — bridge table (many-to-many link between articles and teams).
