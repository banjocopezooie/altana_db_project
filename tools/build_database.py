"""
Takes the input CSV file and builds a Sqlite database from the input.
"""

import os
import sys
import sqlite3
import pandas as pd

"""
Converting the CSV File to a Sqlite database file
"""
def populate_database(input_csv_file, chunk_size):
    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_file = base_dir + "/../data/DB_ReceitaFederal_QuadroSocietario.db"

    print("Removing old database files.")
    if os.path.exists(db_file):
        os.remove(db_file)

    conn = sqlite3.connect(db_file)

    print("Populating database...")
    for data_chunk in pd.read_csv(input_csv_file, delimiter="\t", chunksize=chunk_size):
        data_chunk.to_sql("brz_companies", conn, index=False, if_exists="append")

    # Closing the connection
    conn.close()
    print("The sql database file was populated. \n")



def main():
    print("Starting to Build the Database.")
    input_csv_file = sys.argv[1]
    populate_database(input_csv_file, 10000)


if __name__ == "__main__":
    main()
