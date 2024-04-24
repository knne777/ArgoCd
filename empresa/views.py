from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Empresa

class EmpresaView(APIView):
    def post(self, request):
        print(request.data)
        data = request.data
        empresa = Empresa(name=data['name'],descripcion=data['descripcion'])
        empresa.save()
        return Response(200)
    def get(self,request):
        itmes = [(x.name, x.descripcion) for x in Empresa.objects.all()]
        return Response(itmes)


# Create your views here.
