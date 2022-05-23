import os
import sys
import sqlite3
import pandas as pd
from tools.build_database import *
from services.query_database import *


def main():
    print("The project is starting!")
    print("Starting to Build the Database.")
    input_csv_file = sys.argv[1]
    populate_database(input_csv_file, 10000)

    base_dir = os.path.abspath(os.path.dirname(__file__))
    db_file = base_dir + "/data/DB_ReceitaFederal_QuadroSocietario.db"
    conn = sqlite3.connect(db_file)
    cur = conn.cursor()

    #Querying Database
    associated_operators_for_company(conn, cur, "29208510000130")
    associated_operators_for_company(conn, cur, "28433541000122")
    associated_operators_for_company(conn, cur, "17201986000160")

    associated_companies_for_operator(conn, cur, "SANDRO MARCOS MANIERO")
    associated_companies_for_operator(conn, cur, "POSTO DE COMBUSTIVEL P1 LTDA")

    print("Third Query:")
    connected_companies_for_operator(conn, cur, "29208510000130")

    #Close Connection
    conn.close()


if __name__ == "__main__":
    main()