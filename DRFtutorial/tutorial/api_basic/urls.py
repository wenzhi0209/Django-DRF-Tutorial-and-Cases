import imp
from django.urls import path,include
from .views import  article_list,article_detail,ArticleAPIView,ArticleDetails,GenericAPIView,GenericAPIViewDetail,ArticleViewSet
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('article',ArticleViewSet,basename='article')

urlpatterns = [

    path('viewset/',include(router.urls)),
    path('viewset/<int:pk>/',include(router.urls)),
    path('article/',article_list),
    path('detail/<int:pk1>/',article_detail),
    path('articleAPI/',ArticleAPIView.as_view()),
    path('articleDetailAPI/<int:id>/',ArticleDetails.as_view()),
    path('generic/article/<int:pk>/',GenericAPIViewDetail.as_view()),
    path('generic/article/',GenericAPIView.as_view())
]