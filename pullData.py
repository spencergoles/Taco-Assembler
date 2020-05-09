import requests

TACO_API = "https://ct-tacoapi.azurewebsites.net"

def parseData(data):
    parsed = []
    for item in data:
        parsed.append(item["name"])
    return parsed


def getShells():
    response = requests.get(TACO_API + "/shells")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)


def getBaselayers():
    response = requests.get(TACO_API + "/baselayer")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)

def getMixins():
    response = requests.get(TACO_API + "/mixins")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)

def getCondiments():
    response = requests.get(TACO_API + "/condiments")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)

def getSeasonings():
    response = requests.get(TACO_API + "/seasonings")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)

    