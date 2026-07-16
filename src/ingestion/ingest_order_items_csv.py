import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
import yaml
from src.util.config_load import load_filepath

def ingest_order_items():
    # Access YAML file for required configurations
    yaml_config = load_filepath()

    with open(yaml_config) as file:
        config = yaml.safe_load(file)

    # Connect to data sources
    # Read csv data source
    order_items_df = pd.read_csv(config['csv']['order_items'])

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
    truncate_query = 'TRUNCATE TABLE Order_Items_Staging'
    con.execute(text(truncate_query))

    # load data
    order_items_df.to_sql(
        'Order_Items_Staging',
        con = con,
        if_exists = 'append',
        index = False
    )

    # log results
    log_data = {'row_count': [len(order_items_df)], 'table_name': ['Order_Items_Staging'], 'load_date': [date.today()]}
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