import requests

url = "https://paphus-botlibre.p.rapidapi.com/form-chat"
headers = {
        'x-rapidapi-host': "paphus-botlibre.p.rapidapi.com",
        'x-rapidapi-key': "7520eb7294mshfd402f9e633420bp10d9e8jsn0a0ef7982e47"
}

def chat():
    texto = input("First message: ")
    query = {"instance": 667676, "message": texto, "application": "6841305405613846648"}

    response = requests.request("GET", url, headers=headers, params=query)

    text = response.text.split('>')[3].split('<')[0]
    print("1: " + text)
    respuesta = responder(text)
    print("2: " + respuesta)

    query = {"instance": 667676, "message": respuesta, "application": "6841305405613846648"}

    response = requests.request("GET", url, headers=headers, params=query)
    text = response.text.split('>')[3].split('<')[0]
    print("1: " + text)

    respuesta = responder(text)
    print("2: " + respuesta)
    # print(response.text)


def responder(message):
    query = {"instance": 12332376, "message": message, "application": "6841305405613846648"}

    response = requests.request("GET", url, headers=headers, params=query)

    return response.text.split('>')[3].split('<')[0]

if __name__ == '__main__':
    chat()
