import os

# Use Postgres for Superset internal database (more reliable)
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://airflow:airflow@postgres:5432/superset_metadata'

# Security key (change this in production)
SECRET_KEY = 'retail_etl_superset_key_12345'

# Feature flags
FEATURE_FLAGS = {
    'ENABLE_TEMPLATE_PROCESSING': True,
    'ALERT_REPORTS': True,
    'DYNAMIC_PLUGINS': True,
}

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'simple',
}

# SQL Lab configuration
SQLLAB_CTAS_NO_LIMIT = True
SUPERSET_WEBSERVER_TIMEOUT = 300

# Enable file uploads (if needed)
UPLOAD_FOLDER = '/app/data/'
IMG_UPLOAD_FOLDER = '/app/data/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'

# Logging
ENABLE_PROXY_FIX = True

PREVENT_UNSAFE_DB_CONNECTIONS = False

# Optional: Email configuration (for alerts)
# SMTP_HOST = 'localhost'
# SMTP_PORT = 587
# SMTP_STARTTLS = True
# SMTP_SSL = False
# SMTP_USER = 'your-email@example.com'
# SMTP_PASSWORD = 'your-password'
# SMTP_MAIL_FROM = 'your-email@example.com'