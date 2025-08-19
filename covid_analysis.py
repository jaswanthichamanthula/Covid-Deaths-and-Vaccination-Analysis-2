import pandas as pd
import matplotlib.pyplot as plt
import mysql.connector

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="yourpassword",
    database="covid_db"
)
cursor = db.cursor()

# Fetch deaths by country
cursor.execute("SELECT country, SUM(total_deaths) FROM covid_data GROUP BY country ORDER BY SUM(total_deaths) DESC LIMIT 10;")
deaths_data = cursor.fetchall()

# Convert to DataFrame
df = pd.DataFrame(deaths_data, columns=["Country", "Total Deaths"])

# Plot bar chart
plt.figure(figsize=(10,5))
plt.bar(df["Country"], df["Total Deaths"])
plt.title("Top 10 Countries by Covid Deaths")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
