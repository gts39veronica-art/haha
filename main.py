import sqlite3

conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

query_1 = """
    SELECT d.name, MAX(m.release_date)
    FROM directors
    JOIN movies m ON d.id = m.director_id)
    GROUP BY d.id, d.name;
    """

print("Result of problem 1:")
cursor.execute(query_1)
for row in cursor.fetchall():
    print(f"Receiver: {row[0]}, last film: {row[1]}")
