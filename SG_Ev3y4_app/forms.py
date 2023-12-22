from django import forms
from SG_Ev3y4_app import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

class FormInstitucion(forms.ModelForm):
    Nombre_Institucion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = models.Institucion
        fields = '__all__'

class FormInscritos(forms.ModelForm):
    Estados =[("RESERVADO","RESERVADO"),("COMPLETADA","COMPLETADA"),("ANULADA","ANULADA"),(" NO ASISTEN"," NO ASISTEN")]
    rut=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: 12345678-9'}),validators=[RegexValidator(regex=r'^[0-9]{8}-[0-9Kk]{1}$',message=_('El RUT no es válido. Debe seguir el formato XXXXXXXX-Y'))])
    nombre=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    telefono=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Ejemplo: 912345678','type': 'number'}),validators=[RegexValidator(regex=r'[\d]{9}',message=_('El Numero de telefono no  es correcto debe seguir el formato XXXXXXXXX e ingresar solo caracteres numéricos'))])
    fecha_inscripcion=forms.DateField(widget=forms.TextInput(attrs={'class':'form-control','type':'date'}))
    hora_inscripcion=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','type':'time'}))
    institucion=forms.ModelChoiceField(queryset=models.Institucion.objects.all(), initial=1,widget=forms.Select(attrs={'class':'form-control'}))
    estado=forms.CharField(widget=forms.Select(choices=Estados,attrs={'class':'form-control'}))
    observacion=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':"2"}),required=False)

    class Meta:
        model = models.Inscritos
        fields = ['rut','nombre','telefono','fecha_inscripcion','hora_inscripcion','institucion','estado','observacion']
