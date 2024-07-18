import pandas as pd
import sqlalchemy
import os

def append_to_sql(dataset_path, connection_string, table_name):
    try:
        # Read the dataset
        df = pd.read_csv(dataset_path)
    except Exception as e:
        print(f"Error reading the dataset: {e}")
        return

    try:
        # Create a SQLAlchemy engine
        engine = sqlalchemy.create_engine(connection_string)

        with engine.connect() as connection:
            df.to_sql(table_name, con=connection, if_exists='append', index=False)
        
        print(f"Data appended to {table_name} successfully.")
    except Exception as e:
        print(f"Error appending data to the database: {e}")

if __name__ == "__main__":
    append_to_sql('your_dataset.csv', 'sqlite:///your_database.db', 'your_table_name')

