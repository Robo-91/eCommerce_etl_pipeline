from src.ingestion.ingest_order_reviews_csv import ingest_order_reviews
from src.ingestion.ingest_orders_csv import ingest_orders
from src.ingestion.ingest_product_category_name_translation_csv import ingest_product_category_name_translation

def ingestion_job() :
    ingest_order_reviews()
    ingest_orders()
    ingest_product_category_name_translation()

ingestion_job()
