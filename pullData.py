import requests

TACO_API = "https://ct-tacoapi.azurewebsites.net"

def parseData(data):
    for item in data:
        print(item)
    print(len(data))
    print(data[0])



def getShells():
    response = requests.get(TACO_API + "/shells")
    response.raise_for_status()
    clients = response.json()
    if not clients:
        return "-"
    return parseData(clients)


getShells()


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

    