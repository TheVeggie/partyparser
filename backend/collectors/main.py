from pymongo import MongoClient
import datetime

client = MongoClient('localhost', 27017)

db = client['parties']

afd_collection = db['afd']
union_collection = db['union']
linke_collection = db['linke']
spd_collection = db['spd']
fdp_collection = db['fdp']

