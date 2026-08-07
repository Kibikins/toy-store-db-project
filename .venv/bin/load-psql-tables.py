import os
import pandas as pd
from sqlalchemy import create_engine

# Create a connection to the database
engine = create_engine('postgresql://nakiasmith@localhost:5432/toydb') 

# Folder file path
csv_folder = '/Users/nakiasmith/Downloads/Maven+Fuzzy+Factory/'

# Loop through all CSV files in the folder
for file in os.listdir(csv_folder):
    if file.endswith('.csv'):
        file_path = os.path.join(csv_folder, file)
        
        # Table name defaults to the file name without extension
        table_name = os.path.splitext(file)[0].lower()
        
        # Read CSV data into a DataFrame
        df = pd.read_csv(file_path)
        
        # Load into database (creates table if it doesn't exist)
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"Successfully loaded {file} into table '{table_name}'")