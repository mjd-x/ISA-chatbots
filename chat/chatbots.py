import requests
from .models import Message, Chat, User

url = "https://paphus-botlibre.p.rapidapi.com/form-chat"
headers = {
        'x-rapidapi-host': "paphus-botlibre.p.rapidapi.com",
        'x-rapidapi-key': "7520eb7294mshfd402f9e633420bp10d9e8jsn0a0ef7982e47"
}

def chat(message, chatId):
    # arma la query con el primer mensaje
    query = {"instance": 667676, "message": message, "application": "6841305405613846648"}
    response = requests.request("GET", url, headers=headers, params=query)  # respuesta
    try:
        text = response.text.split('>')[3].split('<')[0]  # trae el texto del mensaje
    except IndexError:
        raise Exception("Hubo un error con la request: " + response.text)

    # busco el objeto chat para tener los usuarios, el primer mensaje lo mando user1, la primer respuesta user2
    chat = Chat.objects.get(id=chatId)
    Message.objects.create(idUser=chat.idUser2, message=text, idChat=chatId)  # creo el nuevo mensaje

    # consigo mensaje de la respuesta (user1)
    respuesta = responder(text)
    Message.objects.create(idUser=chat.idUser1, message=respuesta, idChat=chatId)  # creo el nuevo mensaje

    # manda query con respuesta
    query = {"instance": 667676, "message": respuesta, "application": "6841305405613846648"}

    response = requests.request("GET", url, headers=headers, params=query)
    text = response.text.split('>')[3].split('<')[0]
    Message.objects.create(idUser=chat.idUser2, message=text, idChat=chatId)  # creo el nuevo mensaje

    respuesta = responder(text)
    Message.objects.create(idUser=chat.idUser1, message=respuesta, idChat=chatId)  # creo el nuevo mensaje



def responder(message):
    query = {"instance": 12332376, "message": message, "application": "6841305405613846648"}

    response = requests.request("GET", url, headers=headers, params=query)

    return response.text.split('>')[3].split('<')[0]