from rest_framework import routers
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, ArticleFeedbackViewSet

router = SimpleRouter(trailing_slash=False)
router.register("article", ArticleViewSet)
router.register("feedback", ArticleFeedbackViewSet)

urlpatterns = [

]

urlpatterns += router.urls
