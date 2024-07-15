import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def conf_aws_acesso():
    return boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        aws_session_token=os.getenv('AWS_SESSION_TOKEN'),
        region_name=os.getenv('AWS_DEFAULT_REGION')
)

acesso = conf_aws_acesso()

s3 = acesso.resource('s3')

bucket_name = 'data-lake-do-matheus'
bucket = s3.Bucket(bucket_name)

arquivo1 = 'movies.csv'
arquivo2 = 'series.csv'

pasta_movies = 'Raw/Local/CSV/Movies/2024-07-11/'
pasta_series = 'Raw/Local/CSV/Series/2024-07-11/'

bucket.upload_file(arquivo1, f"{pasta_movies}{arquivo1}")
bucket.upload_file(arquivo2, f"{pasta_series}{arquivo2}")


