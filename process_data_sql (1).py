import pandas as pd
import sqlalchemy

def fetch_and_clean_data(connection_string, table_name, cleaned_table_name):
    try:
        # Create a SQLAlchemy engine
        engine = sqlalchemy.create_engine(connection_string)

        # Fetch the data from the table
        with engine.connect() as connection:
            df = pd.read_sql_table(table_name, con=connection)

        # Perform data cleaning
        df.dropna(inplace=True)  
 

        # Handle outliers (Z-score method)
        from scipy.stats import zscore
        numeric_cols = df.select_dtypes(include=['number']).columns
        df = df[(zscore(df[numeric_cols]) < 5).all(axis=1)]

        # Append cleaned data back to the SQL table
        with engine.connect() as connection:
            df.to_sql(cleaned_table_name, con=connection, if_exists='append', index=False)

        print(f"Cleaned data appended to {cleaned_table_name} successfully.")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    fetch_and_clean_data(connection_string, table_name, cleaned_table_name)
