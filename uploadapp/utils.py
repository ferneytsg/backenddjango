from django.contrib import admin
import requests
import json


token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6IjgyODRlOGU1LTQxOWQtNDJiMS04OTE0LTI3YzVmOWQ2MzJmZiJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NjQyMjM2LCJuYmYiOjE1OTY2Mzg2MzYsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiJmMWMyYWZmMC1jOGIzLTRjYzQtYTFhZS1iY2ZhZjgzNjMwMTgifQ.xW0bMWGouKbJtY2AfWXq3WHO_ACCbHCVZpYq0PqufiaK7Q-bQXZK3F_TdpVwkYNa8QrGeA-R6cICl9pCoKTgDV8_386Ej3izTDcOIvQjVZVZo24imohUY7Ugq7zbdjne8j5QDea201ESrpPnm7mjLgK7g3AbLcRmPC2JA6BZQW1xxalCE1pHgyGmlRnAvVDsYQBZ0RVvFfMG3RD5akyzBBKzNnOLtD0SDViVwAQ1rFOOdlUP1sIVVphpWQRCpsYmfjGMgOLPPG6mHGemvzA8mx6ZYfKjFNivEByqR1m61mX4RULhCljIwq_ItOMdmD8Yu0y_8WW4YHP1U1i9Kaxe_A'
headers = {'Authorization': 'Bearer ' +
           token, }

headersMessage = {'Authorization': 'Bearer ' +
                  token, 'content-type': 'application/json'}


def createCourse():

    url = 'https://tsgprueba.brightspacedemo.com/d2l/api/lp/1.9/courses/'

    body = {
        "Name": "Curso React",
        "Code": "gr2",
        "Path": "",
        "CourseTemplateId": 6629,
        "SemesterId": None,
        "StartDate": None,
        "EndDate": None,
        "LocaleId": None,
        "ForceLocale": False,
        "ShowAddressBook": False
    }

    r = requests.post(url, data=json.dumps(body), headers=headers)
    response = r.json()
    print(response)


# createCourse()


def createMessage():

    url = 'https://prd.activityfeed.us-east-1.brightspace.com/api/v1/d2l:orgUnit:6728/article'

    body = {
        "attachment": [
            {
                "type": "Document",
                        "name": "image.jpg",
                        "url": [
                            {
                                "href": "https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.files.api.brightspace.com/6606_645000_6728_react.png/usages/6728",
                                "mediaType": "application/vnd.siren+json",
                                "rel": ["https://files.api.brightspace.com/rels/files"]
                            },
                            {
                                "href": "https://tsgprueba.brightspacedemo.com/content/enforced/6728-gr2/react.png",
                                "mediaType": "image/jpeg",
                                "rel": ["alternate"]
                            }
                        ]
            }
        ],
        "closed": False,
        "content": "<p>Mensaje curso de react creado desdee django ultimosss2</p>"
    }

    r = requests.post(url, data=json.dumps(body), headers=headersMessage)
    response = r.json()
    print(r)
    print(response)


# createMessage()


def uploadFiles():

    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.files.api.brightspace.com/6728/upload'
    archivo='C:/Users/Ferney/Documents/GitHub/gobernacion_env/gobernacion/media/python.jpg'
   # archivo='http://127.0.0.1:8000/media/wartegg_page-0001.jpg'
    titulo=''
    for i in reversed(archivo):
        if i=='/':
           break
        titulo = i + titulo
    print(titulo)
    body = {
      #  'file': ('python.jpg', open('C:/Users/Ferney/Documents/GitHub/gobernacion_env/gobernacion/media/TAREA_ELECTIVA.docx', 'rb'), 'multipart/form-data')
        'file': (titulo,open(archivo, 'rb'),'multipart/form-data')

    }

    r = requests.post(url, files=body, headers=headers)

    response = r.json()
    for i in response:
        print(i)
    #print(response['class'])
    #print(response['properties'])
    print(response['links'])
    print(response['rel'])
    print(response)


    print("*****************")
    #print(r)
    #print(response)

uploadFiles()