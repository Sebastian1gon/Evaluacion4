from django.shortcuts import render,redirect
from SG_Ev3y4_app.models import Inscritos,Institucion
from SG_Ev3y4_app.forms import FormInscritos,FormInstitucion
from SG_Ev3y4_app.serializer import InscritosSerial,InstitucionSerial
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404, response
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

def datos_user(request):
    data={'nombres':'Sebastian Elias','apellido':'Gonzalez','rut':'21.444.000-8','seccion':'(TI2041/IEI-170-N4/D Temuco IEI)'}
    return response.JsonResponse(data)

def index(request):
    return render(request,"html/index.html")

def listado(request):
    datosbd = Inscritos.objects.all()
    data= {'inscritos':datosbd}
    return render(request,"html/listado.html",data)

def agregar(request):
    form = FormInscritos()
    if request.method == 'POST':
        form = FormInscritos(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/Listado')
    data = {'formulario':form,'tutilo':"INSCRITO"}
    return render(request,"html/agregar.html",data)

def editar(request,id_edit):
    datosbd = Inscritos.objects.get(idins=id_edit)
    form = FormInscritos(instance=datosbd)
    if request.method == 'POST':
        form = FormInscritos(request.POST,instance=datosbd)
        if (form.is_valid()):
            form.save()
            return redirect('/Listado')
    data = {'formulario':form}
    return render(request,"html/actualizar.html",data)

def eliminar(request,id_del):
    datosbd = list(Inscritos.objects.filter(idins=id_del).values())
    if len(datosbd) >0:
        Inscritos.objects.filter(idins=id_del).delete()
    return redirect('/Listado')

#agregar Institucion
def agregarInst(request):
    form = FormInstitucion()
    if request.method == 'POST':
        form = FormInstitucion(request.POST)
        if (form.is_valid()):
            form.save()
            return redirect('/Listado')
    data = {'formulario':form,'tutilo':"INSTITUCIÓN"}
    return render(request,"html/agregar.html",data)


class Inscritos_Views(APIView):
    def get(self, request):
        inscritoss = Inscritos.objects.all()
        serials = InscritosSerial(inscritoss, many=True)
        return Response(serials.data)
        
class Inscrito_Views(APIView):
    def get_object(self, id):
        try:
            return Inscritos.objects.get(idins=id)
        except Inscritos.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        inscrito = self.get_object(id)
        serial = InscritosSerial(inscrito)
        return Response(serial.data)
       
@api_view(['GET'])
def Instituciones_Views(request):
    if request.method == 'GET':
        institucioones = Institucion.objects.all()
        serial = InstitucionSerial(institucioones, many=True)
        return Response(serial.data)
    
@api_view(['GET'])
def Institucion_View(request, idi):

    try:
        institucioon = Institucion.objects.get(id=idi)
    except Institucion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serial = InstitucionSerial(institucioon)
        return Response(serial.data)

def pagApis(request):
    return render(request,'html/Apis.html')