from src.ingestion.ingest_customers_csv import ingest_customers
from src.ingestion.ingest_geolocation_csv import ingest_geolocations
from src.ingestion.ingest_order_items_csv import ingest_order_items
from src.ingestion.ingest_order_payments_csv import ingest_order_payments
from src.ingestion.ingest_order_reviews_csv import ingest_order_reviews
from src.ingestion.ingest_orders_csv import ingest_orders
from src.ingestion.ingest_product_category_name_translation_csv import ingest_product_category_name_translation
from src.ingestion.ingest_products_csv import ingest_products
from src.ingestion.ingest_sellers_csv import ingest_sellers

def ingestion_job() :
    ingest_customers()
    ingest_geolocations()
    ingest_order_items()
    ingest_order_payments()
    ingest_order_reviews()
    ingest_orders()
    ingest_product_category_name_translation()
    ingest_products()
    ingest_sellers()

ingestion_job()
