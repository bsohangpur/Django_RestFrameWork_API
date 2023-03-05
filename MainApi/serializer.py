# from dataclasses import field
# from pyexpat import model
from rest_framework import serializers
from MainApi.models import Project, Image, Language, Contact, Service, Skill


# Project image serializer...


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('url')

# Project category serializer...


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('name')

# Project main serializer...

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    language_and_tool_names = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'title', 'describtion', 'images',
                  'language_and_tool_names', 'workflow_link', 'project_link')

    def get_language_and_tool_names(self, obj):
        return [item.name for item in obj.languageAndTool.all()]

    def get_images(self, obj):
        request = self.context.get('request')
        image_urls = []

        for image in obj.images.all():
            if image.url:
                # get the URL for the image based on the MEDIA_ROOT and MEDIA_URL settings
                image_url = image.url.url

                # if the request is available, prepend the domain and protocol to the URL
                if request is not None:
                    image_url = request.build_absolute_uri(image_url)

                image_urls.append(image_url)

        return image_urls


# contact serializer

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']


# service serializer

class ServiceSerializer(serializers.ModelSerializer):
    image_urls = serializers.SerializerMethodField()

    class Meta:
        model = Service
        fields = ['title', 'image_urls', 'detail']

    def get_image_urls(self, obj):
        return [str(image.url) for image in Image.objects.all()]


# skill serializer

class SkillSerializer(serializers.ModelSerializer):
    skill_title= serializers.SerializerMethodField()
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Skill
        fields = ['skill_title', 'image']

    def get_skill_title(self, obj):
        return str(obj)
        # return [item for item in obj.title.all()]
