from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="home"),
    path('apis',views.pagApis,name="apis"),
    path('apiDatUser',views.datos_user,name="apiDatUser"),
    path('apiInst',views.Instituciones_Views,name="apiInst"),
    path('apiInst/<int:idi>',views.Institucion_View),
    path('apiInsc',views.Inscritos_Views.as_view(),name="apiInsc"),
    path('apiInsc/<int:id>',views.Inscrito_Views.as_view()),
    path('Listado',views.listado,name="listado"),
    path('Agregar',views.agregar,name="agregar"),
    path('AgregarInst',views.agregarInst,name="agregarinst"),
    path('edit/<int:id_edit>',views.editar,name="edit"),
    path('del/<int:id_del>',views.eliminar,name='del'),

]