import dbutils

db_conn = dbutils.PostgresConn("postgres")
query = "select now() as current_time"
results, colnames = db_conn.executeReadQueryHash(query)

for result in results:
    print results


