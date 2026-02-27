from django.shortcuts import render
from rest_framework import generics, permissions, renderers
from .models import Snippet
from .serializer import SnippetSerializer, UserSerializer
from django.contrib.auth.models import User
from .permission import IsOwnerOrReadOnly
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action
from rest_framework.response import Response


from rest_framework import viewsets



# =============  Use Generic rest_framework   =======================
# Create your views here.

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response(
#         {
#             "users": reverse("user_list", request=request, format=format),
#             "snippets": reverse("snippet_list", request=request, format=format)
#         }
#     )


# class SnippetHighlight(generics.GenericAPIView):  # new
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.code)


# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes=[permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     # permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

#     # def perform_update(self, serializer):
#     #     if self.get_object().owner != self.request.user:
#     #         raise permissions.PermissionDenied("No Permission to update the data")
#     #     serializer.save()


# class UserListView(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserRetriveView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer




# =================  Use Viewsets rest_framework   =======================

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = SnippetSerializer

    # we've used the '@action' decorator to create a custom action, named 'highlight'.
    # This decorator can be used to add any custom endpoints that don't fit into the standard create/update/delete style.
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])  
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.code)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)



