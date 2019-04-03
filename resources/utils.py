import os
import csv
from pymongo import MongoClient
import os.path
from models.addresses import AddressModel


def mongo_loader():
    my_path = os.path.abspath(os.path.dirname(__file__))
    localities_path = os.path.join(my_path, "../data/localities_full.csv")

    ## Set up DB Connection
    mongo_uri = os.environ.get("MONGO_URI")
    mongo_db = os.environ.get("MONGO_DBNAME")

    client = MongoClient(mongo_uri)
    db = client[mongo_db]
    geocodes = db["geocodes"]

    ## Read CSV  file
    csvfile = open(localities_path, 'r')
    reader = csv.DictReader(csvfile)
    header = ["X", "Y", "county", "townland"]

    ## Upload to DB
    for each in reader:
        row = {}
        for field in header:
            row[field] = each[field]

        geocodes.insert_one(row)


def sql_loader(addresses):
    for element in addresses:
        new_address = AddressModel(county=element['county'], address=element['townland'], longitude=element['X'],
                                   latitude=element['Y'])
        new_address.save_to_db()


county_list = ['Carlow', 'Cavan', 'Clare', 'Cork', 'Donegal', 'Dublin', 'Galway', 'Kerry', 'Kildare','Kilkenny', 'Laois',
            'Leitrim', 'Limerick', 'Longford', 'Louth', 'Mayo', 'Meath','Monaghan', 'Offaly','Roscommon', 'Sligo',
            'Tipperary', 'Waterford', 'Westmeath', 'Wexford', 'Wicklow']
