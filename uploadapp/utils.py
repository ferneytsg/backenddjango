import json
import base64
import requests
from django.contrib import admin
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImE5YWZiODZkLWExZDEtNGIyNi04OTc5LTVjZjJhYjY4ZjViNiJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NzUwNDczLCJuYmYiOjE1OTY3NDY4NzMsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiIyOTNkYmE1NS03NzgxLTQzYWEtODBmOC1jNDE0YjgzZTE0ZTAifQ.Fnk_Db-7KJjbLg0AuWBf4WKkde_nNtr0g1F7yPSxGWodh4O9NV_EI6S8DjurDBgge1Zsz7cIa8vK8PQ4EfSdIoZFD7-QOlI5objAgsB293V6bxYIgnRNxBCbb-K41cIx4LQH-NryrS-kTj4_GHzq-h9E8cgQIdkjnJw3kJAZpy8joxpuAQpOwo73Ob3U5EZJ_Zj_O3hY0hJrf1HxNcWq6Co9ra9Th4A4FeGXFfrWg7RnDNAktoOPInmWhWBZo_IkcV3hXNY0D0Cf3zLciUL5UQMULmGUzRdJ7OMI0gsDlM1UT0Yw4jErqcMdrfpK-1JhYD3sDtfD7JVXwSrWQamMpw'
def createCourse():
    # ********************      Headers  *********************************************
    headers = {'Authorization': 'Bearer ' +
               token, }

    # ********************     creaci+on de curso  *********************************************
    url = 'https://tsgprueba.brightspacedemo.com/d2l/api/lp/1.9/courses/'

    body = {
        "Name": nombreCurso,
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
    idCursos = response["Identifier"]
    print(r)
    print("idCurso: "+str(idCursos)+'\n')


# Datos de entrada para crear un Curso
#token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImQ5ZDcwY2YzLTU2NzAtNGIyMy1hNDA0LWY2MTgxZWM4OWMzYyJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NjgwODA2LCJuYmYiOjE1OTY2NzcyMDYsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiI1YmM1NTNkMy1lYWQ3LTQzMzUtYTQ5MS05MmQzOThmN2RjNjQifQ.MrmB51si__io_tzgtClkHlvJEMoljrwvJ4p1DVOJ2NBDTeAechqAX0mfTiByyH0EenHALJEvv1dPVwtxirEzU2LoJPOsRUcQPMJ0INQHl96i5qNGbbKELuDAj1wkY8mZrJH1u7SIJG5CzGM6WvNhP8eAWswtQ7eVdfzikzWRZeBWkE3Ru-kODPcv5W1aQi4FL0bqsYE19ta9iqh-dZJkPeSOGF5BwQ9I-yHyHm-zftae_57-VYfBRV70zZuUugozAqYrHI-ixGuP-QZlgL-eJhmgp51fTJaFtbUZXrsi_fgAShMvyy96IJJP9XNUTfBJwL-3h3YInt8iMTVeEgYyVg'
nombreCurso = "Curso React desde python"
# ***********************************************

# createCourse()


def deleteCourse():
    # ********************      Headers  *********************************************
    headers = {'Authorization': 'Bearer ' +
               token, }

    # ********************     creaci+on de curso  *********************************************
    url = 'https://tsgprueba.brightspacedemo.com/d2l/api/lp/1.9/courses/'+idCursos

    r = requests.delete(url, headers=headers)
    print(r)


# Datos de entrada para crear un Curso
#token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImQ5ZDcwY2YzLTU2NzAtNGIyMy1hNDA0LWY2MTgxZWM4OWMzYyJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NjgwODA2LCJuYmYiOjE1OTY2NzcyMDYsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiI1YmM1NTNkMy1lYWQ3LTQzMzUtYTQ5MS05MmQzOThmN2RjNjQifQ.MrmB51si__io_tzgtClkHlvJEMoljrwvJ4p1DVOJ2NBDTeAechqAX0mfTiByyH0EenHALJEvv1dPVwtxirEzU2LoJPOsRUcQPMJ0INQHl96i5qNGbbKELuDAj1wkY8mZrJH1u7SIJG5CzGM6WvNhP8eAWswtQ7eVdfzikzWRZeBWkE3Ru-kODPcv5W1aQi4FL0bqsYE19ta9iqh-dZJkPeSOGF5BwQ9I-yHyHm-zftae_57-VYfBRV70zZuUugozAqYrHI-ixGuP-QZlgL-eJhmgp51fTJaFtbUZXrsi_fgAShMvyy96IJJP9XNUTfBJwL-3h3YInt8iMTVeEgYyVg'
idCursos = "6744"
# ***********************************************

# deleteCourse()


def createMessage():

    # ********************      Headers  *********************************************

    headers = {'Authorization': 'Bearer ' +
               token}

    headersMessage = {'Authorization': 'Bearer ' +
                      token, 'content-type': 'application/json'}

    # ********************      Cargar archivo *********************************************
    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.files.api.brightspace.com/'+idCurso+'/upload'

    body = {
        'file': (nombreArchivo, open(urlArchivo, 'rb'), 'multipart/form-data')
    }

    r = requests.post(url, files=body, headers=headers)
    response = r.json()
    link1 = response["links"][0]["href"]
    link2 = response["links"][1]["href"]
    tipo1 = response["links"][0]["type"]
    tipo2 = response["links"][1]["type"]
    name = response["properties"]["name"]

    print('\n'+"Csrga archivo, estado: " + str(r) + '\n')

    # ********************      creacion de mensaje *********************************************
    url = 'https://prd.activityfeed.us-east-1.brightspace.com/api/v1/d2l:orgUnit:' + \
        idCurso+'/article'

    body = {
        "attachment": [
            {
                "type": "Document",
                "name": name,
                "url": [
                    {
                        "mediaType": tipo1,
                        "href": link1
                    },
                    {
                        "mediaType": tipo2,
                        "href": link2
                    }
                ]
            }
        ],
        "closed": False,
        "content": mensaje
    }

    r = requests.post(url, data=json.dumps(body), headers=headersMessage)
    print("Creacion Mensaje, estado: " + str(r) + '\n')


# Datos de entrada para crear un mensaje
#token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImQ5ZDcwY2YzLTU2NzAtNGIyMy1hNDA0LWY2MTgxZWM4OWMzYyJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NjgwODA2LCJuYmYiOjE1OTY2NzcyMDYsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiI1YmM1NTNkMy1lYWQ3LTQzMzUtYTQ5MS05MmQzOThmN2RjNjQifQ.MrmB51si__io_tzgtClkHlvJEMoljrwvJ4p1DVOJ2NBDTeAechqAX0mfTiByyH0EenHALJEvv1dPVwtxirEzU2LoJPOsRUcQPMJ0INQHl96i5qNGbbKELuDAj1wkY8mZrJH1u7SIJG5CzGM6WvNhP8eAWswtQ7eVdfzikzWRZeBWkE3Ru-kODPcv5W1aQi4FL0bqsYE19ta9iqh-dZJkPeSOGF5BwQ9I-yHyHm-zftae_57-VYfBRV70zZuUugozAqYrHI-ixGuP-QZlgL-eJhmgp51fTJaFtbUZXrsi_fgAShMvyy96IJJP9XNUTfBJwL-3h3YInt8iMTVeEgYyVg'
idCurso = "6751"
mensaje = "<p>Mensaje para alumnos</p>"

nombreArchivo = "tsg.pdf"
carpetaArchivo = "D:/Archivos andres/Descargas/backenddjango-master/backenddjango-master/"
urlArchivo = carpetaArchivo + nombreArchivo
# ***********************************************

# createMessage()


def createAssignments():

    # ********************      Headers  *********************************************
    headers = {'Authorization': 'Bearer ' +
               token}

    headersMessage = {'Authorization': 'Bearer ' +
                      token, 'content-type': 'application/json'}

    # ********************      creacion de folder *********************************************
    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.assignments.api.brightspace.com/'+idCurso+'/folders'

    body = {
        "name": nombreAsignacion,
        "instructions": instrucciones,
        "dueDate": fechaEntrega,
    }

    r = requests.post(url, data=(body), headers=headers)
    print(r)
    response = r.json()
    print('\n')
    print("Creacion de folder, estado: " + str(r) + '\n')

    link1 = response["links"][2]['href']
    link2 = response["links"][0]['href']
    link3 = response["links"][4]['href']

    # ***********************      Cargar Archivo      *********************************************
    url = link2 + '/attach-file'

    body = {
        'file': (nombreArchivo, open(urlArchivo, 'rb'), 'multipart/form-data')
    }

    r = requests.post(url, files=body, headers=headers)
    print("Subir archivo, estado: " + str(r) + '\n')

    # ********************      crear asignacion    *********************************************
    url = 'https://prd.activityfeed.us-east-1.brightspace.com/api/v1/d2l:orgUnit:' + \
        idCurso + '/article'

    body = {
        "attachment": [],
        "closed": False,
        "type": "Assignment",
        "url": [
            {
                'href': link1,
                "rel": ["https://activities.api.brightspace.com/rels/internal-activity-id"]
            },
            {
                "href": link2,
                "rel": ["self", "https://api.brightspace.com/rels/assignment"]
            },
            {
                "href": link3,
                "rel": ["https://activities.api.brightspace.com/rels/activity-usage"]
            }
        ]
    }

    r = requests.post(url, data=json.dumps(body), headers=headersMessage)
    print("Creacion asignacion, estado: " + str(r) + '\n')


# Datos de entrada para crear una asigancion
#token = ' eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImtpZCI6ImE5YWZiODZkLWExZDEtNGIyNi04OTc5LTVjZjJhYjY4ZjViNiJ9.eyJpc3MiOiJodHRwczovL2FwaS5icmlnaHRzcGFjZS5jb20vYXV0aCIsImF1ZCI6Imh0dHBzOi8vYXBpLmJyaWdodHNwYWNlLmNvbS9hdXRoL3Rva2VuIiwiZXhwIjoxNTk2NzM3OTUwLCJuYmYiOjE1OTY3MzQzNTAsInN1YiI6IjIwNyIsInRlbmFudGlkIjoiZTUyOTU5N2EtZmQ4NS00YWI0LWI0ZTUtNmUzYjA5OTMyNWI0IiwiYXpwIjoibG1zOmU1Mjk1OTdhLWZkODUtNGFiNC1iNGU1LTZlM2IwOTkzMjViNCIsInNjb3BlIjoiKjoqOioiLCJqdGkiOiI2N2VhODA5MS1mOTE0LTQ5NGItYWZhNi02OTcwNzc5NWZhZmQifQ.ZJIiLpO2pn7FJgTcjqD-HpjWO8ODAWPy5v8hVUA-TlspiShWktYX06a4xWRpLowbaxtjdtY9ByEZ8Eih4K9kCDWB_4ZWqLytmHh_WHLO9FxsTD8Shs7_a8wwKtxj3HJ0kSrYiwJWEHWENUdXB8iiAuQtCtGmopwzJ3mi4fA_7RmPuKNS9NVEDNDAb5vZ4ca0lAUneQzT9Jwck9_YpGlh-z-kRZvL5Iw8LYgs81sp2YgrYUruIPMQDwiRCTmgfhSJ8Mu5EQCErct_5r0zL6k5nH10zz_HtWWPb15pCwa7gAbzpTdDVrgQN0vP1O8-_Utu6aKXCVFLx-cPSjAyzQMewg'
idCurso = "6751"
nombreAsignacion = "Tarea react urgente"
instrucciones = "<p>LLevar codigo</p>"
fechaEntrega = "2020-07-29T04:59:00.000Z"

nombreArchivo = "React.png"
carpetaArchivo = "D:/Archivos andres/Descargas/backenddjango-master/backenddjango-master/"
urlArchivo = carpetaArchivo + nombreArchivo
# ***********************************************

# Ejecutar funcion
# createAssignments()
"""

def coursesList():

    # ********************      Headers  *********************************************
    headers = {'Authorization': 'Bearer ' +
               token}

    # ********************      Headers  *********************************************
    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'

    r = requests.get(url, headers=headers)
    response = r.json()

    urlsCursos = []
    for data in response["entities"]:
        if data["class"][2] == "course-offering":
            urlsCursos.append(data["href"])

    cursos = ""
    idsCursos = []
    for urlCursos in urlsCursos:
        for i in reversed(urlCursos):
            if i == '/':
                break
            cursos = i + cursos
            if len(cursos) == 4:
                idsCursos.append(cursos)
                cursos = ""

    # ********************      Headers  *********************************************
    nombreCursos = []
    print('\n')
    diccionario = []
    for idCursos in idsCursos:
        url = 'https://tsgprueba.brightspacedemo.com/d2l/api/lp/1.9/courses/'+idCursos
        r = requests.get(url, headers=headers)
        response = r.json()
        # nombreCursos.append(response["Name"])
        # diccionario.append(dict.fromkeys(
        #     "1", response["Name"]))
        diccionario.append(
            {"id": response["Identifier"], "name": response["Name"]})

    for i in diccionario:
        #print(i['id'])
        #print(i['name'])
        #print(type(i["id"]))
        aux=int((i["id"]))
        #print(type(aux))

    # for nombre in nombreCursos:
    #     print(nombre)
    print('\n')

    return diccionario

#print(coursesList())

def images():
    cursoid='6647'
    # *******      Headers  ****************
    headers = {'Authorization': 'Bearer ' +
               token}

    # *******      Headers  ****************
    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'+cursoid

    r = requests.get(url, headers=headers)
    response = r.json()

    r = requests.get(response["entities"][2]["href"], headers=headers)
    responseImages = r.json()
    print('\n')
    urlImages = responseImages["links"][2]["href"]
    print(urlImages+'\n')

    def get_as_base64(url):
        return base64.b64encode(requests.get(url).content)

    #print(type(get_as_base64(urlImages)))
    return  get_as_base64(urlImages)


print(images())"""
def coursesList():

    # *******      Headers  ****************
    headers = {'Authorization': 'Bearer ' +
               token}

    # *******      Headers  ****************
    url = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'

    r = requests.get(url, headers=headers)
    response = r.json()

    urlsCursos = []
    for data in response["entities"]:
        if data["class"][2] == "course-offering":
            urlsCursos.append(data["href"])

    cursos = ""
    idsCursos = []
    for urlCursos in urlsCursos:
        for i in reversed(urlCursos):
            if i == '/':
                break
            cursos = i + cursos
            if len(cursos) == 4:
                idsCursos.append(cursos)
                cursos = ""

    # *******      Headers  ****************
    diccionario = []
    for id in idsCursos:
        url = 'https://tsgprueba.brightspacedemo.com/d2l/api/lp/1.9/courses/' + id
        url2 = 'https://e529597a-fd85-4ab4-b4e5-6e3b099325b4.organizations.api.brightspace.com/'+id
        r = requests.get(url, headers=headers)
        response = r.json()
        r2 = requests.get(url2, headers=headers)
        response2 = r2.json()
    # *******
        r3 = requests.get(response2["entities"][2]["href"], headers=headers)
        responseImages = r3.json()
        urlImages = responseImages["links"][2]["href"]

        def get_as_base64(url):
            return base64.b64encode(requests.get(url).content)
    # *******
        diccionario.append(
            {"id": response["Identifier"], "name": response["Name"], "images": get_as_base64(urlImages)})

    return diccionario

#print(coursesList())
