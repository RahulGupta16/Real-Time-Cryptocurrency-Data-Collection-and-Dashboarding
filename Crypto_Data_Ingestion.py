import pandas as pd
from datetime import datetime
import requests
import time
from google.cloud import bigquery
import os 
from google.cloud.exceptions import NotFound

credential_path = 'ENTER VALID JSON CREDENTIAL FROM GCP'
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
client = bigquery.Client()
table_id = "work-397019.dataset.Dumped_Data"

df = pd.DataFrame()
num_records = 0
while (num_records>=0):
    response = requests.get(r"ENTER VALID WAZIRX API KEY")
    x = pd.DataFrame(response.json())
    x = x[x.quoteAsset == 'inr']
    x['high-low_diff'] = (x.highPrice.astype('float') - x.lowPrice.astype('float'))*100/x.lowPrice.astype('float')
    x['high-last_diff'] = (x.highPrice.astype('float') - x.lastPrice.astype('float'))*100/x.lastPrice.astype('float')
    x['low-last_diff'] = (x.lowPrice.astype('float') - x.lastPrice.astype('float'))*100/x.lastPrice.astype('float')
    x['open-last_diff'] = (x.openPrice.astype('float') - x.lastPrice.astype('float'))*100/x.lastPrice.astype('float')
    x['Spread'] = x.askPrice.astype('float') - x.bidPrice.astype('float')
    df = pd.concat([df,x],axis = 0)
    num_records = num_records -1
    time.sleep(1)

df.reset_index(drop=True, inplace=True)
df.at = df['at'].apply(lambda x: datetime.fromtimestamp(int(str(x)[0:-3])))#.strftime('%c')))
try:
    client.get_table(table_id)
except NotFound:
    schema = [
        bigquery.SchemaField("symbol", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("baseAsset", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("quoteAsset", "STRING", mode="NULLABLE"),
        bigquery.SchemaField("openPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("lowPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("highPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("lastPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("volume", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("bidPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("askPrice", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("at", "DATETIME", mode="NULLABLE"),
        bigquery.SchemaField("high-low_diff", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("high-last_diff", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("low-last_diff", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("open-last_diff", "FLOAT", mode="NULLABLE"),
        bigquery.SchemaField("Spread", "FLOAT", mode="NULLABLE")
    ]
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  

job_config = bigquery.LoadJobConfig(
    source_format = bigquery.SourceFormat.CSV, skip_leading_rows=1, autodetect=False,write_disposition = bigquery.WriteDisposition.WRITE_APPEND,
    )

job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
job.result() 
table_2 = client.get_table(table_id)  
print(table_2.schema)
print("Total records as of {}: {}\nTotal size (in bytes): {}".format(time.ctime(time.time()),table_2.num_rows, str(table_2.num_bytes) + ' bytes'))