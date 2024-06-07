# Cryptocurrency Live Data Ingestion, ETL, and Dashboarding

## Project Overview
This project focuses on live data ingestion, ETL (Extract, Transform, Load), and dashboarding for cryptocurrency data. Utilizing Python and Google Cloud Platform (GCP) tools such as BigQuery, Looker, and Google Cloud Storage (GCS), I have built a seamless data pipeline and insightful dashboards. The goal is to provide real-time analytics and visualization for cryptocurrency market trends, price movements, and trading volumes.

## Table of Contents
1. [Project Setup](#project-setup)
2. [Data Ingestion](#data-ingestion)
3. [ETL Process](#etl-process)
4. [Data Storage](#data-storage)
5. [Dashboarding](#dashboarding)
6. [Usage](#usage)
7. [Conclusion](#conclusion)

## Project Setup
### Prerequisites
- Python 3.x
- Google Cloud Platform account
- BigQuery, Looker, and GCS services enabled
- Required Python libraries: `pandas`, `google-cloud-bigquery`, `google-cloud-storage`, `requests`, `sqlalchemy`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crypto-data-pipeline.git
    cd crypto-data-pipeline
    ```

2. Install the required Python libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up GCP credentials:
    - Create a service account and download the JSON key file.
    - Set the environment variable for authentication:
      ```bash
      export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
      ```

## Data Ingestion
### Description
The data ingestion component involves collecting real-time data from various cryptocurrency exchanges. This is achieved through APIs provided by the exchanges.

### Implementation
- `data_ingestion.py`: This script fetches real-time cryptocurrency data and stores it temporarily for the ETL process.
- Example API usage:
    ```python
    import requests

    response = requests.get('https://api.exchange.com/v1/ticker')
    data = response.json()
    ```

## ETL Process
### Description
The ETL process involves extracting data, transforming it to a suitable format, and loading it into BigQuery for analysis.

### Implementation
- `etl_process.py`: This script performs the ETL operations.
- Steps:
  1. **Extract**: Fetch data from the ingestion layer.
  2. **Transform**: Clean and transform the data (e.g., handling missing values, data type conversions).
  3. **Load**: Load the transformed data into BigQuery.

### Sample Code
```python
import pandas as pd
from google.cloud import bigquery

# Extract
data = pd.read_json('data/temp_data.json')

# Transform
data_cleaned = data.dropna()

# Load
client = bigquery.Client()
dataset_ref = client.dataset('crypto_data')
table_ref = dataset_ref.table('prices')
job = client.load_table_from_dataframe(data_cleaned, table_ref)
job.result()
```

## Data Storage
### Description
Google Cloud Storage (GCS) is used for secure and scalable storage of raw and processed data.

### Implementation
- `storage_manager.py`: This script handles the upload and retrieval of data from GCS.
- Example:
    ```python
    from google.cloud import storage

    client = storage.Client()
    bucket = client.get_bucket('your-bucket-name')
    blob = bucket.blob('data/raw_data.json')
    blob.upload_from_filename('data/raw_data.json')
    ```

## Dashboarding
### Description
Looker is used to create interactive and dynamic dashboards that provide insights into cryptocurrency market trends, price movements, and trading volumes.

### Implementation
- Set up Looker with BigQuery as the data source.
- Create visualizations and dashboards to analyze the data.

### Sample Dashboard Elements
- Line charts for price movements over time.
- Bar charts for trading volumes by exchange.
- Heatmaps for price correlations between different cryptocurrencies.

## Usage
### Running the Pipeline
1. Run the data ingestion script:
    ```bash
    python data_ingestion.py
    ```

2. Run the ETL process:
    ```bash
    python3 crypto_code.py
    ```

3. Upload data to GCS (if needed):
    ```bash
    python storage_manager.py
    ```

4. Access the Looker dashboards to visualize the data.

## Conclusion
This project provides a comprehensive solution for real-time cryptocurrency data analysis. By leveraging Python and GCP tools, the data pipeline ensures efficient data processing, storage, and visualization. This empowers users to make informed, data-driven decisions in the fast-paced world of cryptocurrency trading.

Feel free to explore the code and adapt it to your specific needs. For any questions or contributions, please reach out or submit a pull request on the GitHub repository.

---
