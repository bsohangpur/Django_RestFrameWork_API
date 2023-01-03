from django.db import models

# project category model


class Language(models.Model):
    name = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.name

# projects images model


class Image(models.Model):
    url = models.ImageField(upload_to='projects/',
                           max_length=100, null=True, default="")

    def __str__(self):
        return str(self.url)

# main projects models


class Project(models.Model):
    title = models.CharField(max_length=50, default="")
    describtion = models.TextField(default="")
    languageAndTool = models.ManyToManyField(
        'Language', related_name='tools', default="")
    images = models.ManyToManyField(
        'Image', related_name='images', default="")
    workflow_link = models.CharField(max_length=255, default="")
    project_link = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=20, default="")
    email = models.EmailField(default="")
    subject = models.CharField(max_length=255, default="")
    message = models.TextField(default="")

    def __str__(self):
        return self.name


class Service(models.Model):
    images = models.ManyToManyField(
        'Image', related_name='service_images', default="")
    title = models.CharField(max_length=255, default="")
    detail = models.TextField(default="")

    def __str__(self):
        return self.title


class Skill(models.Model):
    title = models.ForeignKey(Language, on_delete=models.PROTECT, default="")
    image = models.ForeignKey(Image, on_delete=models.PROTECT, default="")

    def __str__(self):
        return str(self.title)
