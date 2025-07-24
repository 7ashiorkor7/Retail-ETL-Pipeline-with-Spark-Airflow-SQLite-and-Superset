# Retail-ETL-Pipeline-with-Spark-Airflow-SQLite-and-Superset
This project demonstrates an end-to-end Retail Data Engineering pipeline built using open-source tools and designed to run entirely on a local machine (or AWS Free Tier). It simulates how raw retail data flows through an ETL process into a lightweight data warehouse and is visualized in an interactive dashboard.

As a data scientist delving into data engineering through hands-on projects due to my aspiration to be a full-stack data scientist. I thrive on solving tough setup issues, learning cloud-native tools, and building real-world systems step by step.
This project showcases:
- Problem-solving under resource constraints
- Working fluently with Docker
- Running Spark jobs outside of tutorials
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

## What Makes This Unique

> I didn’t clone this. I rebuilt it from the ground up using Docker and open-source tools under strict resource constraints.

###  Challenges Faced:
| Problem | How I Solved It |
|--------|------------------|
| Spark threw `basedir must be absolute` error | Set `HOME=/tmp` inside the container |
| Ivy dependency resolution failed | Used `-e HOME=/tmp` during `docker run` |
| Files weren’t accessible in container | Properly mounted host path with `-v "..."` syntax |
| Output wasn’t saving | Directed Spark to write explicitly to mounted `/opt/app/data/processed/` |

> Because I was on the AWS Free Tier, I opted for Docker instead of EMR, which came with its own challenges like managing Windows path quirks, wrangling Spark’s verbose logs, and working around Docker’s memory limitations.

## Tech Stack

| Layer | Tools |
|-------|-------|
|  Raw Data | CSVs in `/data/raw/` |
|  ETL | Apache Spark (Python) |
|   Database | SQLite (future step) |
|   Visualization | Apache Superset |
|  Orchestration | Apache Airflow |
|  Containerization | Docker |
