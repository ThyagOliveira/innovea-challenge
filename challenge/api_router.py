from rest_framework.routers import DefaultRouter
from articles.api.views.articles import ArticlesViewSet

router = DefaultRouter()
router.register("articles", ArticlesViewSet)

app_name = "api"
urlpatterns = router.urls