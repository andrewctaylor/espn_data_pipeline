# ESPN Article Data Pipeline

An end-to-end **ELT data pipeline** that ingests live ESPN API data, loads it into **Snowflake**, transforms it with **dbt**, and orchestrates the process using **Apache Airflow**.

I built this project for two main reasons:
1. **Sports + Data**: I'm a huge sports fan. Recently, I discovered ESPN’s public API and noticed that its live articles endpoint wasn’t widely used in other projects. The API returns JSON payloads, so I wanted to build a clean/queryable database of ESPN articles over time. Hopefully this will help make this public data more accessible to others.
2. **Learning Modern Data Tools**: I wanted hands-on experience with industry-standard tools like **Snowflake**, **dbt**, and **Apache Airflow**. This project gave me a convenient excuse to self-learn them all while building this pipeline.

**(This project is still being improved, any feedback/suggestions are welcomed and appriciated)**

**Primary tools used:** Snowflake, dbt, Apache Airflow, Docker, Python

# Setup

1. **Clone the repo**

   ```bash
   git clone https://github.com/andrewctaylor/espn_data_pipeline.git
   cd espn_data_pipeline
   ```

2. **Configure environment**

   Copy the example and fill in your credentials.

   ```bash
   cp .env-example .env
   # open .env and set values
   ```

3. **Initialize Airflow** (one-time)

   Run database migrations and create the admin user.

   ```bash
   cd airflow
   docker compose up airflow-init
   # user/password should be set in .env
   ```

4. **Launch services**

   ```bash
   docker compose up -d
   ```

Open the Airflow UI at `http://localhost:8080`  
Log in with the username/password you set in your `.env`.
After this you should be abel to trigger the DAG manually and/or debug it




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
├── espn_dbt/              # dbt models
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── staging/       
│   │   └── analytics/     
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
│
└── espn_etl/              # Python Extract/Load utilities
    ├── backend/
    │   ├── api_calls.py           # pulls data from ESPN API
    │   └── snowflake_connect.py   # connects to Snowflake DB
    └── scripts/
        └── load_videos.py         # inserts JSON into Snowflake

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
   |  Snowflake (RAW)      |   ← Store raw JSON payload
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

## ❄️ Data Model (Stored in Snowflake, built via dbt)
All of the data is stored in a singular database called **API_DATA_DB**:
```
## RAW_JSON schema

| Table              | Role                         | Key Columns                              |
|--------------------|------------------------------|------------------------------------------|
| `NEWS_RAW`         | Stores raw JSON payloads     | `id` (UUID), `created_at`                |
|                    |                              | `json_blob` (VARIANT), `sport`, `league` |

## MODELS schema

| Table        | Type        | Primary Key     | Foreign Keys         | Notes                    |
|--------------|-------------|-----------------|----------------------|--------------------------|
| `ARTICLES`   | Fact        | `article_id`    |                      | ~12 additional features  |
| `CATEGORIES` | Dimension   | `category_id`   | `article_id`         | ~18 additional features  |
| `IMAGES`     | Dimension   | `image_id`      | `article_id`         | ~11 additional features  |
| `LINKS`      | Dimension   | `link_id`       | `article_id`         | ~5 additional features   |
  
STAGING views
- STG_NEWS — move data from RAW schema to MODELS schema
- ARTICLES_RAW - flatten raw JSON payloads into semi-structured JSON objects for articles
- CATEGORIES_RAW - flatten article data into semi-structured JSON objects for categories
```

