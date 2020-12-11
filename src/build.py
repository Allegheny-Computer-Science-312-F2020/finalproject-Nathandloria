from pymongo import MongoClient
import csv
import string

client = MongoClient('localhost:27017')
client.drop_database('countries_db')
db = client.countries_db

col = db.Country

try:
    x = list()
    cnt = 0

    with open('data/countries.csv', 'r') as csvfile:
        for el in csvfile:
            if cnt == 0:
                x = el.split(',')
            else:
                row = {}
                for i in range(len(el.split(','))):
                    try:
                        row[x[i].strip('\n')] = float(el.split(',')[i].strip('\n'))
                    except:
                        row[x[i].strip('\n')] = el.split(',')[i].strip('\n')

                col.insert_one(row)

            cnt += 1

        print('Data inserted')

    for r in col.find():
        print(r)

except Exception as x:
    print(x)
