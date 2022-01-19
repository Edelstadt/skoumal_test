from rest_framework import viewsets, mixins
from web.serializers import AuthorSerializer, WebSiteSerializer
from web.models import Author, WebSite


class AuthorViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class WebSiteViewSet(
    mixins.CreateModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet
):
    queryset = WebSite.objects.all()
    serializer_class = WebSiteSerializer
