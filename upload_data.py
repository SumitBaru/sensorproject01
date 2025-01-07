from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
url= "mongodb+srv://sumit:12345@cluster0.r2tc3.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(url)

DATABASE_NAME = "pwskills"
COLLECTION_NAME = "waferfault"

df = pd.read_csv("C:\sensorproject\notebooks\wafer_23012020_041211.csv")

df=df.drop("Unnamed: 0", axis=1)


json_record = list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)

