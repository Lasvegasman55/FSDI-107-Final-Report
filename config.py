import pymongo
import certifi

con_string = mongodb+srv://coolcatt28:<db_coolcatt28>@cluster0.kldjr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
client = pymango.MangoClient(con_string, tlsCaFile = certif.where())
db = client.get_database("Tacos")