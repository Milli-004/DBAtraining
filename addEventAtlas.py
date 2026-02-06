from pymongo import MongoClient       #to establish cluster connection

client = MongoClient("mongodb+srv://srivastavasudhir456_db_user:RfJpiIFvzbHPYMrM@cluster0.z6veqku.mongodb.net/?appName=Cluster0")

eventdb = client["eventdb"]     # database name

#create add event collection using database
addevent = eventdb["addevent"]

#insert the event using collection
#addevent.insert_one({"eventname" :"tedx",
                     #"venue":"bareilly",
                     #"date":"22 feb 26"})


# addevent.insert_many([{"eventname" :"invertia",
#                      "venue":"bareilly",
#                      "date":"14 feb 26"},
#                      {"eventname" :"Bootcamp",
#                      "venue":"bareilly",
#                      "date":"22 feb 26"}])

# addevent.delete_one({"eventname":"tedx"})

# addevent.update_one({'eventname':"invertia"},{'$set':{'date':'22 feb 2026'}})

#fetch the events
for event in addevent.find():
    print(event)

