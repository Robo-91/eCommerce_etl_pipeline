from src.ingestion.ingest_order_reviews_csv import ingest_order_reviews
from src.ingestion.ingest_orders_csv import ingest_orders

def ingestion_job() :
    ingest_order_reviews()
    ingest_orders()

ingestion_job()
