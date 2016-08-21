"""API Routes for core models."""
from rest_framework import routers, serializers, viewsets

from core import models


class RealEstateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.RealEstate
        fields = ('id', 'name', 'url')


class RealEstateViewSet(viewsets.ModelViewSet):
    # filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'url')

    queryset = models.RealEstate.objects.filter(is_active=True)
    serializer_class = RealEstateSerializer


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('image',)


class ImmobileSerializer(serializers.ModelSerializer):
    image_set = ImageSerializer(many=True)

    class Meta:
        model = models.Immobile
        # fields = ()

    def create(self, validated_data):
        images = validated_data.pop('image_set')
        immobile = models.Immobile.objects.create(**validated_data)

        for image in images:
            models.Image.objects.create(immobile=immobile, image=image['image'])
        return immobile


class ImmobileViewSet(viewsets.ModelViewSet):
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('city', 'real_estate')

    # queryset = models.Immobile.objects.filter(is_active=True).prefetch_related('image_set')
    queryset = models.Immobile.objects.all()
    serializer_class = ImmobileSerializer


router = routers.DefaultRouter()
router.register(r'immobiles', ImmobileViewSet)
router.register(r'real-estates', RealEstateViewSet)
