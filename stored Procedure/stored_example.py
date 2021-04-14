import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import js2py


url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
database_name = 'testDatabase'
container_name = 'products'

import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import js2py


url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
database_name = 'testDatabase'
container_name = 'products'

with open('create_stored.js') as file:
    file_contents = file.read()

sproc = {
    'id': 'spCreateToDoItem',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
created_sproc = container.scripts.create_stored_procedure(body=sproc)
import azure.cosmos.cosmos_client as cosmos_client
from decouple import config
import js2py


url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
database_name = 'testDatabase'
container_name = 'products'

with open('create_stored.js') as file:
    file_contents = file.read()

sproc = {
    'id': 'spCreateToDoItem',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
created_sproc = container.scripts.create_stored_procedure(body=sproc)
