from rest_framework import generics, mixins
from .serializers import PersonSerializer
from .models import Person


class PersonListCreateGenericView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

	def get(self, request, *args, **kwargs):
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

class PersonDetailUpdateDestroyGenericView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

	def get(self, request, *args, **kwargs):
		return self.retrieve(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		return self.update(request, *args, **kwargs)

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)