from api.views import ContactUsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'contacts', ContactUsViewSet, basename='contact')
urlpatterns = router.urls