import os
import ssl
import socket
from getpass import getpass
from urllib.parse import urlparse

import certifi
import pymongo
from pymongo.errors import PyMongoError


def main():
    uri = os.getenv("MONGODB_URL") or getpass("Paste MongoDB URI: ")
    parsed = urlparse(uri)
    host = parsed.hostname

    print("Python:", os.sys.version.split()[0])
    print("OpenSSL:", ssl.OPENSSL_VERSION)
    print("PyMongo:", pymongo.version)
    print("certifi:", certifi.where())
    print("URI host:", host)

    client = pymongo.MongoClient(
        uri,
        tls=True,
        tlsCAFile=certifi.where(),
        connectTimeoutMS=20000,
        socketTimeoutMS=20000,
        serverSelectionTimeoutMS=20000,
    )

    try:
        client.admin.command("ping")
    except PyMongoError as exc:
        print("\nMongoDB ping failed:")
        print(type(exc).__name__)
        print(exc)
        raise SystemExit(1) from exc

    print("\nMongoDB ping successful.")


if __name__ == "__main__":
    main()
