from .views import PersonViewset
from django.urls import path
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('', PersonViewset, basename='person')
# urlpatterns = router.urls

urlpatterns = [
	path('api', PersonViewset.as_view({'get': 'list'})),
	path('api/<int:pk>', PersonViewset.as_view({'get': 'retrieve'})),
	path('api', PersonViewset.as_view({'post': 'create'})),
	path('api/<int:pk>', PersonViewset.as_view({'put': 'update'})),
	path('api/<int:pk>', PersonViewset.as_view({'delete': 'destroy'})),
	path('api/', PersonViewset.as_view({'get': 'list'})),
	path('api/<int:pk>/', PersonViewset.as_view({'get': 'retrieve'})),
	path('api/', PersonViewset.as_view({'post': 'create'})),
	path('api/<int:pk>/', PersonViewset.as_view({'put': 'update'})),
	path('api/<int:pk>/', PersonViewset.as_view({'delete': 'destroy'})),
]