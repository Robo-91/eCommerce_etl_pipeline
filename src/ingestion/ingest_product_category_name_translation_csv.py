import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
import yaml
from src.util.config_load import load_filepath

def ingest_product_category_name_translation():

    # Access YAML file for required configurations
    yaml_config = load_filepath()

    with open(yaml_config) as file:
        config = yaml.safe_load(file)

    # Connect to data sources
    # Read csv data source
    product_category_name_translation_df = pd.read_csv(config['csv']['product_category_name_translation'])

    # Connect to SQL Server
    ## Create required variables for SSMS connection
    server = config['database']['server']
    database = config['database']['database']
    driver = config['database']['driver']
    database_conn = f'mssql+pyodbc://@{server}/{database}?driver={driver}'

    ## Create connection via SQL alchemy
    engine = create_engine(database_conn)
    con = engine.connect()

    # Truncate Staging Table
    truncate_query = 'TRUNCATE TABLE Product_Category_Name_Translation_Staging'
    con.execute(text(truncate_query))

    # load data
    product_category_name_translation_df.to_sql(
        'Product_Category_Name_Translation_Staging',
        con = con,
        if_exists = 'append',
        index = False
    )

    # log results
    log_data = {'row_count': [len(product_category_name_translation_df)], 'table_name': ['Product_Category_Name_Translation_Staging'], 'load_date': [date.today()]}
    log_data_df = pd.DataFrame(log_data)
    log_data_df.to_sql(
        name = 'LoadStagingTablesLog',
        con = con,
        if_exists = 'append',
        index = False
    )

    # Commit changes and close connection
    con.commit()
    con.close()