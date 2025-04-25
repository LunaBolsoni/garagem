from rest_framework.serializers import ModelSerializer

from core.models import veiculo

class veiculoSerializer(ModelSerializer):
    class Meta:
        model = veiculo
        fields = "__all__"