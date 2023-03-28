from rest_framework import viewsets
from apps.tutores.models import Tutor
from apps.tutores.serializer import TutorSerializer


class TutoresViewSet(viewsets.ModelViewSet):
    """Exibindo todos os tutores"""
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer