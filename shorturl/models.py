from django.db import models

class UrlShort(models.Model):
    ori_link = models.CharField(max_length=255)
    hash_link = models.CharField(max_length=255)
    short_link = models.CharField(unique=True, db_index=True, max_length=50)