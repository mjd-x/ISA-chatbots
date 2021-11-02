import requests
from .models import Message, Chat, User

url = "https://paphus-botlibre.p.rapidapi.com/form-chat"
headers = {
        'x-rapidapi-host': "paphus-botlibre.p.rapidapi.com",
        'x-rapidapi-key': "651c607c7cmshe3ed5dd06be028dp1de91ajsn0747a216b052"
}

appId = "983797852788671498"

def chat(message, chatInstance):
    # arma la query con el primer mensaje
    #query = {"instance": 667676, "message": message, "application": appId}
    query = {"instance": 12332376, "message": message, "application": appId}
    
    response = requests.request("GET", url, headers=headers, params=query)  # respuesta
    print(response)
    
    try:
        text = response.text.split('>')[3].split('<')[0]  # trae el texto del mensaje
        print(text)
    except IndexError:
        raise Exception("Hubo un error con la request: " + response.text)

    # busco el objeto chat para tener los usuarios, el primer mensaje lo mando user1, la primer respuesta user2
    chat = Chat.objects.get(id=chatInstance.id)
    Message.objects.create(idUser=chat.idUser2, message=text, idChat=chatInstance)  # creo el nuevo mensaje

    # consigo mensaje de la respuesta (user1)
    respuesta = responder(text)
    print(respuesta)
    Message.objects.create(idUser=chat.idUser1, message=respuesta, idChat=chatInstance)  # creo el nuevo mensaje

    # manda query con respuesta
    query = {"instance": 12332376, "message": respuesta, "application": appId}

    response = requests.request("GET", url, headers=headers, params=query)
    print(response)
    text = response.text.split('>')[3].split('<')[0]
    print(text)
    Message.objects.create(idUser=chat.idUser2, message=text, idChat=chatInstance)  # creo el nuevo mensaje

    respuesta = responder(text)
    print(respuesta)
    Message.objects.create(idUser=chat.idUser1, message=respuesta, idChat=chatInstance)  # creo el nuevo mensaje



def responder(message):
    query = {"instance": 12332376, "message": message, "application": appId}

    response = requests.request("GET", url, headers=headers, params=query)
    print(response)

    return response.text.split('>')[3].split('<')[0]
