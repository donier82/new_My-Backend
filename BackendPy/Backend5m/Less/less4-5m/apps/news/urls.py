from rest_framework.routers import DefaultRouter

from .views import NewsAPI

router = DefaultRouter()
router.register('news', NewsAPI, basename="news API")

urlpatterns = [
    
]

urlpatterns += router.urls