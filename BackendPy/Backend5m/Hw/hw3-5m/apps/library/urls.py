from rest_framework.routers import DefaultRouter

from .views import AuthorAPI, BookAPI, GenreAPI

router = DefaultRouter()
router.register('author', AuthorAPI, basename="author API")

urlpatterns = [
    
]

urlpatterns += router.urls

router.register('book', BookAPI, basename="book API")
urlpatterns += router.urls
router.register('genre', GenreAPI, basename="genre API")
urlpatterns += router.urls