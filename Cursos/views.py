from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
import requests
from .models import *
from rest_framework import viewsets ,generics,status
from .serializers import *

from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser



class VersionesViewsets(viewsets.ModelViewSet):
    queryset =Versiones.objects.all()
    serializer_class = VersionesSerializers

    def create(self, request, *args, **kwargs):
        response = requests.get('https://restcountries.eu/rest/v2/lang/es')
        ejemplo = response.json(*args, **kwargs)
        print((response.json()))

        serializer = VersionesSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("ferney")
            try:
                version = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)




class EstudiantesViewsets(viewsets.ModelViewSet):
    queryset = Estudiantes.objects.all()
    serializer_class = EstudiantesSerializers

class DispositivosViewsets(viewsets.ModelViewSet):
    queryset = Dispositivos.objects.all()
    serializer_class = DispositivosSerializers



    def create(self, request, *args, **kwargs):

        serializer = DispositivosSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            try:
                dispositivo = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



    @action(methods=['get'], detail=True)
    def mac(self, request, pk=None):

        try:
            queryset = Dispositivos.objects.filter(MAC=pk)
            serializer_class = DispositivosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    """
    @action(methods=['get'], detail=True)
    def mac(self, request,pk= None):

        app_creds = {'app_id': 'G9nUpvbZQyiPrk3um2YAkQ', 'app_key': 'ybZu7fm_JKJTFwKEHfoZ7Q'}
        ac = d2lauth.fashion_app_context(app_id=app_creds['app_id'], app_key=app_creds['app_key'])
        redirect_url = 'http://localhost:8080?x_a=dC31ncmeHGvtullmp-6xSu&x_b=GPo8Rm7ou1fxZ7D8JHKOu1&x_c=093VuH_tHn1WGlla7pQ7MvGDJUX8lZ5gS5jwOgR8xNE'
        uc = ac.create_user_context(result_uri=redirect_url, host='devcop.brightspace.com', encrypt_requests=True)
        route = '/d2l/api/versions/'
        url = uc.create_authenticated_url(route)
        url
        'https://devcop.brightspace.com/d2l/api/versions/?x_t=1338916317&x_d=lz2D5RD9LFejpriJTcw7QD8FaBPymmWpK0_mdNt5on0&x_b=dC31ncmeHGvtullmp-6xSu&x_c=pRir1VlN73yhAytcLq6kQ4krBv563YoASnKcJSwdBBY&x_a=G9nUpvbZQyiPrk3um2YAkQ'
        r = requests.get(url)
        r.status_code
        print(r.status_code)

        try:
            queryset = Dispositivos.objects.filter(MAC=pk)
            serializer_class = DispositivosSerializers(queryset,many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

"""


"""
    def create(self, request, *args, **kwargs):

        response = requests.get('https://restcountries.eu/rest/v2/lang/es')
        ejemplo = response.json(*args, **kwargs)
        print(len(ejemplo))

        for i in ejemplo:
            serializer = DispositivosSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                request.data._mutable = True
                request.data['MAC'] = i["name"]
                dispositivo = serializer.save()
                request.data._mutable = False
        return Response(serializer.data, status=status.HTTP_200_OK)
"""








class ProfesoresViewsets(viewsets.ModelViewSet):
    queryset = Profesores.objects.all()
    serializer_class = ProfesoresSerializers

    def pre_save(self, obj):
        obj.samplesheet = self.request.FILES.get('file')


class GradosViewsets(viewsets.ModelViewSet):
    queryset = Grados.objects.all()
    serializer_class = GradosSerializers
    parser_classes = (MultiPartParser, JSONParser,)

class MateriasViewsets(viewsets.ModelViewSet):
    queryset = Materias.objects.all()
    serializer_class = MateriasSerializers

    @action(methods=['get'], detail=True)
    def curso(self, request, pk=None):

        try:
            queryset = Materias.objects.filter(curso=pk)
            serializer_class = MateriasSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)




class TareasViewsets(viewsets.ModelViewSet):
    queryset = Tareas.objects.all()
    serializer_class = TareasSerializers


    def create(self, request, *args, **kwargs):

        serializer = TareasSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print("ferney")
            try:
                dispositivo = serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            except  Exception:
                return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Tareas.objects.filter(materias=pk)
            serializer_class = TareasSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)



class EvaluacionesViewsets(viewsets.ModelViewSet):
    queryset = Evaluaciones.objects.all()
    serializer_class = EvaluacionesSerializers

    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Evaluaciones.objects.filter(materias=pk)
            serializer_class = EvaluacionesSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EntregasViewsets(viewsets.ModelViewSet):
    queryset = Entregas.objects.all()
    serializer_class = EntregasSerializers



class EjerciciosViewsets(viewsets.ModelViewSet):
    queryset = Ejercicios.objects.all()
    serializer_class = EjerciciosSerializers

    @action(methods=['get'], detail=True)
    def clases(self, request, pk=None):
        print(pk)
        try:
            queryset = Ejercicios.objects.filter(clases=pk)
            serializer_class = EjerciciosSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)



class PlaneacionViewsets(viewsets.ModelViewSet):
    queryset = Planeacion.objects.all()
    serializer_class = PlaneacionesSerializers


class MaterialEstudioViewsets(viewsets.ModelViewSet):
    queryset = MaterialEstudio.objects.all()
    serializer_class = MaterialEstudioSerializers

    @action(methods=['get'], detail=True)
    def clases(self, request, pk=None):
        print(pk)
        try:
            queryset = MaterialEstudio.objects.filter(clases=pk)
            serializer_class = MaterialEstudioSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)

    @action(methods=['get'], detail=True)
    def blobmaterialestudio(self, request, pk=None):
        try:
            queryset = MaterialEstudio.objects.filter(blob__codigo=pk)

            serializer_class = MaterialEstudioSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)



class ClasesViewsets(viewsets.ModelViewSet):
    queryset = Clases.objects.all()
    serializer_class = ClasesSerializers

    @action(methods=['get'], detail=True)
    def materias(self, request, pk=None):
        print(pk)
        try:
            queryset = Clases.objects.filter(materias=pk)

            serializer_class = ClasesSerializers(queryset, many=True).data
            return Response(serializer_class, status=status.HTTP_200_OK)
        except Exception:
            return Response(status=status.HTTP_404_NOT_FOUND)


class SubidasViewsets(viewsets.ModelViewSet):
    queryset = Subidas.objects.all()
    serializer_class = SubidasSerializers