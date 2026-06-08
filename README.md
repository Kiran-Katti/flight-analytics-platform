# Flight Analytics Platform

An end-to-end data engineering and analytics project that ingests flight data, loads it into PostgreSQL, transforms it using dbt, and serves analytical insights through an interactive Dash dashboard.

## Architecture

```text
CSV Files
    ↓
Python ETL
    ↓
PostgreSQL
    ↓
dbt Models
    ↓
Star Schema
    ↓
Analytics Marts
    ↓
Dash Dashboard
```

## Tech Stack

* Python
* PostgreSQL
* Docker
* SQLAlchemy
* Pandas
* dbt
* Dash
* Plotly
* Git

## Dataset Size

| Dataset   |   Records |
| --------- | --------: |
| Flights   | 1,936,758 |
| Airports  |    85,539 |
| Countries |       249 |

## Project Objectives

* Build an end-to-end data pipeline for flight analytics.
* Implement ETL processes using Python and Pandas.
* Store and manage data in PostgreSQL.
* Transform raw data into analytical models using dbt.
* Design a star schema for reporting and analysis.
* Develop interactive dashboards using Dash and Plotly.
* Apply software engineering best practices with Git and Docker.

```
```

## Dashboard Screenshots

* Overview

<img width="1891" height="672" alt="image" src="https://github.com/user-attachments/assets/81153c76-5928-4a22-81f0-14533541f00d" />

* Carrier Performance

<img width="1890" height="661" alt="image" src="https://github.com/user-attachments/assets/84def21b-1dfe-4e58-834d-10d6f70da24d" />

* Airport Analytics

<img width="1896" height="682" alt="image" src="https://github.com/user-attachments/assets/057be2ac-303e-4a53-9598-281ee2cf5b63" />
