from pymongo import MongoClient
import csv
import string
import matplotlib.pyplot as plt
import numpy as np

client = MongoClient('localhost:27017')
db = client.countries_db

col = db.Country
doc = col.find({ "Railways" : { "$ne" : "" }, "Highways" : { "$ne" : "" } },{ "_id" : 0, "Railways" : 1, "Highways" : 1 })

rw = list()
rhw = list()
for el in doc:
    if el['Railways'] != '' and el['Highways'] != '':
        rw.append(float(el['Railways']))
        rhw.append(float(el['Railways']) / float(el['Highways']))

plt.plot(rw, rhw, 'o', color='black')
plt.plot(np.unique(rw), np.poly1d(np.polyfit(rw, rhw, 1))(np.unique(rw)))

plt.xlabel('Railways (km)')
plt.ylabel('Railways / Highways')

plt.savefig('q_3.png')













# db.Country.find({ "Electricity_consumption" : { $ne : "" }, "Natural_gas_production" : { $ne : "" }},{ "Electricity_consumption":1, "Natural_gas_production":1 })
