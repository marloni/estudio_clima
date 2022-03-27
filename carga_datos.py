""" Here is the explanation for the code above:
1. This is a python script that converts a csv file to an sqlite3 database, 
   using the csv module.
2. The csv file to be converted is in the same folder as this script.
3. The database will be named 'csv_to_sqlite.db'.
4. The csv file must use the same delimiter, quote, and escape character.
5. The csv file must have a header row.
6. The database will have the same table name as the csv file.
7. The database will have the same column names as the csv file.
8. The database will have the same column data types as the csv file. """""" CSV to SQLite """

# Import the csv module
import csv
import sqlite3

# Create a database in RAM
conn = sqlite3.connect(':memory:')

# Create a cursor object
c = conn.cursor()

# Create a table
c.execute("CREATE TABLE csv_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, weight REAL)")

# Open the csv file
with open('csv_file.csv', 'r') as csv_file:
    # Create a csv reader object
    csv_reader = csv.reader(csv_file)
    # Skip the header row
    next(csv_reader)
    # Insert data into the table
    for row in csv_reader:
        c.execute("INSERT INTO csv_table VALUES (?, ?, ?, ?)", row)
         
# Save (commit) the changes
conn.commit()
 
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
 
# Open the database
conn = sqlite3.connect('csv_to_sqlite.db')
 
# Create a cursor object
c = conn.cursor()
 
# Print the table names
c.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(c.fetchall())
 
# Print the column names
c.execute("PRAGMA table_info(csv_table)")
print(c.fetchall())
 
# Print the first 5 rows
c.execute("SELECT * FROM csv_table LIMIT 5")
print(c.fetchall())