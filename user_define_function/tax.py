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


with open('tax.js') as file:
    file_contents = file.read()
udf_definition = {
    'id': 'Tax',
    'serverScript': file_contents,
}
client = cosmos_client.CosmosClient(url, key)
database = client.get_database_client(database_name)
container = database.get_container_client(container_name)
udf = container.scripts.create_user_defined_function(udf_definit)
