from .views import PersonListCreateGenericView, PersonDetailUpdateDestroyGenericView
from django.urls import path

urlpatterns = [
	path('api', PersonListCreateGenericView.as_view()),
	path('api/<int:pk>', PersonDetailUpdateDestroyGenericView.as_view()),
	path('api/', PersonListCreateGenericView.as_view()),
	path('api/<int:pk>/', PersonDetailUpdateDestroyGenericView.as_view()),
]