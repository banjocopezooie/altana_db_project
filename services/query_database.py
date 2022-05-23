"""
This file contains the functions to query the database
"""

import os
import sys
import sqlite3

"""
Query the database for all operators associated with a given company
"""
def associated_operators_for_company(conn, cur, company_id):
    print("\n Assocaited Operators for Company ID: " + company_id)
    list_results = []
    results = cur.execute("select nm_socio from brz_companies where nr_cnpj='%s'" % company_id)
    for row in results:
        list_results.append(row)

    if len(list_results) == 0:
        print("No results found for query. \n")
    else:
        print(list_results)

"""
Query the database for all companies associated with given operator
"""
def associated_companies_for_operator(conn, cur, operator_name):
    print("\n Associated Companies for Operater Name: " + operator_name)
    list_results = []
    results = cur.execute("select nr_cnpj,nm_fantasia "
                          "from brz_companies where nm_socio='%s'" % operator_name)
    for row in results:
        list_results.append(row)

    if len(list_results) == 0:
        print("No results found for query. \n")
    else:
        print(list_results)


"""
Query the database for all companies connected to a given company via shared operators
"""
def connected_companies_for_operator(conn, cur, company_id):
    print("\n Companies connected to shared operators for Company ID: " + company_id)
    list_results = []
    results = cur.execute("select nr_cnpj, nm_fantasia, nm_socio from brz_companies "
                          "where nm_socio in (select nm_socio from brz_companies where nr_cnpj='%s') "
                          "and not nr_cnpj='%s' order by nm_socio desc" % (company_id, company_id))

    for row in results:
        list_results.append(row)

    if len(list_results) == 0:
        print("No results found for query. \n")
    else:
        print(list_results)

