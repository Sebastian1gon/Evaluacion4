from rest_framework import serializers
from SG_Ev3y4_app import models


class InscritosSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Inscritos
        fields = '__all__'

class InstitucionSerial(serializers.ModelSerializer):
    class Meta:
        model = models.Institucion
        fields = '__all__'