from pymongo import MongoClient
import csv
import string
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient('localhost:27017')
db = client.countries_db

col = db.Country
doc = col.find({ "Electricity_consumption" : { "$ne" : "" }, "Natural_gas_production" : { "$ne" : "" }}, { "_id": 0, "Electricity_consumption": 1, "Natural_gas_production": 1 })

e_consumption = list()
ng_production = list()
for el in doc:
    if el['Electricity_consumption'] != '' and el['Natural_gas_production'] != '':
        e_consumption.append(float(el['Electricity_consumption']))
        ng_production.append(float(el['Natural_gas_production']))

plt.plot(ng_production, e_consumption, 'o', color='black')
plt.plot(np.unique(ng_production), np.poly1d(np.polyfit(ng_production, e_consumption, 1))(np.unique(ng_production)))

plt.ylabel('Electricity Consumption (kWh)')
plt.xlabel('Natural Gas Production (cu m)')

plt.savefig('q_2.png')













# db.Country.find({ "Electricity_consumption" : { $ne : "" }, "Natural_gas_production" : { $ne : "" }},{ "Electricity_consumption":1, "Natural_gas_production":1 })
