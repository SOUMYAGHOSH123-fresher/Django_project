from .models import Snippet
from rest_framework import serializers
from django.contrib.auth.models import User 


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='snippet_highlight', format="html"
    # )

    class Meta:
        model=Snippet
        fields=[
            # "url",
            "id",
            # "highlight",
            "title",
            "code",
            "linenos",
            "language",
            "owner",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedIdentityField(
        view_name='snippet_detail', read_only=True, many=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']



# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         exclude = ['created']


# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(
#         many=True, queryset=Snippet.objects.all()
#     )

#     class Meta:
#         model = User
#         fields =['id', 'username', 'snippets']


