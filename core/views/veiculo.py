from rest_framework.viewsets import ModelViewSet

from core.models import Veiculo
from core.serializers import veiculoSerializer

...
class veiculoViewSet(ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = veiculoSerializer