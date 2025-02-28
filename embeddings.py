### Trying to connect to GCP embeddings-438000 project
from dotenv import load_dotenv
import os
from google.cloud import bigquery
import pandas as pd
from google.cloud import bigquery
import sys


load_dotenv()
key = os.getenv("API_KEY")
project_id = os.getenv("project")
location = os.getenv("location")

#generate a unique id for this session
#from datetime import datetime
#UID = datetime.now().strftime("%m%d%H%M")

#Load the BigQuery table into a pandas dataframe
QUESTIONS_SIZE = 1000
bq_client = bigquery.Client(project=project_id)
QUERY_TEMPLATE = """
                SELECT distinct q.id, q.title
                FROM (SELECT * FROM `bigquery-public-data.stackoverflow.posts_questions`
                WHERE Score > 0 ORDER BY View_Count desc) AS q
                LIMIT {limit};
                """
query = QUERY_TEMPLATE.format(limit=QUESTIONS_SIZE)
query_job = bq_client.query(query)
rows = query_job.result()
df = rows.to_dataframe()

df.head()