from datetime import datetime
from zoneinfo import ZoneInfo

from airflow.sdk import dag
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator


moscow_time = datetime.now(ZoneInfo("Europe/Moscow")).strftime("%H:%M")

POSTGRES_CONN_ID = "postgres_conn"
VERTICA_CONN_ID = "vertica_conn"

INSERT_SQL = f"""
INSERT INTO avp.log (date, time, comment)
VALUES (
    '{datetime.now(ZoneInfo("Europe/Moscow")).strftime("%Y-%m-%d")}',
    '{moscow_time}',
    'Тестовая запись из Airflow'
);
"""

@dag(
    dag_id="write_log_to_postgres_and_vertica",
    start_date=datetime(2026, 1, 1),
    schedule="0 * * * *",
    catchup=False,
    tags=["postgres", "vertica"],
)
def write_log_dag():
    write_postgres = SQLExecuteQueryOperator(
        task_id="write_to_postgres",
        conn_id=POSTGRES_CONN_ID,
        sql=INSERT_SQL,
    )

    write_vertica = SQLExecuteQueryOperator(
        task_id="write_to_vertica",
        conn_id=VERTICA_CONN_ID,
        sql=INSERT_SQL,
    )

    write_postgres >> write_vertica


write_log_dag()
