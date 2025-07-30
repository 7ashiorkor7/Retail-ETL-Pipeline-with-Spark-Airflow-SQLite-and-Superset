# Retail-ETL-Pipeline-with-Spark-Airflow-SQLite-and-Superset
I love data and versatility. Lately, I have been curious about being a full-stack data scientist. So, I decided to give it a shot by building up my data engineering skills. However, I had some exposure to it through work experiences where I had to cover basic data engineering tasks as the only data scientist on the team. Wonderful right? This project focuses on building a Retail ETL Pipeline. Buying and selling go on everywhere in the world, so a common project to start with. I have been bolted out of my comfort zone with this project, and I must admit that I enjoyed it even amidst the challenges. The initial plan was to use AWS, but my free tier subscription did not cover the demands of the project, so Docker came to the rescue. Don't we all love technology? There is almost always a substitute. Never say never! Interestingly, I also encountered resource constraints locally. But like I said, never say never! I'm excited about everything I have learnt so far. Data engineering has a number of moving parts, which makes it fun and, at the same time, demanding. I appreciate data engineering more and more now. If you want all the nitty-gritty of this project, kindly find it below. 

This project demonstrates an end-to-end Retail Data Engineering pipeline built using open-source tools and designed to run entirely on a local machine. It simulates how raw retail data flows through an ETL process into a lightweight data warehouse and is visualised in an interactive dashboard.

As a data scientist delving into data engineering through hands-on projects due to my aspiration to be a full-stack data scientist. 
This project showcases:
- Problem-solving under resource constraints
- Working fluently with Docker
- Running Spark jobs 
- My curiosity and willingness to learn in public

## Overview

This project is a **complete end-to-end Retail ETL pipeline**, engineered entirely from scratch, using:

- **Apache Spark** for scalable transformations
- **Airflow** for orchestration
- **SQLite** for lightweight data storage
- **Apache Superset** for interactive dashboards
- **Docker** to containerise and simplify everything

It simulates the backend of a retail store, processing raw data into clean analytics-ready tables.

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/c9f16d63-85ab-4f7e-8fb4-b24d5c6f78ea" />

<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/a1807f94-7866-4d90-a8fe-af532edc79d7" />

## Use Case

Imagine a retail chain generating daily data across:
- Inventory
- Sales
- Products
- Stores
- Calendar events

The goal: **centralise, transform, and analyse** this fragmented data to answer business questions like:
- How are sales trending by store and product?
- What’s the current inventory situation?
- What gross margin are we making per product category?

## What Makes This Unique and what I enjoyed about it

> I didn’t clone this. I rebuilt it from the ground up using Docker and open-source tools under strict resource constraints.
> This project really challenged me. I hadn’t used Docker in a few years, so getting everything to run smoothly was tough at first. Especially troubleshooting container permissions, environment variables, and Superset integration. But it turned into a fun and rewarding learning experience.
> More than anything, it reinforced my aspiration to become a full-stack data scientist — someone who can seamlessly blend engineering, modeling, analysis, and visualization, and excel at each even when faced with tough challenges.

## Tech Stack

| Layer | Tools |
|-------|-------|
|  Raw Data | CSVs in `/data/raw/` |
|  ETL | Apache Spark (Python) |
|   Database | SQLite  |
|   Visualization | Apache Superset |
|  Orchestration | Apache Airflow |
|  Containerization | Docker |

## Project Structure
```
Retail-ETL-Pipeline-with-Spark-Airflow-SQLite-and-Superset/
│
├── data/
│   ├── raw/                         # Original dummy datasets (calendar, sales, etc.)
│   └── processed/                   # Output data after Spark transformation
│
├── spark_jobs/
│   ├── transformation.py            # PySpark script for ETL processing
│   └── retail_etl.py                # Alternate or combined ETL logic (if applicable)
│
├── scripts/
│   ├── generate_dummy_data.py       # Script to generate sample retail datasets
│   ├── load_data_to_sqlite.py       # Loads transformed data into SQLite
│   └── queries.sql                  # SQL queries for analysis and validation
│
├── docker/
│   ├── docker-compose.yml           # Orchestrates services (Spark, Airflow, etc.)
│   └── dags/
│       └── retail_pipeline_dag.py   # Airflow DAG to automate the ETL pipeline
│
├── retail_oltp.db                   # SQLite database storing the final results
├── notebooks/                       # Jupyter notebooks for data exploration
└── README.md                        # Project documentation
```

### Challenges Faced

| Problem | How I Solved It | What I Learned |
|--------|------------------|----------------|
| Spark threw `basedir must be absolute` error | Set `HOME=/tmp` inside the container | Environment variables can make or break Spark jobs in Docker. |
| Ivy dependency resolution failed | Used `-e HOME=/tmp` during `docker run` | Some Spark dependencies need explicit directory access to resolve correctly. |
| Files weren’t accessible in the container | Properly mounted host path with `-v "..."` syntax | Docker file mounting must be handled carefully, especially on Windows. |
| Output wasn’t saving | Directed Spark to write explicitly to mounted `/opt/app/data/processed/` | Always define exact write paths when using shared volumes. |
| Superset: `FATAL: database "superset_metadata" does not exist` | Created `init-superset-db.sql` in `docker-entrypoint-initdb.d` and restarted with volume reset | Initial DB setup should be handled automatically via entrypoint scripts. |
| Superset: `UniqueViolation` on `superset db upgrade` | Ran `docker volume rm` to reset corrupted database state | When migrations fail, it’s often better to wipe and reset than debug endlessly. |
| Superset: `DeadlockDetected` from concurrent migrations | Added a `superset_init` service with `restart: "no"` and `depends_on` | Separate one-time setup tasks from runtime services to avoid conflicts. |
| Superset: `ModuleNotFoundError: No module named 'psycopg2'` | Added `psycopg2-binary` and `sqlalchemy-utils` to pip install in container | Every container needs its own dependencies, even if they share a base image. |

> Because I was on the AWS Free Tier, I opted for Docker instead of EMR, which came with its own challenges like managing Windows path quirks, wrangling Spark’s verbose logs, and working around Docker’s memory limitations.

## Superset Dashboard: Sales Performance Insights

This project includes an interactive dashboard built using **Apache Superset** to explore and communicate sales performance across stores and time.  
All visualisations were powered by **custom SQL queries**, not drag-and-drop, which demonstrates full control over data aggregation, filtering, and transformation.

![sales_performance_dashboard](https://github.com/user-attachments/assets/6e567aff-487b-4690-aa8d-8edc01f1d95c)

