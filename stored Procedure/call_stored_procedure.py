import uuid
from decouple import config
import azure.cosmos.cosmos_client as cosmos_client

new_id = str(uuid.uuid4())
url = config('ACCOUNT_URI')
key = config('ACCOUNT_KEY')
database_name = 'nutriationDatabase'
container_name = 'foodcollection'
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)

# Creating a document for a container with "id" as a partition key.

with open('create_stored.js') as file:
    file_contents = file.read()

sproc = {
    'id': 'to',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
created_sproc = container.scripts.create_stored_procedure(body=sproc)

result = container.scripts.execute_stored_procedure(
    sproc=created_sproc, params='ranjit', partition_key='example')
