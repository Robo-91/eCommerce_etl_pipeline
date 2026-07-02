import pandas as pd
from sqlalchemy import create_engine, text
from datetime import date
import yaml
from src.util.config_load import load_config, load_filepath

# Access YAML file for required configurations
yaml_config = load_filepath()

with open(yaml_config) as file:
    config = yaml.safe_load(file)

# Connect to data sources
# Read csv data source
customers_df = pd.read_csv(config['csv']['customers'])

# Connect to sql server
## Create required variables for SSMS connection
server = config['database']['server']
database = config['database']['database']
driver = config['database']['driver']
database_conn = f'mssql+pyodbc://@{server}/{database}?driver={driver}'

## Create connection via SQL alchemy
engine = create_engine(database_conn)
con = engine.connect()

# truncate staging table
truncate_query = "TRUNCATE TABLE Customers_Staging"
con.execute(text(truncate_query))

# load data
customers_df.to_sql(
    name = 'Customers_Staging',
    con = con,
    if_exists = 'append',
    index = False
)

# log results
log_data = {'row_count': [len(customers_df)], 'table_name': ['Customers_Staging'], 'load_date': [date.today()]}
log_data_df = pd.DataFrame(log_data)
log_data_df.to_sql(
    'LoadStagingTablesLog',
    con = con,
    if_exists = 'append',
    index = False
)

con.commit()
con.close()