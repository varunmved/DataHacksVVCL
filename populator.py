"""
    populator.py

    load our datasets into postgres
"""
import csv
import pdb
import database.dbutils as dbutils

evictions_fin = open("cleaned-data/cleaned-sf-eviction-notices.csv", "r")
business_fin = open("cleaned-data/cleaned-sf-businesses.csv", "r")

db_conn = dbutils.PostgresConn("postgres") 

# upload evictions data
eviction_data = csv.DictReader(evictions_fin)

# upload business data
business_data = csv.DictReader(business_fin)

# for datum in business_data:
#     print "%s -> %s" % (business_data.line_num, datum["business_name"]) 
#     db_conn.insert("sf_businesses", [datum])

for datum in eviction_data:
    print "%s -> %s" % (eviction_data.line_num, datum["eviction_id"])
    db_conn.insert("sf_evictions", [datum])
    







db_conn.disconnect()
evictions_fin.close()
business_fin.close()
