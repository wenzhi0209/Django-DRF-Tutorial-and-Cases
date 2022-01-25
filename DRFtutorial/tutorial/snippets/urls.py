from django.urls import path,include
from snippets import views
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet, UserViewSet
from rest_framework import renderers

snippet_list=SnippetViewSet.as_view({
    'get':'list',
    'post':'create'
})

snippet_detail=SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

snippet_highlight=SnippetViewSet.as_view({
    'get':'highlight'
},renderer_classes=[renderers.StaticHTMLRenderer])

user_list=UserViewSet.as_view({
    'get':'list'
})

user_detail= UserViewSet.as_view({
    'get':'retrieve'
})

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]