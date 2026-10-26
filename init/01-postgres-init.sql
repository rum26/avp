CREATE SCHEMA IF NOT EXISTS avp;

CREATE TABLE IF NOT EXISTS avp.log (
    id SERIAL PRIMARY KEY,
    date TEXT,
    time TEXT,
    comment TEXT
);