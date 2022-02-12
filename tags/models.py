from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    tag = models.ForeignKey(Tag,on_delete=models.CASCADE)
    # Making generics to make it independent from product class. SO first content type is being used
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    # id of the model
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
