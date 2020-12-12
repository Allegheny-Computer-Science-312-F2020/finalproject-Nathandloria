from pymongo import MongoClient
import csv
import string
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient('localhost:27017')
db = client.countries_db

col = db.Country

bten = list()
tten = list()

doc = col.find({ "GDP" : { "$ne" : "" }, "Debt_external" : { "$ne" : "" } }, { "_id" : 0, "Country" : 1, "GDP" : 1, "Debt_external" : 1 })

for el in doc.sort("GDP", -1).limit(10):
    tten.append(el['Debt_external'] / el['GDP'])

doc = col.find({ "GDP" : { "$ne" : "" }, "Debt_external" : { "$ne" : "" } }, { "_id" : 0, "Country" : 1, "GDP" : 1, "Debt_external" : 1 })

for el in doc.sort("GDP", 1).limit(10):
    bten.append(el['Debt_external'] / el['GDP'])

rat = 0.0
for el in tten:
    rat += el

tavg = rat / len(tten)

rat = 0.0
for el in bten:
    rat += el

bavg = rat / len(bten)

print(f"Ratio of GDP to external debt (top 10): {tavg}")
print(f"Ratio of GDP to external debt (bottom 10): {bavg}")
# db.Country.find({ "Electricity_consumption" : { $ne : "" }, "Natural_gas_production" : { $ne : "" }},{ "Electricity_consumption":1, "Natural_gas_production":1 })
