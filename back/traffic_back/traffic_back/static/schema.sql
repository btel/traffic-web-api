DROP TABLE IF EXISTS traffic;

CREATE TABLE traffic (
    id serial PRIMARY KEY,
    timestamp varchar,
    debit integer,
    percent real);

