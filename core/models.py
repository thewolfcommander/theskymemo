from django.db import models

# Create your models here.
class CommonInfo(models.Model):
    """
    This model is for the information that is going to be shared between the different models
    """
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)


class Contact(CommonInfo):
    """
    This model is for holding contact info
    """
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)


    class Meta:
        ordering = ('updated', 'name',)
        verbose_name = 'People who Contacted'
        verbose_name_plural = 'People who Contacted'

