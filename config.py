import pymongo
import certifi
import os  # Added for environment variables

# Better to get connection string from environment variable
con_string = "mongodb+srv://coolcatt28:<db_coolcatt28>@cluster0.kldjr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = pymongo.MongoClient(con_string, tlsCAFile=certifi.where())
db = client.get_database("Tacos")