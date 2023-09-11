from rest_framework import viewsets
from .serializers import PersonSerializer
from .models import Person



class PersonViewset(viewsets.ModelViewSet):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer