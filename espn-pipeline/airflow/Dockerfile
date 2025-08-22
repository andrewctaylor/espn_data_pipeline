FROM apache/airflow:2.10.2-python3.11

USER root
RUN apt-get update && apt-get install -y --no-install-recommends git \
    && rm -rf /var/lib/apt/lists/*
USER airflow

ENV PATH="/home/airflow/.local/bin:${PATH}"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt
