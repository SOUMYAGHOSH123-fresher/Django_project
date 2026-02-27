from django.urls import path, include
from SnippetApp import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import renderers
# from .views import UserViewSet, SnippetViewSet, api_root


##  ----  Binding ViewSets to URLs explicitly   ----
# snippet_list = views.SnippetViewSet.as_view({'get': 'list', 'post': 'create'})
# snippet_detail = views.SnippetViewSet.as_view(
#     {"get": "retrieve", "put": "update", "patch": "partial_update", "delete": "destroy"}
# )
# snippet_highlight = views.SnippetViewSet.as_view(
#     {'get': 'highlight'},
#     renderer_classes = [renderers.StaticHTMLRenderer]
# )
# user_list = views.UserViewSet.as_view({'get': 'list'})
# user_detail = views.UserViewSet.as_view({'get': 'retrieve'})


# urlpatterns = format_suffix_patterns(
#     [
#         path('', api_root),

#         path("snippets/", snippet_list, name='snippet_list'),
#         path('snippets/<int:pk>/', snippet_detail, name='snippet_detail'),
#         path("snippets/<int:pk>/highlight/", snippet_highlight, name='snippet_highlight'), 

#         path('users/',user_list, name='user_list'),
#         path('users/<int:pk>/', user_detail, name='user_detail'),
#     ]
# )



# ========================     Using Routers      =================
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views. UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path("", include(router.urls)),
]


