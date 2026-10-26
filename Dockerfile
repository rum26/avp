FROM apache/airflow:3.0.6-python3.11

RUN pip install \
    apache-airflow-providers-postgres \
    apache-airflow-providers-vertica