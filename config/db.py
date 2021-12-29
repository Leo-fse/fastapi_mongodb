# Authentication Examples
# https://pymongo.readthedocs.io/en/stable/examples/authentication.html

import urllib.parse

from pymongo import MongoClient

host = "localhost"
port = 27017
username = urllib.parse.quote_plus("username")
password = urllib.parse.quote("password")
authSource = "admin"
authMechanism = "SCRAM-SHA-256"

conn = MongoClient(
    host=host,
    port=port,
    usename=username,
    password=password,
    authSource=authSource,
    authMechamism="SCRAM-SHA-256",
)

uri = (
    f"mongodb://{username}:{password}@{host}/"
    f"?authSource={authSource}&authMechanism={authMechanism}"
)

conn2 = MongoClient(uri)
