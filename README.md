# Cryptocurrency Live Data Ingestion, ETL, and Dashboarding

## Project Overview
This project focuses on live data ingestion, ETL (Extract, Transform, Load), and dashboarding for cryptocurrency data. Utilizing Python and Google Cloud Platform (GCP) tools such as BigQuery, Looker, and Google Cloud Storage (GCS), I have built a seamless data pipeline and insightful dashboards. The goal is to provide real-time analytics and visualization for cryptocurrency market trends, price movements, and trading volumes. The Python scripts are scheduled to run on a GCP Compute Engine VM to ensure continuous data processing.

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
- Required Python libraries: `pandas`, `google-cloud-bigquery`, `google-cloud-storage`, `requests`

### Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/RahulGupta16/Real-Time-Cryptocurrency-Data-Collection-and-Dashboarding.git
    cd Real-Time-Cryptocurrency-Data-Collection-and-Dashboarding
    ```

2. Install the required Python libraries.

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
- `Crypto_Data_Ingestion.py`: This script fetches real-time cryptocurrency data. The data is extracted and transformed, then ingested into BigQuery. The script is scheduled to run on a GCP Compute Engine VM using cron jobs to perform regular ETL tasks.
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
- `Crypto_Data_Ingestion.py`: This script performs the ETL operations.
- Steps:
  1. **Extract**: Fetch data from the ingestion layer.
  2. **Transform**: Clean and transform the data (e.g., handling missing values, data type conversions).
  3. **Load**: Load the transformed data into BigQuery.

## Data Storage
### Description
Google Cloud Storage (GCS) is used for secure and scalable storage of raw and processed data.

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
1. Run the data ingestion & ETL script:
    ```bash
    python3 Crypto_Data_Ingestion.py
    ```

2. Upload data to GCS (if needed).

3. Access the Looker dashboards to visualize the data.

## Conclusion
This project provides a comprehensive solution for real-time cryptocurrency data analysis. By leveraging Python and GCP tools, the data pipeline ensures efficient data processing, storage, and visualization. This empowers users to make informed, data-driven decisions in the fast-paced world of cryptocurrency trading.

Feel free to explore the code and adapt it to your specific needs. For any questions or contributions, please reach out or submit a pull request on the GitHub repository.

---
