import psycopg2

DB_PARAMS = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "bouncym2025",
    "host": "127.0.0.1",
    "port": "5432"
}

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

cur.execute('SELECT "Coet ID" FROM "Coets Android appended" WHERE last_reviewed IS NOT NULL ORDER BY last_reviewed')
results = cur.fetchall()

print("Reviewed Coet IDs:")
for r in results:
    print(r[0])

cur.close()
conn.close()
