import os
import uuid
from pprint import pprint

from azure.cosmos import CosmosClient


ENDOPINT = os.environ["ENDPOINT"]
KEY = os.environ["KEY"]
COSMOS_CLIENT = CosmosClient(ENDOPINT, KEY)
COSMOS_DATABASE = COSMOS_CLIENT.get_database_client("prueba-db2")
COSMOS_CONTAINER = COSMOS_DATABASE.get_container_client("prueba-contenedor")

elemento_nuevo = {
    "gender": "female",
    "name": {
        "title": "Sr.",
        "first": "Testing",
        "last": "Tester",
    },
    "location": {
        "street": {
            "number": 123456,
            "name": "AAAAAA",
        },
        "city": "Mexico City",
        "state": "Mexico",
        "country": "Mexico",
        "postcode": 93701,
        "coordinates": {
            "latitude": "-24.7920",
            "longitude": "-96.6822",
        },
        "timezone": {
            "offset": "+5:45",
            "description": "Kathmandu",
        },
    },
    "email": "testing.test@example.com",
    "login": {
        "uuid": "5fcfb203-407b-4821-a274-8a0e8ccc1d56",
        "username": "usuarioprueba",
        "password": "12345",
        "salt": "AgeefG",
        "md5": "8bb6843c0ec905af768920ceb6d330e7",
        "sha1": "b0f2cc995cc76f91a74bb5c8f75cbed81f4d238f",
        "sha256": "1ca3954812193873cc86a39b004c2a092253ebba557e77d0ebbd3f28f2dd1fa0",
    },
    "dob": {
        "date": "1990-01-15T05:00:25.167Z",
        "age": 25,
    },
    "registered": {
        "date": "1990-01-15T05:00:25.167Z",
        "age": 25,
    },
    "phone": "06-878-183",
    "cell": "043-921-84-13",
    "id": str(uuid.uuid4()),
    "picture": {
        "large": "https://randomuser.me/api/portraits/men/87.jpg",
        "medium": "https://randomuser.me/api/portraits/med/men/87.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/men/87.jpg",
    },
    "nat": "FI",
    "_rid": "dyBCAPwyGPsBAAAAAAAAAA==",
    "_self": "dbs/dyBCAA==/colls/dyBCAPwyGPs=/docs/dyBCAPwyGPsBAAAAAAAAAA==/",
    "_etag": '"870365a3-0000-0700-0000-62e456c20000"',
    "_attachments": "attachments/",
    "_ts": 1659131586,
}

COSMOS_CONTAINER.create_item(body=elemento_nuevo)
results = COSMOS_CONTAINER.query_items(query="SELECT * FROM c", enable_cross_partition_query=True)

for result in results:
    pprint(result)
    input()
