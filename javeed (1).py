import ibmiotf.application
import ibmiotf.device
import random
import json
import time
import json
import wiotp.sdk.device
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result
from cloudant.result import Result, ResultByKey


# IBM Cloudant Legacy authentication
client = Cloudant("apikey-v2-26cvscqymokovdj7rs2u5j0twv2ogcs0x7ewms4tww3a", "a161324b37fc53e709f38f4bc1ee5881",
                  url="https://apikey-v2-26cvscqymokovdj7rs2u5j0twv2ogcs0x7ewms4tww3a:a161324b37fc53e709f38f4bc1ee5881@2a771bbb-85a9-44ca-acb4-2b418ff3ab10-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()

database_name = "javeed16"

my_database = client.create_database(database_name)

if my_database.exists():
    print(f"'{database_name}' successfully created.")
    json_document = {
                    "_id": "1001",
                    "name":"javeed"
                    }
    new_document = my_database.create_document(json_document)
    if new_document.exists():
        print("Document '{new_document}' successfully created.")

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']  #search by id, if id=1001   

print("---------------")
print("the data with id =1001 is")
print (result)
print("---------------")
# Iterate over the result collection
for result in result_collection:
    print(result)# it will print all the records

# First retrieve the document
for document in my_database:
    my_document = my_database['1001'] 

# Update the document content
# This can be done as you would any other dictionary
my_document['temperature'] = 60
my_document['pulserate'] = 60


myConfig = {
    "identity": {
        "orgId": "hb0cnz",
        "typeId": "iotdevice",
        "deviceId": "1001"
    },
    "auth": {
        "token": "1234567890"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()

while True:
        
        latitude= 17.3850
        longitude= 78.4867

        #out area location

        #latitude= 17.4219272
        #longitude= 78.5488783
        myData={'lat':latitude,'lon':longitude}
        client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
        print("Data published to IBM IoT platform: ",myData)
        time.sleep(5)
client.disconnect()

# You must save the document in order to update it on the database
my_document.save()

result_collection = Result(my_database.all_docs, include_docs=True)
# Get the result for matching a key
result = result_collection['1001']     
# Iterate over the result collection
print (result)



