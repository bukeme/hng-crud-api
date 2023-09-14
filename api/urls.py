from .views import PersonViewset
from django.urls import path
# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register('', PersonViewset, basename='person')
# urlpatterns = router.urls

urlpatterns = [
	path('api', PersonViewset.as_view({'get': 'list'}), name='person-list'),
	path('api/<int:pk>', PersonViewset.as_view({'get': 'retrieve'}), name='person-detail'),
	path('api', PersonViewset.as_view({'post': 'create'}), name='person-create'),
	path('api/<int:pk>', PersonViewset.as_view({'put': 'update'}), name='person-update'),
	path('api/<int:pk>', PersonViewset.as_view({'delete': 'destroy'}), name='person-destroy'),
	path('api/', PersonViewset.as_view({'get': 'list'}), name='person-list'),
	path('api/<int:pk>/', PersonViewset.as_view({'get': 'retrieve'}), name='person-detail'),
	path('api/', PersonViewset.as_view({'post': 'create'}), name='person-create'),
	path('api/<int:pk>/', PersonViewset.as_view({'put': 'update'}), name='person-update'),
	path('api/<int:pk>/', PersonViewset.as_view({'delete': 'destroy'}), name='person-destroy'),
]