from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet

router = SimpleRouter(trailing_slash=False)
router.register("article", ArticleViewSet)

urlpatterns = [

]

urlpatterns += router.urls
