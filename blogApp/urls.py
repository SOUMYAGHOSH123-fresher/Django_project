from django.urls import path, include
from .views import BlogViewSet
from rest_framework.routers import DefaultRouter
from .views import BlogListCreateView, BlogRetiveUpdateDeleteView

router = DefaultRouter()
router.register(r'blogs', BlogViewSet)

urlpatterns = [
    # path("", include(router.urls)),
    path('blogs/', BlogListCreateView.as_view()),
    path('blogs/<int:id>/', BlogRetiveUpdateDeleteView.as_view())
]


