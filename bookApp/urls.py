from django.urls import path, include
from rest_framework.routers import DefaultRouter    # 'DefaultRouter'   is a 'URL generator' for 'ViewSets' in Django REST Framework.
from bookApp.views import BookListCreateView, BookDetailView, BookDetailsView


# When we use ViewSets, 'router' does this for you.
router = DefaultRouter()
# router.register(r'books', BookListCreateView, basename='book')
router.register(r'books', BookDetailsView, basename='book')


urlpatterns = [
    path("", include(router.urls)),    # use in viewsets only
    # path('books/', BookListCreateView.as_view()),
    # path('books/<int:pk>/', BookDetailView.as_view()),
]
