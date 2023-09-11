from .views import PersonViewset
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', PersonViewset, basename='person')
urlpatterns = router.urls