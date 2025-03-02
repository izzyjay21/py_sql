import sqlite3

database= "database.sqlite"
conn = sqlite3.connect(database)

print("marked")


import pandas as pd


tables =pd.read_sql("""
             SELECT * FROM sqlite_master  WHERE type ="table";
""",conn)

print(tables)


country =pd.read_sql("SELECT * FROM COUNTRY;",conn)
print(country)

country_name = pd.read_sql("""
                      SELECT * FROM Country WHERE Country_name = "U.A.E";
""",conn)
 
print(country_name)


country_id = pd.read_sql("""
          SELECT * FROM Country WHERE Country_id ==8
""",conn)

print(country_id)

min_max = pd.read_sql("""
              SELECT MIN(Country_id), MAX(Country_id) FROM Country;
""",conn)

print(min_max)


like = pd.read_sql("""
 SELECT * FROM Country WHERE Country_Name LIKE "india";

""",conn)

print(like)