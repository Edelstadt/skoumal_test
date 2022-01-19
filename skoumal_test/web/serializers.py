from requests import get as requests_get
from rest_framework import serializers
from web.models import Author, WebSite


class WebSiteSerializer(serializers.ModelSerializer):
    length = serializers.SerializerMethodField(read_only=True)

    def validate(self, attrs):
        url = attrs.get("url", None)

        if url:
            try:
                req = requests_get(url)
                if req.status_code == 200:
                    attrs["length"] = len(req.content)

                    return attrs
                raise Exception
            except Exception as error:
                raise serializers.ValidationError(
                    "URL is not a valid Address"
                ) from error

        return attrs

    @staticmethod
    def get_length(obj):
        return obj.length

    class Meta:
        model = WebSite
        fields = "__all__"
        partial = True


class AuthorSerializer(serializers.ModelSerializer):
    web_sites = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = "__all__"

    @staticmethod
    def get_web_sites(obj):
        return WebSiteSerializer(WebSite.objects.filter(author=obj.id), many=True).data
