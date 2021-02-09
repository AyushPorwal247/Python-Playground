#Importing a module named mysql.connector
import mysql.connector

#Making a connection with a database with given credentials
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database",
)

#Navigating through database 
cursor = con.cursor()

#Reading data from the database
query = cursor.execute("SELECT * FROM Dictionary")

#Fetching data from database
results = cursor.fetchall()
print(results)