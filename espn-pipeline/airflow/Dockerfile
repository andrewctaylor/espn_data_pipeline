FROM apache/airflow:2.9.3-python3.11

ARG AIRFLOW_VERSION=2.9.3
ARG PYTHON_VERSION=3.11
ARG CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
 && pip install --no-cache-dir -r /requirements.txt --constraint "${CONSTRAINT_URL}"

RUN pip install --no-cache-dir "dbt-core==1.8.*" "dbt-snowflake==1.8.*"

WORKDIR /opt/airflow
