from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()

router.register('author', views.AuthorModelViewSet)
router.register('genre', views.GenreModelViewSet)
router.register('book', views.BookModelViewSet)


urlpatterns = router.urls
